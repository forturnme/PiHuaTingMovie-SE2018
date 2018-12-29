from flask import Flask, request, make_response
from server_config import *
import random
import hashlib
import time
import pymysql

# session表
session = {}
session_time = {}
MAX_TIME = 10000
# 维护session表
def check_session_time():
    for key, value in session_time.items():
        now = int(time.time())
        if (now - value) > MAX_TIME:
            session_time.pop(key)
            session.pop(key)
# 返回一串随机字符串，生成session
def random_str():
    seed = 'qwertyuiopasdfghjklzxcvbnm1234567890'
    s = ''
    for i in range(10):
        index = random.randint(0, len(seed)-1)
        s += seed[index]
    return s

# 连接数据库
host = SQL_ADDRESS
username = SQL_USERNAME
password = SQL_PASSWORD
db_name = SQL_SCHEMA
sqlport = int(SQL_PORT)
def conn_sql(connection, cursor):
    _status=False
    tries=0
    try:
        connection.ping()
    except:
        while _status==False and tries<10:
            try:
                connection = pymysql.connect(host=host, user=username, port=sqlport, password=password, charset='utf8mb4', db=db_name)
                connection.commit()
                _status=True
            except:
                tries+=1
        cursor = connection.cursor()
    return connection, cursor

connection = pymysql.connect(host=host, user=username, port=sqlport, password=password, charset='utf8mb4', db=db_name)
cursor = connection.cursor()

# 计算md5
def getEncryption(password,vcode):
    return hashlib.md5((str(password) + str(vcode)).encode(encoding='UTF-8')).hexdigest()

app = Flask(__name__)


def User(request):
    username = request.form.get('username')
    if username is None:
        username = ''
    password = request.form.get('password')
    if password is None:
        password = ''
    return username, password
#注册
@app.route('/register', methods=['POST'])
def register():
    global connection, cursor
    connection, cursor = conn_sql(connection, cursor)
    username, password =User(request)
    # 检测是此用户用户名是否用过
    if len(password) == 0:
        response = make_response('stats=no_password', 404)
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'POST'
        response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
        # connection.close()
        return response
    sql = "SELECT * FROM PASSWORDS WHERE username='{}';".format(username)
    if cursor.execute(sql) == 0:
        insert_table_sql = """\
            INSERT INTO PASSWORDS(username,password,vcode)
             VALUES('{}','{}',{})
            """
        cursor.execute(insert_table_sql.format(username, password, -1))
        connection.commit()
        response = make_response('stats=registered_OK', 210)
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'POST'
        response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
        # connection.close()
        return response
    else:
        response = make_response('stats=username_used', 404)
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'POST'
        response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
        # connection.close()
        return response

# 返回验证码
@app.route('/vcode', methods=['POST'])
def verification_Code():
    global connection, cursor
    connection, cursor = conn_sql(connection, cursor)
    username, password = User(request)
    sql = "SELECT * FROM PASSWORDS WHERE username='{}';".format(username)
    if cursor.execute(sql) == 0:
        response = make_response('stats=username_wrong', 404)
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'POST'
        response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
        # connection.close()
        return response
    else:
        vcode = random.randint(0, 9999)
        sql = "UPDATE PASSWORDS SET vcode={} WHERE username='{}';".format(str(vcode), username)
        try:
            cursor.execute(sql)  # 执行sql语句
            connection.commit()  # 提交到数据库执行
        except:
            connection.rollback()
        response = make_response('vcode=' + str(vcode), 210)
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'POST'
        response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
        # connection.close()
        return response

# 登录
@app.route('/login', methods=['POST'])
def route_login():
    global connection, cursor
    connection, cursor = conn_sql(connection, cursor)
    username, password = User(request)
    # 查找是否由此用户并验证md5
    sql = "SELECT * FROM PASSWORDS WHERE username='{}';".format(username)
    if cursor.execute(sql) == 0:
        response = make_response('stats=username_wrong', 404)
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'POST'
        response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
        # connection.close()
        return response
    else:
        results = cursor.fetchone()
        # vcode用完设为-1
        sql = "UPDATE PASSWORDS SET vcode={} WHERE username='{}';".format(str(-1), username)
        try:
            cursor.execute(sql)  # 执行sql语句
            connection.commit()  # 提交到数据库执行
        except:
            connection.rollback()
        # print(results)
        if results[3] == -1:
            response = make_response('stats=login_novcode', 404)
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Methods'] = 'POST'
            response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
            # connection.close()
            return response
        md_password = getEncryption(results[2], results[3])
        # print('[md_password] ', md_password)
        if md_password == password:
            response = make_response('stats=login_OK', 210)
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Methods'] = 'POST'
            response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
            # connection.close()
            return response
        else:
            response = make_response('stats=password_wrong', 404)
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Methods'] = 'POST'
            response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
            # connection.close()
            return response


@app.route('/jump', methods=['POST'])
def jump():
    global connection, cursor
    connection, cursor = conn_sql(connection, cursor)
    username, password = User(request)
    #查找是否由此用户并验证md5
    sql = "SELECT * FROM PASSWORDS WHERE username='{}';".format(username)
    if cursor.execute(sql) == 0:
        response = make_response('stats=username_wrong', 404)
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'POST'
        response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
        # connection.close()
        return response
    else:
        # results = connection.cursor().fetchall()
        results = cursor.fetchone()
        #vcode用完设为-1
        sql = "UPDATE PASSWORDS SET vcode={} WHERE username='{}';".format(str(-1), username)
        try:
            cursor.execute(sql)  # 执行sql语句
            connection.commit()  # 提交到数据库执行
        except:
            connection.rollback()
        # print(results)
        if results[3] == -1:
            response = make_response('stats=login_novcode', 404)
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Methods'] = 'POST'
            response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
            # connection.close()
            return response
        md_password = getEncryption(results[2], results[3])
        if md_password == password:
            session_id = random_str()
            check_session_time()
            session[session_id] = username
            session_time[session_id] = int(time.time())
            response_body = 'http://139.199.75.35:3000/report.html?token={}\r\n'.format(session_id)
            response = make_response(response_body, 210)
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Methods'] = 'POST'
            response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
            # connection.close()
            return response
        else:
            response = make_response('stats=password_wrong', 404)
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Methods'] = 'POST'
            response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
            # connection.close()
            return response

@app.route('/report.html', methods=['GET'])
def report():
    # path = request.path
    # print(path)
    # if len(path.split('?')) < 2:
    #     token = ''
    # else:
    #     token = path.split('?', 1)[1]
    token = request.args.get('token')
    # print(token)
    if session.__contains__(token):
        s_time = session_time.get(token)
        if int(time.time()) - s_time > MAX_TIME:
            response = make_response('stats=time_out', 210)
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access - Control - Allow - Credentials'] = 'true'
            response.headers['Access-Control-Allow-Methods'] = 'POST'
            response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
            session.pop(token)
            return response
        else:
            with open('report.html', 'r', encoding='utf-8') as f:
                response_body = f.read()
            response = make_response(response_body, 210)
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access - Control - Allow - Credentials'] = 'true'
            response.headers['Access-Control-Allow-Methods'] = 'POST'
            response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
            session.pop(token)
            return response
    else:
        response = make_response('stats=token_wrong', 404)
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access - Control - Allow - Credentials'] = 'true'
        response.headers['Access-Control-Allow-Methods'] = 'POST'
        response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
        return response

app.run(host='0.0.0.0',debug=False,port=3000)

