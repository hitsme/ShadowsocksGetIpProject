#!/usr/bin/expect
set timeout 30
spawn ssh 35.200.3.252
sleep 1 
expect "*password*"
sleep 1
send "passwdxx\r"
expect "*#"
send "mysql -u root -p\r"
sleep 1
expect "*password*" 
send "passwdxx"
expect "*#"
interact