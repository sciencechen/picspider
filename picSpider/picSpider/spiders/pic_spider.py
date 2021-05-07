
import uuid

import scrapy

import sys
print(sys.path)
sys.path.append("..")
import items
from items import PicspiderItem



class PicSpiderSpider(scrapy.Spider):
    name = 'pic_spider'
    allowed_domains = ['95mm.net', 'cdn.zzdaye.com']
    start_urls = ['https://www.95mm.net/4879/2.html']
    picName = 0
    filename = '00.jpg'
    temp_pic_url = []

    def parse(self, response):
        next_url = response.xpath("/html[1]//div[@class='nc-light-gallery']/p[1]/a[1]/@href").extract()
        pic_url = response.xpath("/html[1]//div[@class='nc-light-gallery']/p[1]/a[1]/img/@src").extract()
        # print(pic_url)
        self.picName = response.xpath("/html//h1[@class='post-title h3']/text()").extract()
        item = PicspiderItem()
        item['filename'] = self.picName[0].replace("/", "-")
        item['picurl'] = pic_url[0]
        # yield item
        # yield scrapy.Request(next_url[0], callback=self.parse)
        # yield scrapy.Request(pic_url[0])

        # yield图片链接，然后保存
        yield scrapy.Request(pic_url[0], meta={'filename': item['filename']}, callback=self.saveing)
        print(self.temp_pic_url)
        self.temp_pic_url = []
        # 翻页，迭代，寻找下一个图片目标
        yield scrapy.Request(next_url[0], callback=self.parse)
        pass

    def saveing(self, response):
        # self.picName = uuid.uuid1()
        self.picName = response.meta['filename']
        with open("C:/chenjimiao/project/python/aiTeacherPlan/images3/" + '{}.jpg'.format(self.picName),
                  'wb') as f:
            f.write(response.body)
            print('xxxxxxxx---------xxxxxxxx---------完成saveing')



