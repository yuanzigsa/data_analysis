# @Author  : yuanzi
# @Time    : 2024/8/31 12:38
# Website: https://www.yzgsa.com
# Copyright (c) <yuanzigsa@gmail.com>
import json
import pandas as pd
from utils.conmysql import conmysql
from flask import Flask, render_template, request, redirect, make_response, abort

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    number = 1
    if request.method == 'GET':
        return render_template('index.html', number=number)
    if request.method == 'POST':
        query_sql = request.form.get('sql')
        # if "select" or ";" not in query_sql:
        #     return "查询语句不合法！"
        df = pd.read_sql_query(query_sql, conmysql())
        return f'查询结果为：{df.to_dict(orient="records")}'

@app.route('/query')
def query():
    data ={
        'name': '张三',
        'age': 18,
        'gender': '男'
    }
    # abort(403)
    response = make_response(json.dumps(data, ensure_ascii=False))
    response.headers['Content-Type'] = 'application/json'

    return response


if __name__ == '__main__':
    app.run()

