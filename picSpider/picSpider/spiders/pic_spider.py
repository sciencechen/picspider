
import scrapy
import sys
import uuid
print(sys.path)
sys.path.append("..")
from items import PicspiderItem


class PicSpiderSpider(scrapy.Spider):
    name = 'pic_spider'
    allowed_domains = ['95mm.net', 'cdn.zzdaye.com']
    start_urls = ['https://www.95mm.net/2344/8.html']
    picName = 0

    def parse(self, response):
        next_url = response.xpath("/html[1]//div[@class='nc-light-gallery']/p[1]/a[1]/@href").extract()
        pic_url = response.xpath("/html[1]//div[@class='nc-light-gallery']/p[1]/a[1]/img/@src").extract()
        # print(pic_url)
        self.picName = response.xpath("/html//h1[@class='post-title h3']/text()").extract()
        item = PicspiderItem()
        item['filename'] = self.picName[0].replace("/", "-")
        item['picurl'] = pic_url[0]

        # yield图片链接，然后保存
        yield scrapy.Request(pic_url[0], meta={'filename': item['filename']}, callback=self.saveing)

        # 翻页，迭代，寻找下一个图片目标
        yield scrapy.Request(next_url[0], callback=self.parse)
        pass

    def saveing(self, response):
        # self.picName = uuid.uuid1()
        self.picName = response.meta['filename']
        item = PicspiderItem()
        item['filename'] = self.picName
        item['picurl'] = response.body

        # yield进pipelines中处理
        yield item
