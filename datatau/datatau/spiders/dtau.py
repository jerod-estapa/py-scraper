# -*- coding: utf-8 -*-

from scrapy import Spider
from scrapy.selector import Selector

from datatau.items import DatatauItem


class DtauSpider(Spider):
    name = "dtau"
    allowed_domains = ["www.datatau.com"]
    start_urls = (
        'http://www.datatau.com/',
    )

    def parse(self, response):

        titles = Selector(response).xpath('//td[@class="title"]/a[@href]')

        for title in titles:
            item = DatatauItem()
            item['title'] = title.xpath("text()").extract()
            item['url'] = title.xpath("@href").extract()
            yield item

