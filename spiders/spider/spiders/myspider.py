# -*- coding: utf-8 -*-
import scrapy
from spider.items import SpiderItem
from scrapy.conf import settings
import pymysql
from server_config import *

sql_find = 'SELECT boxing FROM cleaned_movie_data WHERE name="%s";'
sql_insert = 'INSERT INTO cleaned_movie_data(name,boxing,year,month,day,director,actor,genre)\
    VALUES("%s",%f,%d,%d,%d,"%s","%s","%s");'
sql_update = 'UPDATE cleaned_movie_data SET boxing=%f WHERE name="%s";'
start_url = "http://58921.com"

# default_year = 2015

# 连接数据库
host = SQL_ADDRESS
username = SQL_USERNAME
password = SQL_PASSWORD
db_name = SQL_SCHEMA
portnum = int(SQL_PORT)
def conn_sql():
    connection = pymysql.connect(host=host, port=int(portnum), user=username, password=password, charset='utf8mb4', db=db_name)
    connection.commit()
    cursor = connection.cursor()
    return connection, cursor

class MyspiderSpider(scrapy.Spider):
    def __init__(self):
        self.conn, self.cur = conn_sql()
    name = 'myspider'
    allowed_domains = ['58921.com']
    cookie = settings['COOKIE']  # 带着Cookie向网页发请求
    headers = {
        'Connection': 'keep - alive',  # 保持链接状态
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
    }

    def start_requests(self):
        urls = [
            'http://58921.com/alltime/2015',
            'http://58921.com/alltime/2015?page=1',
            'http://58921.com/alltime/2015?page=2',
            'http://58921.com/alltime/2015?page=3',
            'http://58921.com/alltime/2015?page=4',
            'http://58921.com/alltime/2015?page=5',
            'http://58921.com/alltime/2015?page=6',
            'http://58921.com/alltime/2015?page=7',
            'http://58921.com/alltime/2015?page=8',
            'http://58921.com/alltime/2015?page=9',
            'http://58921.com/alltime/2015?page=10',
            'http://58921.com/alltime/2015?page=11',
            'http://58921.com/alltime/2015?page=12',
            'http://58921.com/alltime/2015?page=13',
            'http://58921.com/alltime/2015?page=14',
            'http://58921.com/alltime/2015?page=15',
            'http://58921.com/alltime/2015?page=16',
            'http://58921.com/alltime/2015?page=17',
            'http://58921.com/alltime/2016',
            'http://58921.com/alltime/2016?page=1',
            'http://58921.com/alltime/2016?page=2',
            'http://58921.com/alltime/2016?page=3',
            'http://58921.com/alltime/2016?page=4',
            'http://58921.com/alltime/2016?page=5',
            'http://58921.com/alltime/2016?page=6',
            'http://58921.com/alltime/2016?page=7',
            'http://58921.com/alltime/2016?page=8',
            'http://58921.com/alltime/2016?page=9',
            'http://58921.com/alltime/2016?page=10',
            'http://58921.com/alltime/2016?page=11',
            'http://58921.com/alltime/2016?page=12',
            'http://58921.com/alltime/2016?page=13',
            'http://58921.com/alltime/2016?page=14',
            'http://58921.com/alltime/2016?page=15',
            'http://58921.com/alltime/2016?page=16',
            'http://58921.com/alltime/2016?page=17',
            'http://58921.com/alltime/2016?page=18',
            'http://58921.com/alltime/2016?page=19',
            'http://58921.com/alltime/2017',
            'http://58921.com/alltime/2017?page=1',
            'http://58921.com/alltime/2017?page=2',
            'http://58921.com/alltime/2017?page=3',
            'http://58921.com/alltime/2017?page=4',
            'http://58921.com/alltime/2017?page=5',
            'http://58921.com/alltime/2017?page=6',
            'http://58921.com/alltime/2017?page=7',
            'http://58921.com/alltime/2017?page=8',
            'http://58921.com/alltime/2017?page=9',
            'http://58921.com/alltime/2017?page=10',
            'http://58921.com/alltime/2017?page=11',
            'http://58921.com/alltime/2017?page=12',
            'http://58921.com/alltime/2017?page=13',
            'http://58921.com/alltime/2017?page=14',
            'http://58921.com/alltime/2017?page=15',
            'http://58921.com/alltime/2017?page=16',
            'http://58921.com/alltime/2017?page=17',
            'http://58921.com/alltime/2017?page=18',
            'http://58921.com/alltime/2017?page=19',
            'http://58921.com/alltime/2018',
            'http://58921.com/alltime/2018?page=1',
            'http://58921.com/alltime/2018?page=2',
            'http://58921.com/alltime/2018?page=3',
            'http://58921.com/alltime/2018?page=4',
            'http://58921.com/alltime/2018?page=5',
            'http://58921.com/alltime/2018?page=6',
            'http://58921.com/alltime/2018?page=7',
            'http://58921.com/alltime/2018?page=8',
            'http://58921.com/alltime/2018?page=9',
            'http://58921.com/alltime/2018?page=10',
            'http://58921.com/alltime/2018?page=11',
            'http://58921.com/alltime/2018?page=12',
            'http://58921.com/alltime/2018?page=13',
            'http://58921.com/alltime/2018?page=14',
            'http://58921.com/alltime/2018?page=15',
            'http://58921.com/alltime/2018?page=16',
            'http://58921.com/alltime/2018?page=17',
            'http://58921.com/alltime/2018?page=18',
            'http://58921.com/alltime/2018?page=19',
            'http://58921.com/alltime/2018?page=20',
            'http://58921.com/alltime/2018?page=21',
            'http://58921.com/alltime/2018?page=22',
            'http://58921.com/alltime/2018?page=23',
            'http://58921.com/alltime/2018?page=24',
        ]
        for url in urls:
            default_year = int(url.split('?')[0].split('/')[-1])
            yield scrapy.Request(url, meta={'default-year':default_year}, callback=self.parse, cookies=self.cookie, headers=self.headers)

    def parse(self, response):
        default_year = response.meta['default-year']
        url_list = response.xpath("//td//a//@href").extract()
        init_url = "http://58921.com"
        c = 0
        for url in url_list:
            c += 1
            if c % 2 == 0:
                continue
            my_item = SpiderItem()
            yield response.follow(init_url + url,  meta={'default-year':default_year}, callback = self.check)
            # # break
        pass

    def check(self, response):
        default_year = response.meta['default-year']
        movie = SpiderItem()
        movie['name'] = response.xpath('normalize-space(//h1[@class="content_title"]/text())').extract_first()
        url = response.xpath('//a[@class="pull-left"]/@href').extract()[0]
        directors = []
        licount = len(response.xpath('//div[@class="media-body"]/ul/li').extract())
        onair = len(response.xpath('//span[@class="label label-success"]').extract())
        if licount > 3: # 有元数据的电影
            if onair == 0:# 下映了的
                if licount == 6:
                    if response.xpath('////div[@class="media-body"]/ul/li[last()-1]/strong/text()').extract()[0] == '制作国家/地区：':
                        uptime = response.xpath('//div[@class="media-body"]/ul/li[3]/text()').extract()[0]
                    else:
                        uptime = response.xpath('//div[@class="media-body"]/ul/li[4]/text()').extract()[0]
                else:
                    uptime = response.xpath('//div[@class="media-body"]/ul/li[4]/text()').extract()[0]
                    movie['actor'] = ','.join(response.xpath('//div[@class="media-body"]/ul/li[3]/a/text()').extract())
                for its in response.xpath('//div[@class="media-body"]/ul/li[2]/a/text()').extract():
                    its = " ".join(its.split('/'))
                    directors.extend(its.split())
                movie['genre'] = ','.join(response.xpath('//div[@class="media-body"]/ul/li[last()]/a/text()').extract())
                if licount > 7:
                    movie['genre'] = ','.join(
                        response.xpath('//div[@class="media-body"]/ul/li[7]/a/text()').extract())
                else:
                    movie['genre'] = ','.join(
                        response.xpath('//div[@class="media-body"]/ul/li[last()]/a/text()').extract())
            else:
                uptime = response.xpath('//div[@class="media-body"]/ul/li[6]/text()').extract()[0]
                for its in response.xpath('//div[@class="media-body"]/ul/li[4]/a/text()').extract():
                    its = " ".join(its.split('/'))
                    directors.extend(its.split())
                movie['actor'] = ','.join(response.xpath('//div[@class="media-body"]/ul/li[5]/a/text()').extract())
                if licount > 9:
                    movie['genre'] = ','.join(response.xpath('//div[@class="media-body"]/ul/li[9]/a/text()').extract())
                else:
                    movie['genre'] = ','.join(response.xpath('//div[@class="media-body"]/ul/li[last()]/a/text()').extract())
            movie['director'] = ','.join(directors)
            movie['year'] = int(uptime.split('-')[0])
            movie['month'] = int(uptime.split('-')[1])
            movie['day'] = int(uptime.split('-')[2])
        else:
            movie['year'] = default_year
            print('[insuf-movie found] ',movie['name'],movie['year'])
        movie = scrapy.Request(start_url + url + '/boxoffice', meta = {'movie': movie}, callback = self.get_boxing)
        yield movie
        pass

    def get_boxing(self, response):
        movie = response.meta['movie']
        boxtext = response.xpath('//h3/text()').extract()[0]
        boxtext = boxtext.split('(')[-1].split(')')[0].split()[1]
        boxing = float(boxtext[:-1])
        if boxtext[-1]=='亿':
            boxing = round(boxing*10000,2)
        elif boxtext[-1]=='万':
            boxing = round(boxing, 2)
        else:
            boxing = round(float(boxtext)/10000,2)
        movie['boxing'] = boxing
        # 更新sql
        if self.cur.execute(sql_find % (movie['name'])) != 0:
            result = self.cur.fetchone()
            if result[0] - boxing >= 1 and movie['genre'] != None:
                try:
                    self.cur.execute(sql_update%(boxing,movie['name']))
                    self.conn.commit()
                    print('Updated 1 item')
                except:
                    print('<<<<db error')
                    self.conn.rollback()
                    try:
                        self.cur.execute(sql_update % (boxing, movie['name']))
                        self.conn.commit()
                    except:
                        print('<<<<db error *2')
                        self.conn.rollback()
        else:
            try:
                self.cur.execute(sql_insert%(movie['name'],boxing,movie['year'],movie['month'],movie['day'],
                                        movie['director'],movie['actor'],movie['genre']))
                self.conn.commit()
                print('Updated 1 item')
            except:
                print('<<<<db error')
                self.conn.rollback()
                try:
                    self.cur.execute(sql_insert % (movie['name'], boxing, movie['year'], movie['month'], movie['day'],
                                                   movie['director'], movie['actor'], movie['genre']))
                    self.conn.commit()
                except:
                    print('<<<<db error *2')
                    self.conn.rollback()
        yield movie
        pass

if __name__ == '__main__':
    conn_sql()