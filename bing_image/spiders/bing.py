# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urlencode
from ..items import BingImageItem


class BingSpider(scrapy.Spider):
    name = 'bing'
    allowed_domains = ['cn.bing.com']

    def start_requests(self):
        base_url = 'https://cn.bing.com/images/async?'

        for i in range(1, self.settings.get('MAX_COUNT') + 1):
            params = {
                'q': self.settings.get('NAME'),
                'first': 0,
                'count': i,
                'cw': 1129,
                'ch': 746,
                'scenario': 'ImageBasicHover',
                'datsrc': 'N_I',
                'layout': 'ColumnBased',
                'mmasync': 1,
                'IG': '3EA0C21D86C74BA88C00C43273A6280E',
                'SFX': 2,
                'iid': 'images'
            }
            url = base_url + urlencode(params)
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        item = BingImageItem()
        photos_url = response.xpath('//div[@class="img_cont hoff"]/img[@class="mimg"]/@src').extract()
        for photo_url in photos_url:
            print(photo_url)
            item['url'] = photo_url
            yield item
