# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface


# import uuid

import scrapy
from itemadapter import ItemAdapter


class PicspiderPipeline:
    picName = ""
    def process_item(self, item, spider):
        print('xxxxxxxx-----------xxxxxxxxxxxxx----进入PicspiderPipeline')
        adapter = ItemAdapter(item)
        print('xxxxxxxx------xxxxxxxxxxxxx----链接为：  '+adapter['picurl'], adapter['filename'])
        # yield scrapy.Request(adapter['picurl'], adapter['filename'], callback=self.saveing)
        print('xxxxxxxx-----------xxxxxxxxxxxxx----完成PicspiderPipeline')
        return item

    def saveing(self, response):
        # filename = '00.jpg'
        # with open(filename, 'wb') as fp:
        #     fp.write(response.body)
        #     print('xxxxxxxx-----------xxxxxxxxxxxxx----完成saveing')

        # self.picName = uuid.uuid1()
        self.picName = response.item['filename']
        with open("C:/chenjimiao/project/python/aiTeacherPlan/picspider/images2/" + '{}.jpg'.format(self.picName),
                  'wb') as f:
            f.write(response.body)
            print('xxxxxxxx-----------xxxxxxxxxxxxx----完成saveing')
