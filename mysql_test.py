import pymysql

# 使用 connect 方法，传入数据库地址，账号密码，数据库名就可以得到你的数据库对象
db = pymysql.connect(host="localhost", user="root", password="123456", db="aaa")

# 接着我们获取 cursor 来操作我们的 aaa 这个数据库
cursor = db.cursor()

sql = "insert into beautyGirls(name, age) values ('Mrs.cang', 18)"

try:
    cursor.execute(sql)
    db.commit()
except:
    # 回滚
    db.rollback()

# 最后我们关闭这个数据库的连接
db.close()
