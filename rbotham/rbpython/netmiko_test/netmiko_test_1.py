# Test 1 - Basic netmiko test
# 07-10-2016
#
#
#

from netmiko import ConnectHandler
from datetime import datetime
import os


fopen = open('pre_collection.txt', 'w+')



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


j_cmds = ['show configuration | display set | no-more','show route | no-more ', 'show route protocol bgp | no-more', 'show arp | no-more']

cmd_line = ""

# print start date
print "-----------------------------------------\n"
print "\nStartTime: " + str(datetime.now())


for index, item in enumerate(j_cmds):
	output = net_connect.send_command(item)
	cmd_line =  "Command being run = " + item + "\n" + output
	print cmd_line
	#print output
        fopen.write(cmd_line) 



print "-----------------------------------------\n"
print "\nEndTime: " + str(datetime.now())
#Print some output



fopen.close()
