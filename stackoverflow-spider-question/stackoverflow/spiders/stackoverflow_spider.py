#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

import scrapy
from stackoverflow.spiders.items import StackoverflowItem
from scrapy.selector import Selector

formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('monitor')
logger.setLevel(logging.INFO)

fh = logging.FileHandler('monitor.log')
fh.setLevel(logging.INFO)

fh.setFormatter(formatter)
logger.addHandler(fh)


class StackoverflowSpider(scrapy.Spider):

    name = "stackoverflow"

    def __init__(self):
        self.count = 1

    def start_requests(self):
        _url = 'https://stackoverflow.com/questions?page={page}&sort=newest&pagesize=50'
        urls = [_url.format(page=page) for page in range(74244,90000)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for index in range(1, 51):
            self.count += 1
            if self.count % 100 == 0:
                logger.info(self.count)

            sel = response.xpath('//*[@id="questions"]/div[{index}]'.format(index=index))
            
            item = StackoverflowItem()
#            item['votes'] = sel.xpath('div[1]/div[2]/div[1]/div[1]/span/strong/text()').extract()
#            item['answers'] = sel.xpath('div[1]/div[2]/div[2]/strong/text()').extract()
#            item['answers'] = sel.xpath('div[1]/div[2]/div[2]/strong/text()').extract()
            item['answersNumber'] = sel.xpath('.//div[contains(@class,"status")]/strong/text()').extract()
            item['views'] = sel.xpath('.//div[contains(@class,"views")]/text()').extract()[0][6:-7]

            item['votes'] = sel.xpath(
                    './/span[contains(@class,"vote-count-post")]/strong/text()').extract()[0]
##            
#            item['views'] = "".join(sel.xpath('div[1]/div[3]/@title').extract()).split()[0].replace(",", "")
            item['questions'] = sel.xpath('div[2]/h3/a/text()').extract()
#            question_id = "".join(sel.xpath('div[2]/h3/a/@href').extract()).split("/")[2]
#            item['links'] = 'https://stackoverflow.com/questions/'+ question_id
            item['links'] = 'https://stackoverflow.com' + sel.xpath(
                    'div[@class="summary"]/h3/a/@href').extract()[0]
            item['tags'] = sel.xpath('div[2]/div[2]/a/text()').extract()
            item['questionTime'] = sel.xpath('.//span[contains(@class,"relativetime")]/@title').extract()
            yield item
            
#    def parse(self, response):
#        sel = Selector(response)
#        sites = sel.xpath('//div[@id="questions"]/div[@class="question-summary"]')
#        items = []
#        print(len(sites))
#
#        for site in sites:
#            item = StackoverflowItem()
#            #tt = site.xpath('div[1]/div[3]/text()').extract()
#            #print tt[0].split(' ')
##            item['views'] = site.xpath('div[1]/div[3]/text()').extract()[0].split(' ')[4]
#            item['votes'] = site.xpath('div[1]/div[2]/div[1]/div/span/strong/text()').extract()
##            item['answers'] = site.xpath('div[1]/div[2]/div[2]/strong/text()').extract()
#            item['questions'] = site.xpath('div[2]/h3/a/text()').extract()
#            item['answers'] = site.xpath('.//div[contains(@class,"status")]/strong/text()').re_first(r'\d')
##            key_list = [ksite.xpath('text()').extract()[0].encode('utf-8') for ksite in site.xpath('div[2]/div[2]/a')]
##            item['key'] = " ".join(str(ele) for ele in key_list)
#
##            item['author'] = site.xpath('div[2]/div[3]/div/div[3]/a/text()').extract()
#
##            item['time'] = site.xpath('div[2]/div[3]/div/div[1]/span/text()').extract()
#
#            items.append(item)
#
#        return items
