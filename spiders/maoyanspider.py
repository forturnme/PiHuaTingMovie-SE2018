# coding=utf-8
from bs4 import BeautifulSoup as bs
from urllib.error import HTTPError
from urllib.request import urlopen
from sqlalchemy import create_engine
import json
import pandas as pd
from server_config import *

print('Starting to crawl......')

# 打开网页，获取源码
def open_page(url):
    try:
        netword=urlopen(url)
    except HTTPError as hp:
        print(hp)
    else:
    # 采用BeautifulSoup来解析，且指定解析器
        html=bs(netword,'lxml')
        return html

# 获取网页数据 
def get_page(url):
    # 电影名称，上映天数，电影总票房，票房占比，排片场次，排片占比，场均人次，上座率 
    movieName, boxInfo = [], []
    html=open_page(url)
    # print(html)
    p=html.find('p')
    text=p.get_text()
    # 将数据转换为python能够处理的格式
    jsonObj=json.loads(text)
    # 获取字典里面特定的键对应的键值
    data=jsonObj.get('data')
    # 想要的数据就在字典的键"list"对应的值
    lists=data.get('list')
    for list in lists:
        # 获取字典里面特定的键对应的键值,并存储到列表中去
        movieName.append(list.get('movieName'))
        boxInfo.append(list.get('boxInfo'))
    return movieName, boxInfo

a = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
movieName, boxInfos, year, month, day = [], [], [], [], []

for i in range(2015, 2019):
    for j in range(1, 13):
        if i == 2016 & j == 2:
            n = 29
        else:
            n = a[j]
        for k in range(1, n):
            tmpMonth = str(j)
            tmpDay = str(k)
            tmpYear = str(i)
            if j < 10:
                tmpMonth = '0' + tmpMonth
            if k < 10:
                tmpDay = '0' + tmpDay
            url = 'https://box.maoyan.com/promovie/api/box/second.json?beginDate=' + tmpYear + tmpMonth + tmpDay
            # print(url)
            tmpMovieName, tmpboxInfos = get_page(url)
            # print(tmpMovieName)
            for x in tmpMovieName:
                movieName.append(x)
                year.append(tmpYear)
                month.append(tmpMonth)
                day.append(tmpDay)
            for x in tmpboxInfos:
                boxInfos.append(float(x))
print('Summing up result......')
d=pd.DataFrame({'name': movieName, 'boxing': boxInfos, 'year': year, 'month': month, 'day': day})#数据有三列，列名分别为one,two,three
# d.to_csv("test.csv", index = False, sep=',')
print('Started to update database......')
engine = create_engine('mysql+pymysql://'+SQL_USERNAME+':'+SQL_PASSWORD+'@'+SQL_ADDRESS+':'+SQL_PORT+'/'+SQL_SCHEMA)
d.to_sql("boxing_day",engine,if_exists='replace', index=False)
print('Daily boxing data crawled Okay!')
