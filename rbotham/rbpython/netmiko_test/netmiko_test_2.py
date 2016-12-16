# Test 1 - Basic netmiko test
# 07-10-2016
#
#
#

from netmiko import ConnectHandler
from datetime import datetime
import os


fopen = open('pre_collection.txt', 'w+')
cmdopen = open('junos_commands', 'r')
cmdline = cmdopen.readlines()

j_cmds = []

for item in cmdline:
	j_cmds.append(item)
	print item
	

juniper = {
    'device_type': 'juniper',
    'ip':   '120.120.100.2',
    'username': 'rich',
    'password': 'ccie10808',
    'port' : 22,          	# optional, defaults to 22
    'secret': '',     		# optional, defaults to ''
    'verbose': False,       	# optional, defaults to False
}

net_connect = ConnectHandler(**juniper)
os.system('clear')




# print start date
print "-----------------------------------------\n"
print "\nStartTime: " + str(datetime.now())


for  item in j_cmds:
	output = net_connect.send_command(item)
	print output
        fopen.write(output) 


print "-----------------------------------------\n"
print "\nEndTime: " + str(datetime.now())
#Print some output



fopen.close()
