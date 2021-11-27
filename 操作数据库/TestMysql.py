from pymysql import *

# 创建数据库链接
conn = connect(host="10.10.111.59",user="root",password="1qaz@WSX",database="zmt_jsjg",charset="utf8")

# 创建游标对象，可以利用此对象操作数据库
try:
    cur = conn.cursor()
    cur.execute("select * from p_user")
    result = cur.fetchall()
    print("succes")
    print(result)

    pass
except Exception as e:
    print(e)
finally:
    cur.close()
    conn.close()