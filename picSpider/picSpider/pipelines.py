# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface


# import uuid

import scrapy
from itemadapter import ItemAdapter


class PicspiderPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        picName = adapter['filename']
        picFile = adapter['picurl']
        with open("C:/chenjimiao/project/python/aiTeacherPlan/images4/" + '{}.jpg'.format(picName),
                  'wb') as f:
            f.write(picFile)
        print('xxxxxxxx-----------xxxxxxxxxxxxx----完成PicspiderPipeline')
        return item

    # def saveing(self, response):
    #     # filename = '00.jpg'
    #     # with open(filename, 'wb') as fp:
    #     #     fp.write(response.body)
    #     #     print('xxxxxxxx-----------xxxxxxxxxxxxx----完成saveing')
    #
    #     # self.picName = uuid.uuid1()
    #     self.picName = response.item['filename']
    #     with open("C:/chenjimiao/project/python/aiTeacherPlan/picspider/images2/" + '{}.jpg'.format(self.picName),
    #               'wb') as f:
    #         f.write(response.body)
    #         print('xxxxxxxx-----------xxxxxxxxxxxxx----完成saveing')
