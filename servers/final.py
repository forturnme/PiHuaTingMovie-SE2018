import pymysql
import pandas as pd

# from sqlalchemy import create_engine

def boxing_money_year(engine):
    # engine = create_engine('mysql+pymysql://root:hitse2018@139.199.75.35:3306/se')
    sql = '''select boxing,year from boxing_month WHERE year in (2015,2016,2017,2018);'''
    df = pd.read_sql_query(sql, engine)
    grouped = df.groupby('year')
    result = grouped.sum()
    # a = df.groupby('year')['boxing'].sum().tolist()
    # print df['year'].value_counts()
    # df.loc['Row_sum'] = df.apply(lambda x: x.sum())
    # a = df['boxing']['Row_sum']
    list2 = []
    a = result['boxing'].values
    for i in a:
        list2.append(round(i, 2))
    return pd.Index(['2015', '2016', '2017', '2018']), list2


# a = boxing_money_year(2017)


def top_20(engine, x):
    # db  = pymysql.connect(host='139.199.75.35',user='root',passwd='hitse2018',port=3306,charset='utf8')
    # cur = db.cursor()
    # cur.execute('use se')
    sql = 'SELECT name,boxing FROM cleaned_movie_data WHERE year = ' + str(x) + ' ' + 'ORDER BY boxing DESC LIMIT 0,20'
    # cur.execute(selectsql.encode('utf-8'))

    # data = cur.fetchall()
    data = pd.read_sql_query(sql, engine)
    '''for item in data:
        print(item)'''

    # db.close()
    # keys = []
    # values = []
    # for i in range(len(data)):
    #    keys.append(data[i][0])
    #    values.append(data[i][1])
    # return pd.Index(keys), values
    return data['name'], data['boxing'].tolist()


# a = top_20(2017)


def actor_max(engine, x):
    # engine = create_engine('mysql+pymysql://root:hitse2018@139.199.75.35:3306/se')
    sql = '''select actor from cleaned_movie_data WHERE year = ''' + str(x) + ';'
    df = pd.read_sql_query(sql, engine)
    a = df['actor'].str.split(',', expand=True).stack().reset_index(level=0).set_index('level_0').rename(
        columns={0: 'actor'}).join(df.drop('actor', axis=1))
    # print(a['actor'].value_counts().head(10))
    # b = list(a['actor'].value_counts().head(10).items())
    # for item in b:
    # print(item[0],item[1])
    b = a['actor'].value_counts().head(10).keys()
    c = a['actor'].value_counts().head(10).values.tolist()
    return b, c


# actor_max(2017)


def movie_rate(engine, x, y, z):
    # engine = create_engine('mysql+pymysql://root:hitse2018@139.199.75.35:3306/se')
    if z == 'genre-year':
        sqlb = '''select boxing,genre from boxing_genre WHERE year = ''' + str(x) + ';'
        dh = pd.read_sql_query(sqlb, engine)
        h = dh['genre'].str.split(',', expand=True).stack().reset_index(level=0).set_index('level_0').rename(
            columns={0: 'genre'}).join(dh.drop('genre', axis=1))
        grouped = h.groupby('genre')

    if z == 'genre-quarter':
        # sqlc = '''select boxing,genre from boxing_genre WHERE year = 2017 and month in (1*3+1,2*3);'''
        sqlc = '''select boxing,genre from boxing_genre WHERE year = ''' + str(x) + ' ' + 'and month in ' + '(' + str(
            (y - 1) * 3 + 1) + ',' + str((y - 1) * 3 + 2) + ',' + str(y * 3) + ')' + ';'
        dj = pd.read_sql_query(sqlc, engine)
        j = dj['genre'].str.split(',', expand=True).stack().reset_index(level=0).set_index('level_0').rename(
            columns={0: 'genre'}).join(dj.drop('genre', axis=1))
        grouped = j.groupby('genre')

    if z == 'genre-month':
        # sqla = '''select boxing,genre from boxing_genre WHERE year = 2017 and month = 2;'''
        sqla = '''select boxing,genre from boxing_genre WHERE year = ''' + str(x) + ' ' + 'and month = ' + str(y) + ';'
        dg = pd.read_sql_query(sqla, engine)
        g = dg['genre'].str.split(',', expand=True).stack().reset_index(level=0).set_index('level_0').rename(
            columns={0: 'genre'}).join(dg.drop('genre', axis=1))
        grouped = g.groupby('genre')

    result = grouped.sum().reset_index()
    # del result['year']
    # del result['month']
    result.dropna(inplace=True)
    # print(result)
    ans2 = result['boxing'].values
    ans1 = result['genre']
    list2 = []
    for item in ans2:
        list2.append(round(item, 2))

    return pd.Index(ans1), list2


# a = movie_rate(x = 2016,y = 2,z = 'genre-quarter')
# print(a[0])
# print(a[1])


def boxing_money_month(engine, x):
    # engine = create_engine('mysql+pymysql://root:hitse2018@139.199.75.35:3306/se')
    sql = '''select boxing,year,month from boxing_month WHERE year =''' + str(x) + ';'
    df = pd.read_sql_query(sql, engine)
    grouped = df.groupby('month')
    result = grouped.sum()
    # del result['year']
    ans1 = result['boxing'].values
    ans2 = result['boxing'].keys()
    list2 = []
    for item in ans1:
        list2.append(round(item, 2))
    return ans2, list2

# a = boxing_money_month(2017)
# print(a[0])
# print(a[1])

# engine = create_engine('mysql+pymysql://root:hitse2018@139.199.75.35:3306/se')
# print(movie_rate(engine,2017,2,'genre-month'))