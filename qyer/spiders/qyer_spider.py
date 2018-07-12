# -*- coding: utf-8 -*-
import scrapy


class QyerSpiderSpider(scrapy.Spider):
    name = 'qyer-spider'
    allowed_domains = ['http://plan.qyer.com']
    start_urls = ['http://http://plan.qyer.com/']

    def parse(self, response):
        pass
