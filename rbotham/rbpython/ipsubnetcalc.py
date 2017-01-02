# rich test ip subnet calc
#
#

class SubnetCalc(object):
		def __init__(self, ip_addr, ip_mask):
				self.ip_addr = ip_addr; print "IP address is", self.ip_addr,"\n"
				self.ip_mask = ip_mask; print "IP netmask is", self.ip_mask, "\n"
		
		def convert_to_binary(self):
				
				
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
								
				hostbits = bin_mask1.count('0') + bin_mask2.count('0')+ bin_mask3.count('0')+ bin_mask4.count('0'); print "host bits are", hostbits
			
				mask_bits = (32 - hostbits);print "mask bits are", mask_bits,"\n"
				
	
				if mask_bits >= 24: 
					print "ip mask is ",self.ip_mask
					max_subnets = (2 ** (mask_bits - 24))
					max_hosts = (2 ** hostbits - 2)
					print "The subnet mask is a \t\t\t", mask_bits
					print "Maximum subnets are:\t\t\t", max_subnets
					print "Maximum hosts per subnet are:\t", max_hosts 
					
				elif mask_bits < 24 and mask_bits >= 16:
					max_subnets = (2 ** (mask_bits - 8))
					max_hosts = (2 ** hostbits - 2)
					print "The subnet mask is a \t\t\t", mask_bits
					print "Maximum subnets are:\t\t\t", max_subnets
					print "Maximum hosts per subnet are:\t", max_hosts 
			
			
				'''
				this bit is wrong
				'''
				
				elif mask_bits < 16 and mask_bits >= 8:
					max_subnets = (2 ** (mask_bits))
					max_hosts = (2 ** (hostbits - 2))
					print "The subnet mask is a \t\t\t", mask_bits
					print "Maximum subnets are:\t\t\t", max_subnets
					print "Maximum hosts per subnet are:\t", max_hosts 
				
							

#---------------------------------------------------#
test_ip = SubnetCalc('120.100.45.6', '255.255.224.0')
test_ip.convert_to_binary()

