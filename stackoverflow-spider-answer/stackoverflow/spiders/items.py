#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy


class StackoverflowItem(scrapy.Item):

    links = scrapy.Field()
    views = scrapy.Field()
    votes = scrapy.Field()
    answersID = scrapy.Field()
    contents = scrapy.Field()
    answerTime = scrapy.Field()
    comments = scrapy.Field()
    questionID = scrapy.Field()
    answerIndex = scrapy.Field()
    
