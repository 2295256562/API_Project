import pymysql


# 配置连接信息
config = {
    'host':'127.0.0.1',
    'port':3306,
    'user':'root',
    'password':'123',
    'db':'t1',
    'charset':'utf8mb4',
    'cursorclass':pymysql.cursors.DictCursor,
}

class DBMysql:
    def do_mysql(self,query_mysql, state='all'):
        # 创建连接
        connection = pymysql.connect(**config)
        # 游标
        cursor = connection.cursor()
        # 执行语句
        cursor.execute(query_mysql)
        if state ==1:
            res = cursor.fetchone()
        else:
            res = cursor.fetchall()
        # 关闭游标
        cursor.close()
        # 关闭连接
        connection.close()
        return res