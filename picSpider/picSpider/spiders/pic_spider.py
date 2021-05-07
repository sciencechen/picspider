
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
    start_urls = ['https://www.95mm.net/4873/2.html#98725']
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



        self.temp_pic_url.extend(pic_url)
        # yield scrapy.Request(pic_url[0])
        if len(self.temp_pic_url) > 0 :
            for url in self.temp_pic_url:
                yield scrapy.Request(url, meta={'filename': item['filename']}, callback=self.saveing)
            print('xxxxxxxx-----------xxxxxxxxxxxxx----完成saveing')
            print(self.temp_pic_url)
            self.temp_pic_url = []
            yield scrapy.Request(next_url[0], callback=self.parse)
        else:
            yield scrapy.Request(next_url[0], callback=self.parse)
        pass

    def saveing(self, response):
        # filename = '00.jpg'
        # with open(filename, 'wb') as fp:
        #     fp.write(response.body)
        #     print('xxxxxxxx-----------xxxxxxxxxxxxx----完成saveing')

        # self.picName = uuid.uuid1()
        self.picName = response.meta['filename']
        with open("C:/chenjimiao/project/python/aiTeacherPlan/images2/" + '{}.jpg'.format(self.picName),
                  'wb') as f:
            f.write(response.body)



