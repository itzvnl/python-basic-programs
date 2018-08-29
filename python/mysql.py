import pymysql
connection = pymysql.connect(host='localhost',user='root',passwd='admin',db='py_work')
cursor=connection.cursor()
sql=('select * from Persons')
cursor.execute(sql)
data=cursor.fetchall()
print(data)
