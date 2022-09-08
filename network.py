import netifaces as ni

ip = ni.ifaddresses('wlo1')[ni.AF_INET][0]['addr']
mask = ni.ifaddresses('wlo1')[ni.AF_INET][0]['netmask']
broadcast = ni.ifaddresses('wlo1')[ni.AF_INET][0]['broadcast']
mac = ni.ifaddresses('wlo1')[ni.AF_LINK][0]['addr']

ipsplit = ip.split('.')
masksplit = mask.split('.')

ipoctet1 = bin(int(ipsplit[0]))
ipoctet2 = bin(int(ipsplit[1]))
ipoctet3 = bin(int(ipsplit[2]))
ipoctet4 = bin(int(ipsplit[3]))

maskoctet1 = bin(int(masksplit[0]))
maskoctet2 = bin(int(masksplit[1]))
maskoctet3 = bin(int(masksplit[2]))
maskoctet4 = bin(int(masksplit[3]))

if int(masksplit[0]) != 0:
	 cidr = len(maskoctet1.split('b')[1])
	 if int(masksplit[1]) != 0:
		 cidr = cidr + len(maskoctet2.split('b')[1])
		 if int(masksplit[2]) != 0:
			 cidr = cidr + len(maskoctet3.split('b')[1])
			 if int(masksplit[3]) != 0:
				 cidr = cidr + len(maskoctet4.split('b')[1])
				 
print(f'Your subnet mask is /{cidr} in CIDR notation!')
hostbits = 32 - int(cidr)
print(f'Based on your subnet mask, there are {cidr} network bits turned on and {hostbits} bits turned on.')
total = pow(2, hostbits) - 2
print(f'This means there are a total of {total} usable IP addresses in your subnet!')


