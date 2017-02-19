
import re
fopen = open("myiprouteout.txt", "r")
routes = fopen.readlines()

subnet_marker = []


for subnet_index, route in enumerate(routes):
    if re.search(r".+subnetted.+", route):
        amount_subnets = re.search(r"[0-9]+\s", route)
        print route.strip(), "\n", "Subnet amount is --> ", amount_subnets.group()
        print "subnet index is at line  -->", subnet_index, "\n"
fopen.close()





'''

Notes
route_string = "     198.18.40.0/32 subnetted, 6 subnets"

if re.search(r".+subnetted.+", route_string):
    line = re.search(r".+subnetted.+", route_string)
    print "Match Found", line.group()
'''
