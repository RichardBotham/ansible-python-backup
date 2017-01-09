'''

! Notes

>>> 2 **(class_b_bin.count("0"))
32

					subnets         hosts
/19	255.255.224.0	2048 	(2046)	8190
Class B

          Subnet bits 	Host Bits
/21      |------------|-----------|

11111111.11111111.11111000.00000000
!


logic ( class b ) for /21 mask

bit_string = "11111111.11111111.11111100.00000000"
host_bits = bit_string.count("0")

subnet_mask = 21
class_a = 8
class_b = 16
class_c = 24

if net_bits > class_b and net_bits < class_c:
	class_bits = class_b
	subnet_bits = (class_bits - host_bits)


max_nets = (2 ** host_bits -2)
'''

#! Begin working Code
#!
bit_string = "11111111.11111111.11111111.11110000"
#
host_bits = bit_string.count("0")
net_bits = bit_string.count("1")
#
mask_octets = bit_string.split(".")
#
class_a_bin = mask_octets[0] + mask_octets[1]
class_b_bin = mask_octets[2]
class_c_bin = mask_octets[3]
#
class_a = 8
class_b = 16
class_c = 24
#
#
if net_bits >= class_a and net_bits < class_b:
	class_bits = class_a
	max_subnets = 2 ** (class_a_bin.count("1"))
	hosts = 2 ** host_bits -2
	subnets = 2 ** (host_bits)
	sub_block = 2 ** (class_a_bin.count("0"))
	print "Subnet Mask", net_bits
	print "Maximum subnets", max_subnets
	print "Number of Hosts\t", hosts
	print "Class bits", class_bits
	print "Host bits", host_bits
	print "Sub block is" , sub_block
	
	for a in range(10,256,1):
			for b in range(0,256,sub_block):
				print "Class A Subnet number " + str(a) + "." + str(b) + ".0" + ".0" + "/" + str(net_bits)

elif net_bits >= class_b and net_bits < class_c:
	class_bits = class_b
	max_subnets = 2 ** (class_b_bin.count("1"))
	hosts = 2 ** host_bits -2
	subnets = 2 ** (host_bits)
	sub_block = 2 ** (class_b_bin.count("0"))
	print "Subnet Mask", net_bits
	print "Maximum subnets", max_subnets
	print "Number of Hosts\t", hosts
	print "Class bits", class_bits
	print "Host bits", host_bits
	print "Sub block is" , sub_block
	
	for a in range(10,256,1):
			for b in range(0,256,sub_block):
				print "Class B Subnet number " + str(b) + " is : --> " + "1." + str(a) + "." + str(b) + ".0" + "/" + str(net_bits)
elif net_bits >= class_c:
	class_bits = class_c
	max_subnets = 2 ** (class_c_bin.count("1"))
	hosts = 2 ** host_bits - 2
	subnets = 2 ** (host_bits)
	sub_block = 2 ** (class_c_bin.count("0"))
	print "Subnet Mask", net_bits
	print "Maximum subnets", max_subnets
	print "Number of Hosts\t", hosts
	print "Class bits", class_bits
	print "Host bits", host_bits
	print "Sub block is" , sub_block
	for a in range(10, 256, 1):
		for b in range(0, 256, sub_block):
			print "Class C Subnet number " + str(b) + " is : --> " + "1." + str(a) + "." + str(b) + ".0" + "/" + str(net_bits)


#! End of working code