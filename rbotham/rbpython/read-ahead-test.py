
import re
fopen = open("myiprouteout.txt", "r")
routes = fopen.readlines()

for route in routes:
    if re.search(r".+subnetted.+", route):
        amount_subnets = re.search(r"[0-9]+\ssubnets", route)
        print route.strip(), "\t\t\t\t\t\t\t\tAmount of subnets are",amount_subnets.group()



'''
route_string = "     198.18.40.0/32 subnetted, 6 subnets"

if re.search(r".+subnetted.+", route_string):
    line = re.search(r".+subnetted.+", route_string)
    print "Match Found", line.group()
'''

fopen.close()