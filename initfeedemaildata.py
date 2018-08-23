#coding:utf-8
import MySQLdb

def getconnectdb():
    return MySQLdb.connect('127.0.0.1','root','passwdxx','mysql')
def createtableforemail():
    db=getconnectdb()
    cursor=db.cursor()
    cursor.execute('''create table if not exists `freindemailhistory`(
        `row_id` int unsigned auto_increment,
        `emailaccount` varchar(20) not null,
        `username` varchar(50) null,
        `adddate` date null,
        primary key (`row_id`)
        )engine=InnoDB default charset=utf8;''')
    print 'table freundemailhistory init secuss'
if __name__=='__main__':
        createtableforemail()
