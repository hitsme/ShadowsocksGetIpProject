#coding:utf-8
import MySQLdb
def getconnectdb():
    return MySQLdb.connect("127.0.0.1","root","passwdxx","mysql")
def sendmessage():
    db=getconnectdb()
    cursor=db.cursor()
    sql="select * from serviceiphistory where issend='0'"
    cursor.execute(sql)
    result=cursor.fetchall()
    for i in range(len(result)):
      print result[i][1]
if __name__=='__main__':
    sendmessage()