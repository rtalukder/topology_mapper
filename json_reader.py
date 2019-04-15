import json
from pprint import pprint

myfile = open('mac_to_vendor.json', 'r', encoding="utf8")

data = json.load(myfile)

example="6805CA"

for i in range(len(data)):
	if (data[i]['mac'] == example):
		print(data[i]['vendor'])
	