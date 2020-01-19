# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AssetsSpiderItem(scrapy.Item):
    pass


class ChampionSpiderItem(scrapy.Item):
    # en_title = scrapy.Field()
    # en_name = scrapy.Field()
    # en_full_name = scrapy.Field()
    cn_title = scrapy.Field()
    cn_name = scrapy.Field()
    cn_full_name = scrapy.Field()
    list_pic_url = scrapy.Field()
    detail_pic_url = scrapy.Field()
    banner_pic_url = scrapy.Field()


class RecordSpiderItem(scrapy.Item):
    rowJson = scrapy.Field()


class ItemItem(scrapy.Item):
    name = scrapy.Field()
    imgUrl = scrapy.Field()
