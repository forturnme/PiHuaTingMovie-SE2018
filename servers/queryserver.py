from flask import Flask,request,make_response,jsonify
from final import *
from sqlalchemy import create_engine
from server_config import *

engine = create_engine('mysql+pymysql://'+SQL_USERNAME+':'+SQL_PASSWORD+'@'+SQL_ADDRESS+':'+SQL_PORT+'/'+SQL_SCHEMA)
app = Flask(__name__)

@app.route('/query', methods=['GET', 'POST'])
def query():
    def json_contents(cans):
        response = make_response(jsonify({
            'key':cans[0].tolist(),
            'value':cans[1]
            }))
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'POST'
        response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type' 
        return response
    def query_error(err_str):
        response = make_response('query-error:' + err_str)
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'POST'
        response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
        return response
    error = None
    if request.method == 'POST':
        qtype = None
        value = None
        try:
            qtype = request.form['type']
            value = request.form['value']
            if value == '' or value == None:return query_error()
            # print('request is ',request,'\n form is: ',request.form)
            if qtype == 'genre-year':
                return json_contents(movie_rate(engine,value,None,qtype))
            elif qtype == 'genre-quarter' or qtype == 'genre-month':
                val = value.split('-')
                return json_contents(movie_rate(engine,val[0],int(val[1]),qtype))
            elif qtype == 'boxing-month':
                return json_contents(boxing_money_month(engine,value))
            elif qtype == 'hot':
                return json_contents(top_20(engine,value))
            elif qtype == 'actor':
                return json_contents(actor_max(engine,value))
            elif qtype == 'boxing-year':
                return json_contents(boxing_money_year(engine))
            else:return query_error('cannot-resolve-type')
        # except KeyError:
            # return query_error('key-error')
        except IndexError:
            return query_error('index-error')
    else:
        pass

app.run(host='0.0.0.0',debug=False,port=5000)
