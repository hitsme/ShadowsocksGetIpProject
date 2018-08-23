# coding:utf-8
'''
vps重启后获取服务最新ip，
然后想主服mysql插入
'''
import  os
import MySQLdb
import datetime
def getNewIp():
    #ret=os.system("curl ")
    ret=os.popen("curl icanhazip.com").read()
    return ret

def getconnectdb():
    return MySQLdb.connect('35.200.3.252','root','passwdxx','mysql')
def ipinserttodb():
    db=getconnectdb()
    cursor=db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS `serviceiphistory`(
        `row_id` INT UNSIGNED AUTO_INCREMENT,
        `ip` VARCHAR(20) NOT NULL,
        `isreboot` VARCHAR(10) NOT NULL,
        `issend` VARCHAR(10) NULL,
        `isactivity`  VARCHAR(10) NULL,
        `insertdate` DATE NULL,
        `senddate` DATE NULL,
        PRIMARY KEY ( `row_id` )
        )ENGINE=InnoDB DEFAULT CHARSET=utf8;''')
    newip=getNewIp()
    dt=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("insert into serviceiphistory(\
    ip,\
    isreboot,\
    issend,\
    isactivity,\
    insertdate,\
    senddate)\
    values ('%s',\
    '%s',\
    '%s',\
    '%s',\
    '%s',\
    '%s')" % \
    (newip,'1','0','1',dt,''))
    db.commit()
    db.close()
if __name__=='__main__':
    #tstr=getNewIp()
    #ipstr=str(tstr)[0]
    #truefalse=(ipstr=='35.194.161.223')
    ipinserttodb();
    print "ip changed"