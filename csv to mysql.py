import pandas as pd
from sqlalchemy import create_engine
import pymysql


pymysql.install_as_MySQLdb()

df = pd.read_csv('xsb.csv')

# 当engine连接的时候我们就插入数据
engine = create_engine('mysql://root:123456@localhost/xsb?charset=utf8')

with engine.connect() as conn, conn.begin():
    df.to_sql('xsb', conn, if_exists='replace')
