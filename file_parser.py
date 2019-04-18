# Raquib Talukder
# File Parsers

import sys
import time
import json
import json_reader

def args():
	if (len(sys.argv) != 3):
		print ('Arg Errors : python file_parser.py arp_file mac_file')
		sys.exit()

	# arp file
	arp_file = sys.argv[1]
	arp_hostname = get_hostname(arp_file)
	arp_json_file = arp_parser(arp_file, arp_hostname)

	# mac address file
	mac_file = sys.argv[2]
	mac_hostname = get_hostname(mac_file)
	mac_json_file = mac_parser(mac_file, mac_hostname)

	if (arp_hostname == mac_hostname):
		json_reader.reverse_arp(arp_json_file, mac_json_file, mac_hostname)
	else:
		print("Mac Address and ARP files aren't from the same host")
		sys.exit()

def arp_parser(filename, arp_hostname):
	ios_dir = "/root/topology_mapper/" + arp_hostname + "/ios_output/arp_output"
	data_dir = "/root/topology_mapper/" + arp_hostname + "/formatted_data/formatted_arps"
	keys = ["Protocol", "Address", "Age(min)", "Hardware Addr", "Type", "Interface"]
	arp_list = []

	(file_type, hostname, file_extension) = filename.split('.')

	arp_file_reader_name = ios_dir + "." + arp_hostname + "." + file_extension
	arp_file_writer_name = data_dir + "." + arp_hostname + "." + time_return() + ".json"

	arp_reader = open(arp_file_reader_name, 'r')
	arp_writer = open(arp_file_writer_name, 'w+', encoding="utf8")

	for i in arp_reader:
		mylist = (i.split('\\n'))

	for i in range(1, len(mylist)-1):
		info_tuple = ((mylist[i]).split())
		arp_list.append(dict(zip(keys, info_tuple)))

	# manipulate last indice 
	last_index = (mylist[-1])
	mystr = last_index[:-2]
	info_tuple = (mystr.split())
	arp_list.append(dict(zip(keys, info_tuple)))

	# pretty printing
	arp_writer.write(json.dumps(arp_list, sort_keys=True, indent=4, separators=(',', ': ')))

	# close out files
	arp_reader.close()
	arp_writer.close()

	return arp_file_writer_name

def mac_parser(filename, mac_hostname):
	ios_dir = "/root/topology_mapper/" + mac_hostname + "/ios_output/mac_output"
	data_dir = "/root/topology_mapper/" + mac_hostname + "/formatted_data/formatted_macs"
	keys = ["Vlan", "Mac Address", "Type", "Ports"]
	mac_list = []
	vlan_line = 0

	(file_type, hostname, file_extension) = filename.split('.')

	mac_file_reader_name = ios_dir + "." + mac_hostname + "." + file_extension
	mac_file_writer_name = data_dir + "." + mac_hostname + "." + time_return() + ".json"

	mac_reader = open(mac_file_reader_name, 'r')
	mac_writer = open(mac_file_writer_name, 'w+', encoding="utf8")

	for i in mac_reader:
		mylist = (i.split('\\n'))

	for i in mylist:
		if "Vlan" in i:
			vlan_line = mylist.index(i)

	for i in range(vlan_line+2, len(mylist)-1):
		info_tuple = ((mylist[i]).split())
		if (info_tuple[0] != 'All'):
			mac_list.append(dict(zip(keys, info_tuple)))

	# pretty printing
	mac_writer.write(json.dumps(mac_list, sort_keys=True, indent=4, separators=(',', ': ')))
	
	# close out files
	mac_reader.close()
	mac_writer.close()
	return mac_file_writer_name

def get_hostname(filename):
	(file_type, hostname, file_extension) = filename.split('.')
	return hostname

def time_return():
	timestr = time.strftime("%m%d%Y-%H:%M")
	return timestr

if __name__ == "__main__":
	args()
	print("Parameters Used - ARP File:\t\t " + sys.argv[2])
	print("Parameters Used - Mac Address File:\t " + sys.argv[1])