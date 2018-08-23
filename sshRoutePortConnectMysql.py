# coding:utf-8
'''
# 希望对大家有帮助哈，请多提问题
create by mgl
date: 2018/04/14
'''
import sys
import MySQLdb
import os
from sshtunnel import SSHTunnelForwarder
def write_to_txt_file(filename, results_list):
    # 如果该文件已存在，则删除该文件
    if os.path.exists(filename)==True:
        os.remove(filename)
    with open(filename, "ab") as f:
        for item in results_list:
            b = "\t".join([str(a) for a in item])
            # print b
            f.write(b + "\n")
'''
出于安全考虑，数据库服务器只允许堡垒机通过ssh访问，这对日常的使用带来了麻烦。
昨天的工作中，就遇到了这样的问题，MySQL数据库放在了服务器A上，只允许服务器B来访问，
而我在机器C上，可以通过ssh连接服务器B。
'''
# 定义MySQL操作命令
sql1="select * from sepcify_database.one_and_two_stars limit 10"  # 指定了操作表所在的数据库名字
sql2="select * from one_and_two_stars limit 10"   # 没有指定操作表所在的数据库名字

# 连接数据库
def ssh_connect_and_read_db(out_savename):
    with SSHTunnelForwarder(
            ('35.189.165.143', 22),  # B机器的配置--跳板机
            ssh_username="root",  # B机器的配置--跳板机账号
            ssh_password="passwdxx",  # B机器的配置--跳板机账户密码
            remote_bind_address=('35.200.3.252', 3306)) as server:  # A机器的配置-MySQL服务器

        conn = MySQLdb.connect(host='127.0.0.1',  # 此处必须是必须是127.0.0.1，代表C机器
                               port=server.local_bind_port,
                               user='root',   # A机器的配置-MySQL服务器账户
                               passwd='passwd' # A机器的配置-MySQL服务器密码c
							               ,charset='utf8'      # 和数据库字符编码集合，保持一致，这样能够解决读出数据的中文乱码问题
                               ,db='mysql' # 可以限定，只访问特定的数据库,否则需要在mysql的查询或者操作语句中，指定好表名
                               )
        # print conn
        # 打开数据库
        cursor=conn.cursor()
        # 执行sql操作
        try:
            # test1
            cursor.execute("SELECT VERSION()")
            data = cursor.fetchone()
            print "Database version : %s " % data
            # test2
            test_sql = "select *  from test limit 3"
            cursor.execute(test_sql)
            data = cursor.fetchall()
            data_list = list(data)
            # 写入txt文档
            write_to_txt_file(out_savename,data_list)
            #return data_list
        except:
            info = sys.exc_info()
            print info[0]
            print info[1]
        # 关闭数据库
        conn.close()
ssh_connect_and_read_db("out_savename.txt")