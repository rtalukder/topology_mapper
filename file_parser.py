# Raquib Talukder
# File Parsers

import sys
import time

def args():
	if (len(sys.argv) != 3):
		print ('Arg Errors : python file_parser.py mac_file arp_file')
		sys.exit()

    # mac address file
	mac_file = sys.argv[1]
	mac_parser(mac_file)
    # arp file
	arp_file = sys.argv[2]
	arp_parser(arp_file)

def mac_parser(filename):
	ios_dir = "ios_output/mac_output"
	data_dir = "data/formatted_macs"

	(file_type, hostname, file_extension) = filename.split('.')

	mac_file_reader_name = ios_dir + "." + hostname + "." + file_extension
	mac_file_writer_name = data_dir + "." + hostname + "." + time_return() + "." + file_extension

	print(mac_file_reader_name)
	print(mac_file_writer_name)

	mac_reader = open(mac_file_reader_name, 'r')
	mac_writer = open(mac_file_writer_name, 'w')

	mylist = []
	vlan_line = 0

	for i in mac_reader:
		mylist = (i.split('\\n'))

	for i in mylist:
		if "Vlan" in i:
			vlan_line = mylist.index(i)

	mac_writer.write("Vlan    Mac Address       Type        Ports\n\n")

	for i in range(vlan_line+2, len(mylist)-1):
		info_tuple = ((mylist[i]).split())
		if (info_tuple[0] != 'All'):
			print(info_tuple)
			mac_writer.write(str(info_tuple))
			mac_writer.write('\n')

	mac_reader.close()
	mac_writer.close()
	print("MACs completed")

def arp_parser(filename):
	ios_dir = "ios_output/arp_output"
	data_dir = "data/formatted_arps"

	(file_type, hostname, file_extension) = filename.split('.')

	arp_file_reader_name = ios_dir + "." + hostname + "." + file_extension
	arp_file_writer_name = data_dir + "." + hostname + "." + time_return() + "." + file_extension

	print(arp_file_reader_name)
	print(arp_file_writer_name)

	arp_reader = open(arp_file_reader_name, 'r')
	arp_writer = open(arp_file_writer_name, 'w')

	mylist = []
	vlan_line = 0

	for i in arp_reader:
		mylist = (i.split('\\n'))

	arp_writer.write("Protocol    Address          Age (min)  Hardware Addr   Type   Interface\n\n")

	for i in range(1, len(mylist)-1):
		info_tuple = ((mylist[i]).split())
		print(info_tuple)
		arp_writer.write(str(info_tuple))
		arp_writer.write('\n')

	# manipulate last indice 
	last_index = (mylist[-1])
	mystr = last_index[:-2]
	info_tuple = (mystr.split())
	print(info_tuple)
	arp_writer.write(str(info_tuple))
	arp_writer.write('\n')

	arp_reader.close()
	arp_writer.close()

	print("ARPs completed")

def time_return():
	timestr = time.strftime("%Y%m%d-%H%M")
	return timestr

if __name__ == "__main__":
	print("Mac address file: " + sys.argv[1])
	print("ARP file: " + sys.argv[2])
	args()