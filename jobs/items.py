# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_title = scrapy.Field()
    company = scrapy.Field()
    job_href = scrapy.Field()
    location = scrapy.Field()
    salary = scrapy.Field()
    post_date = scrapy.Field()

    pass
