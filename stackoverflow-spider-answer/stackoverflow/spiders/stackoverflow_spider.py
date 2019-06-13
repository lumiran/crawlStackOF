#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

import scrapy
from stackoverflow.spiders.items import StackoverflowItem
from scrapy.selector import Selector
import csv
import pandas as pd
import numpy as np

formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('monitor')
logger.setLevel(logging.INFO)

fh = logging.FileHandler('monitor.log')
fh.setLevel(logging.INFO)

fh.setFormatter(formatter)
logger.addHandler(fh)


'''
Read the Urls of Questions
'''
dir = 'data'
filename = ['1.csv','2.csv','3.csv','4.csv','5.csv']

all_url = []
numanswer = []
count30 = 0
count0 = 0
for j in range(5):
    file = dir+'/'+filename[j]
    csvfile = csv.reader(open(file,encoding = 'utf-8'))
    for i,stu in enumerate(csvfile):
        if i == 0:
            continue
        numanswer.append(stu[1])
        if int(stu[1])>=30:
            count30+=1
        if int(stu[1])==0:
            count0+=1
        else:    
            all_url.append(stu[2])
            
plt.hist(num,bins = 50)
plt.xlabel('answerNum')
plt.ylabel('questionNum')
for i in range(len(all_url)): 
    
    if '55759858' in all_url[i]:
        print(i)
        print(all_url[i])

class StackoverflowSpider(scrapy.Spider):

    name = "test"

    def __init__(self):
        self.count = 1

    def start_requests(self):
        urls = all_url[141705:-1]
#        urls = ['https://stackoverflow.com/questions/750486/javascript-closure-inside-loops-simple-practical-example?page=1&tab=votes#tab-top']
        for url in urls:
            
            yield scrapy.Request(url=url, callback=self.parse)
#        ?page=1&tab=votes#tab-top
#        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        answerNum = response.xpath('//span[@itemprop="answerCount"]/text()').extract()[0]
        quanestionID = response.xpath('//div[@class="question"]/@data-questionid').extract()
        link = response.xpath('//div[@id="question-header"]/h1/a/@href').extract()
#        print('answerNum',answerNum)
#        print(link)
        if int(answerNum) == 0:
            item = StackoverflowItem()
            item['questionID'] = quanestionID
            item['links'] ='https://stackoverflow.com'+ link[0]
            item['answersID'] = 'None'
            item['contents'] = 'None'
            item['answerTime'] = 'None'
            item['votes'] = 'None'
            item['answerIndex'] = 'None'
            yield item
        else:
            
            for index in range(min(30,int(answerNum))):
                self.count += 1
                if self.count % 100 == 0:
                    logger.info(self.count)
    
    
                sel = response.xpath('//*[contains(@id,"answer-")]')[index]
                
                item = StackoverflowItem()
                item['links'] ='https://stackoverflow.com'+ link[0]
                item['questionID'] = quanestionID
                item['answersID'] = sel.xpath('@data-answerid').extract()
                item['answerIndex'] = index+1
                item['contents'] = sel.xpath('div/div[2]/div/p').extract()
                item['answerTime'] = sel.xpath('div/div[2]/div[2]/time/@datetime').extract()
                item['votes'] = sel.xpath('div/div[1]/div/div/@data-value').extract()
   
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
