import scrapy
import time

from jobs.items import JobsItem



class JobspiderSpider(scrapy.Spider):
    name='jobspider'
    allowed_domains = ['search.51job.com']

    start_urls = [
        'http://search.51job.com/list/000000,000000,0000,19,9,99,%2B,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']


    def parse(self, response):

        next_page_url = response.xpath('//li[@class="bk"][2]/a/@href')
        job_list = response.xpath('//*[@id="resultList"]/div[@class="el"]')
        # print(job_list.extract())
        for each_job in job_list:
            job_info = JobsItem()
            job_info['job_title'] = each_job.xpath('.//p[contains(@class,"t1")]/span/a/text()')
            job_info['company'] = each_job.xpath('.//span[contains(@class,"t2")]/a/text()')
            job_info['job_href'] = each_job.xpath('.//span[contains(@class,"t2")]/a/@href')
            job_info['location'] = each_job.xpath('.//span[contains(@class,"t3")]/text()')
            job_info['salary'] = each_job.xpath('.//span[contains(@class,"t4")]/text()')
            job_info['post_date'] = each_job.xpath('.//span[contains(@class,"t5")]/text()') # mm-dd

            for k, v in job_info.items():
                if v:
                    job_info[k] = v.extract_first().strip()
                else:
                    job_info[k] = 'unknown'
            # print(job_info)
            yield job_info
        if next_page_url is not None:
            abs_url = next_page_url.extract_first().strip()
            print('*'*30)
            # time.sleep(1)
            yield response.follow(abs_url, callback=self.parse)
        # return