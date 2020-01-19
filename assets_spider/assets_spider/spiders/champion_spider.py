# -*- coding: utf-8 -*-
import scrapy
import json
from assets_spider.items import ChampionSpiderItem


class ChampionSpiderSpider(scrapy.Spider):
    name = 'champion_spider'
    allowed_domains = ['apps.game.qq.com']
    pageIndex = 1
    start_urls = [
        "http://apps.game.qq.com/daoju/go/zmgoods/list?cat=16&page=1&plat=android&version=9921"]

    detail_pic_url_prefix = 'http://ossweb-img.qq.com/images/daoju/zm/detail'
    banner_pic_url_prefix = 'http://ossweb-img.qq.com/images/daoju/zm/banner'

    def parse(self, response):
        championRowData = json.loads(response.text)
        for championData in championRowData['data']['goods']:
            champion = ChampionSpiderItem()
            champion['cn_title'] = championData['sGoodsTitle']
            champion['cn_name'] = championData['sGoodsRName']
            champion['cn_full_name'] = championData['sGoodsName']

            original_pic_url = championData['sGoodsPic'].split('?')[0]
            champion['list_pic_url'] = original_pic_url
            champion['detail_pic_url'] = self.detail_pic_url_prefix + original_pic_url[original_pic_url.rfind("/"):]
            champion['banner_pic_url'] = self.banner_pic_url_prefix + original_pic_url[original_pic_url.rfind("/"):]
            yield champion  # throw into pipeline

        # for now, the total number of LOL hero in universe is 147    ===> 2020-01-16
        if self.pageIndex <= 7:
            self.pageIndex += 1
            next_link = "http://apps.game.qq.com/daoju/go/zmgoods/list?cat=16&page=%d&plat=android&version=9921" % (
                self.pageIndex)
            print("going to collect the next_link -> ", next_link)
            yield scrapy.Request(url=next_link, callback=self.parse)
