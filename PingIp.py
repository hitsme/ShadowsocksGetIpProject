import os 
exit_code=os.system("ping 35.200.23.23")
if exit_code:
    print "failed"