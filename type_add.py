# Raquib Talukder
# Master Skill List

import sys

def type_add(skill):

	quit_words = ["quit", "exit", "", " ", "\n"]

	if skill in quit_words:
		print("System has quit")
		sys.exit()

	skill_split = skill.split("\n")
	level = ['Administration', 'Design', 'Development', 'Pre-Sales', 'QA Test', 'Support']
	for i in skill_split:
		if i.strip() == "":
			break
		for j in level:
			print(i.strip() + "-" + j)

while True:
	skill =  raw_input(">>> Enter skill name: ")
	type_add(skill)
