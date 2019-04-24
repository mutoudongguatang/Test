#-*- coding:utf-8 -*-
#
import pymysql.cursors

#创建链接
db = pymysql.connect(host='MySQL的URL',
                             user='user',
                             password='password',
                             db='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
#创建游标
cur = db.cursor()

#执行查询SQL，并且只显示前十条数据
sql = 'select * from chef_food limit 10'

try:
    cur.execute(sql)
    results = cur.fetchall()
    print("id","food_name","ingredients")

    for row in results:
        id = row['id']
        food_name = row['food_name']
        ingredients = row['ingredients']
        print(id,food_name,ingredients)

except Exception as e:
    raise e
finally:
    db.close()