#!/usr/bin/python3

with open("input","r") as f:
	lines = f.readlines()

expenses = []

for line in lines:
	expenses.append(int(line))

for i in expenses:
	for j in expenses:
		for z in expenses:
			if i+j+z == 2020:
				print(i,j,z)






