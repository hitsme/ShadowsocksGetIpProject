#!/usr/bin/env python
#coding:utf-8
 
def pingone():
    import os
    return1=os.system('ping 8.8.8.8')
    if return1:
        print 'ping fail'
    else:
        print 'ping ok'
         
def pingtwo():
    import os
    import subprocess
     
    fnull = open(os.devnull, 'w')
    return1 = subprocess.call('ping 8.8.8.8', shell = True, stdout = fnull, stderr = fnull)
    if return1:
        print 'ping fail'
    else:
        print 'ping ok'
    fnull.close()
 
if __name__=='__main__':
    pingone()