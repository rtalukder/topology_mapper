# Raquib Talukder
# Reverse ARP

import time
import json

def reverse_arp(arp_json_file, mac_json_file, hostname):
	rarp_dir = "rarp_output/rarp_search"
	rarp_file_writer_name = rarp_dir + "." + hostname + "." + time_return() + ".json"


	arp_json = open(arp_json_file, 'r', encoding="utf8")
	mac_json = open(mac_json_file, 'r', encoding="utf8")
	rarp_file = open(rarp_file_writer_name, 'w', encoding="utf8")

	arp_json_data = json.load(arp_json)
	mac_json_data = json.load(mac_json)

	keys = ["IP Addr", "Mac Addr", "Port", "Vendor", "VLAN", "Age(min)"]
	successful_rarp = []

	for i in arp_json_data:
		arp_json_item = i
		matched_mac = [mac_json_item for mac_json_item in mac_json_data if mac_json_item['Mac Address'] == arp_json_item['Hardware Addr']]
		
		if len(matched_mac) > 0:
			vendor = OUI_finder(mac_first_six(matched_mac[0]['Mac Address']))
			values = [arp_json_item['Address'], arp_json_item['Hardware Addr'], matched_mac[0]['Ports'],
						 vendor, matched_mac[0]['Vlan'], arp_json_item['Age(min)'] ]
			successful_rarp.append(dict(zip(keys, values)))
	

	rarp_file.write(("    !--- RARP for: " + hostname + " ---!\n"))
	rarp_file.write((json.dumps(successful_rarp, sort_keys=True, indent=4, separators=(',', ': '))))

def mac_first_six(mac_addr):
	modified_mac_addr = mac_addr.replace(".", "")
	mac_addr_first_six = modified_mac_addr[:6]

	return mac_addr_first_six

def time_return():
	timestr = time.strftime("%Y%m%d-%H%M")
	return timestr

def OUI_finder(mac_addr):
	mac_json_file = open('mac_to_vendor.json', 'r', encoding="utf8")

	mac_addr_json = json.load(mac_json_file)

	for mac_addr_item in mac_addr_json:
		if (mac_addr_item['mac'] == mac_addr):
			return (mac_addr_item['vendor'])

