import pymysql
import time


class ItemCounter(object):


    def __init__(self):
        self.database = pymysql.connect(host='localhost',
                                        port=3306,
                                        user='chunpeng',
                                        passwd='0202',
                                        db='job_info',
                                        charset='utf8')
        self.cursor = self.database.cursor()
        self.table = 'jobs'

    def show_item_count(self):
        sql_string = 'SELECT COUNT(job_id) FROM jobs;'
        self.cursor.execute(sql_string)
        result=self.cursor.fetchall()  #((0,),)
        for i in result:
            print(i[0],"items in database")

if __name__=="__main__":

    while True:
        ic = ItemCounter()
        ic.show_item_count()
        time.sleep(5)
