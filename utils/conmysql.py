# @Author  : yuanzi
# @Time    : 2024/9/1 10:42
# Website: https://www.yzgsa.com
# Copyright (c) <yuanzigsa@gmail.com>

from sqlalchemy import create_engine


def conmysql():
    host = 'localhost'
    port = 3306
    username = 'root'
    password = 'lijinyuan20'
    database = 'demo'
    engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")

    return engine

