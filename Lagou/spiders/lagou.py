# -*- coding: utf-8 -*-
import scrapy


class LagouSpider(scrapy.Spider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    start_urls = ['https://www.lagou.com/jobs/']
    city = "武汉"
    post_data = ""

    def parse(self, response):
        url = "https://www.lagou.com/jobs/positionAjax.json?city={0}&needAddtionalResult=false".format(self.city)

