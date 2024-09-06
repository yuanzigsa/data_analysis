# @Author  : yuanzi
# @Time    : 2024/9/1 9:59
# Website: https://www.yzgsa.com
# Copyright (c) <yuanzigsa@gmail.com>

import pandas as pd
from sqlalchemy import create_engine
from pandas.core.methods.to_dict import to_dict

# 创建一个DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

result = df['Name'][0]

print(to_dict(df))


host = 'localhost'
port = 3306
username = 'root'
password = 'lijinyuan20'
database = 'demo'


sql = "SELECT * FROM users"

engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")

df = pd.read_sql_query(sql, engine)


print(df.to_json(orient='records'))

