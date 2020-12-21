#!/usr/bin/python3

with open("input","r") as f:
	lines = f.readlines()


r = """byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)"""
required = []
for l in r.split("\n"):
	required.append(l.split(" ")[0])



passports = []
passport = {}
for line in lines:
	for kv in line.split(" "):
		for r in required:
			if r in kv:
				passport[kv.split(":")[0]] = kv.split(":")[1].strip()
	if not line.strip():
		passports.append(passport)
		passport = {}
passports.append(passport)



import re

def check_valid(p):
	valid = True
	for l in required[:-1]:
		if l not in p.keys():
			valid = False

	if "byr" in p and not 1920 <= int(p["byr"]) <= 2002:
		print("byr")
		valid = False		
	if "iyr" in p and not 2010 <= int(p["iyr"]) <= 2020:
		print("iyr")
		valid = False		
	if "eyr" in p and not 2020 <= int(p["eyr"]) <= 2030:
		print("eyr")
		valid = False		
	if "hgt" in p:
		if  p["hgt"][-2:] not in ["cm","in"]:
			valid = False
		elif p["hgt"][-2:] == "cm":
			if not 150 <= int(p["hgt"].strip("cm")) <= 193:
				valid = False
		elif p["hgt"][-2:] == "in":
			if not 59 <= int(p["hgt"].strip("in")) <= 76:
				valid = False
	if "hcl" in p and not (re.search("^#[0-9a-f]{6}$",p["hcl"])):
		print("hcl")
		valid = False
	if "ecl" in p and not (re.search("^amb|blu|brn|gry|grn|hzl|oth$",p["ecl"])):
		print("ecl")
		valid = False
	if "pid" in p and not (re.search("^[0-9]{9}$",p["pid"])):
		print("pid")
		valid = False

	return valid


valids = 0
for passport in passports:
	print(passport)
	valid = check_valid(passport)

	if valid:
		print("valid")
		valids += 1


print("valids: ",valids)
















