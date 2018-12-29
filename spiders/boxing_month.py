import pandas as pd
from sqlalchemy import create_engine
from server_config import *

print('Fetching data......')

engine = create_engine('mysql+pymysql://'+SQL_USERNAME+':'+SQL_PASSWORD+'@'+SQL_ADDRESS+':'+SQL_PORT+'/'+SQL_SCHEMA)
sqla = '''select boxing,year,month from boxing_day WHERE year = 2015;'''
dg = pd.read_sql_query(sqla,engine)
grouped = dg.groupby('month')
result0 = grouped.sum()
result0['year']=2015

sqlb = '''select boxing,year,month from boxing_day WHERE year = 2016;'''
df = pd.read_sql_query(sqlb,engine)
grouped1 = df.groupby('month')
result1 = grouped1.sum()
result1['year']=2016

sqlc = '''select boxing,year,month from boxing_day WHERE year = 2017;'''
dh = pd.read_sql_query(sqlc,engine)
grouped2 = dh.groupby('month')
result2 = grouped2.sum()
result2['year']=2017

sqld = '''select boxing,year,month from boxing_day WHERE year = 2018;'''
dl = pd.read_sql_query(sqld,engine)
grouped3 = dl.groupby('month')
result3 = grouped3.sum()
result3['year']=2018

print('Caculating......')
result = pd.concat([result0,result1,result2,result3])
result['month']=[1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11,12]

print('Updating database......')
result.to_sql('boxing_month',engine,index=False,if_exists='replace')
print('Monthly database update Okay!')
