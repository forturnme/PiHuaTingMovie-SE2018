import pandas as pd
from sqlalchemy import create_engine
from server_config import *

print('Fetching movie data......')
engine = create_engine('mysql+pymysql://'+SQL_USERNAME+':'+SQL_PASSWORD+'@'+SQL_ADDRESS+':'+SQL_PORT+'/'+SQL_SCHEMA)

sql = '''select name,genre from cleaned_movie_data;'''

df = pd.read_sql_query(sql,engine)
a = df['genre'].str.split(',', expand=True).stack().reset_index(level=0).set_index('level_0').rename(columns={0:'genre'}).join(df.drop('genre', axis=1))
b = a.drop_duplicates(['genre']).iloc[:,0]
c = b.values

sqla = '''select name,boxing,year,month from boxing_day WHERE year = %d and month = %d;'''

print('Summing up......')
framelist = []
for singleyear in range(2015, 2019):
    for singlemonth in range(1, 13):
        dg = pd.read_sql_query(sqla % (singleyear, singlemonth), engine)
        grp = dg.groupby(['name']).sum().reset_index()
        grp['year'] = singleyear
        grp['month'] = singlemonth
        grp['genre'] = None
        # print(grp)
        for i, row in grp.iterrows():
            genre = df[df['name'] == row['name']]['genre']
            if genre.shape[0] > 0:
                grp.loc[[i], ['genre']] = genre.tolist()[0]
        framelist.append(grp)

boxing_genre = pd.concat(framelist)

print('Updating database......')
boxing_genre.to_sql('boxing_genre',engine,index=False,if_exists='replace')
print('Genred boxing data update Okay!')
