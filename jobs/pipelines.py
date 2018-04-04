# -*- coding: utf-8 -*-
import pymysql
import datetime

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class JobsPipeline(object):
    def open_spider(self, spider):
        self.database = pymysql.connect(host='localhost',
                                  port=3306,
                                  user='xxxxxx',
                                  passwd='xxxxxx',
                                  db='job_info',
                                  charset='utf8')
        self.cursor = self.database.cursor()
        self.table = 'jobs'



    def process_item(self, item, spider):

        sql_string = 'INSERT INTO {} (job_title, company, job_href, location, salary, post_date, update_datetime) \
                VALUES("{}","{}","{}","{}","{}","{}",str_to_date("{}","%Y-%m-%d %H:%i:%s"));' \
            .format(self.table, item['job_title'], item['company'], item['job_href'],
                    item['location'], item['salary'], item['post_date'],
                    datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print(sql_string)
        # print('data to be imported to MySQL')
        # if not self.data_already_exists(item['date'], item['product']):
        try:
            self.cursor.execute(sql_string)
            self.database.commit()
            # print('import successful')
        except:
            print('error')
            self.database.rollback()
        # else:
        #     print('data already exists')
        return item
