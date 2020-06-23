import pymysql  # 固定，导入pymsql
# pymysql
# 查询方法
def query(sql): # sql语句str类型
    db = pymysql.connect(host='192.144.148.91', user='ljtest', password='123456', db="ljtestdb")
    cur = db.cursor()
    cur.execute(sql)
    res = cur.fetchall() # 获取所有的结果
    db.close()          # 关闭连接
    return res

# 修改、增加、删除
def commit(sql):
    db = pymysql.connect(host='192.144.148.91', user='ljtest', password='123456', db="ljtestdb")
    cur = db.cursor()
    cur.execute(sql)
    db.commit() # 修改生效
    db.close()

if __name__ == "__main__": # 直接运行的py文件，才条件才成立
    # pymysql的sql语句原则，外双内单；外单内双。
    xiugai_sql = "update t_user set username='9529' where id=1234"
    commit(xiugai_sql)

    s = "select * from t_user where id=1234" # sql传字符串类型
    r = query(s) # = query方法的res
    print(r)