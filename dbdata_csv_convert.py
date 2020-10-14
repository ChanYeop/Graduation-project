import pymysql
import pandas as pd
import numpy as np

conn=pymysql.connect(host='localhost', user='root', password='long', db='db', charset='utf8')
cursor=conn.cursor()
sql="select * from rss_data"
cursor.execute(sql)
result=cursor.fetchall()
conn.close()
df=pd.DataFrame.from_records(result)
df.to_excel('test75.xlsx')
