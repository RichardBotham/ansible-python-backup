# rich test ip subnet calc
#
#
'''

Note on split('0b')[1]
What this does is format the 'textual' representation of a binary number and removes the '0b' and prints the 1st value in lis t that has been split - NOT the '0'th value.
This doesnt change the actual value of the real binary number 

note >>> y = ((x ** 2) -2) power of operator
'''


class SubnetCalc(object):
		def __init__(self, ip_addr, ip_mask):
				self.ip_addr = ip_addr; print(ip_addr),"\n"
				self.ip_mask = ip_mask; print(ip_mask),"\n"
		
		def convert_to_binary(self):
				
				#all_ones = 255
				
				ip_octets = self.ip_addr.split(".")
								
				bin_ip1 = bin(int(ip_octets[0]))
				bin_ip2 = bin(int(ip_octets[1]))
				bin_ip3 = bin(int(ip_octets[2]))
				bin_ip4 = bin(int(ip_octets[3]))
				
				mask_octets = self.ip_mask.split(".")
				bin_mask1 = bin(int(mask_octets[0])).split('0b')[1].zfill(8)
				bin_mask2 = bin(int(mask_octets[1])).split('0b')[1].zfill(8)
				bin_mask3 = bin(int(mask_octets[2])).split('0b')[1].zfill(8)
				bin_mask4 = bin(int(mask_octets[3])).split('0b')[1].zfill(8)
								
				hostbits = bin_mask1.count('0') + bin_mask2.count('0')+ bin_mask3.count('0')+ bin_mask4.count('0'); print "host bits are", hostbits, "\n"
				
				mask_bits = (32 - hostbits); print "mask bits are ", mask_bits, "\n"
				
				
				#max_hosts = ((2 ** hostbits) -2)
	
				'''
				work out class C
				'''
	
				if mask_bits >= 24:
					max_subnets = (2 ** (mask_bits - 24))
					max_hosts = (2 ** hostbits - 2)
					print "The subnet mask is a \t\t\t", mask_bits
					print "Maximum subnets are:\t\t\t", max_subnets
					print "Maximum hosts per subnet are:\t", max_hosts 
			
				
							
										
																
				#print "ip address is :" , self.ip_addr , "\n"
				#print "ip netmask is :" , self.ip_mask , "\n"
				
				#print "the bit string is \n\n", bin_mask1, bin_mask2, bin_mask3, bin_mask4, "\n"
				
				#print "host bit '0' count is:\t\t", hostbits, "\n"			
				
				#print "mask bit '1' count is:\t\t", mask_bits, "\n"
				
				#print "max hosts per subnet are:\t" , max_hosts, "\n"
				
				#print "max subnets are:\t\t", (max_hosts / 255), "\n"
				
				
				
					
					
											






#---------------------------------------------------#
test_ip = SubnetCalc('120.100.45.6', '255.255.255.0')
test_ip.convert_to_binary()


'''
<type 'int'>
<type 'str'>
>>> 
>>> 
>>> y = ((x ** 2) -2)
Traceback (most recent call last):
  File "<string>", line 1, in <module>
NameError: name 'x' is not defined
>>> y
Traceback (most recent call last):
  File "<string>", line 1, in <module>
NameError: name 'y' is not defined
>>> a = '240'
>>> b = int(a)
>>> c = bin(b)
>>> c
'0b11110000'
>>> c = bin(b).split(0b)[1]
  File "<string>", line 1
    c = bin(b).split(0b)[1]
                      ^
SyntaxError: invalid token
>>> c = bin(b)
>>> d = c.split('0b')[1]
>>> d
'11110000'
>>> e = d.count(0)
Traceback (most recent call last):
  File "<string>", line 1, in <module>
TypeError: expected a character buffer object
>>> e = d.count('0')
>>> e
4
>>> f = ((2 ** e)-2)
>>> f
14
'''
