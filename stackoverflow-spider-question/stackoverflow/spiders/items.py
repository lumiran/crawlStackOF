#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy


class StackoverflowItem(scrapy.Item):

    links = scrapy.Field()
    views = scrapy.Field()
    votes = scrapy.Field()
    answersNumber = scrapy.Field()
    tags = scrapy.Field()
    questions = scrapy.Field()
    questionTime = scrapy.Field()