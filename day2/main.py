

with open("input","r") as f:
	lines = f.readlines()


passwords = []
for line in lines:
	s = line.split(" ")
	min = int(s[0].split("-")[0])
	max = int(s[0].split("-")[1])
	c = s[1][:1]
	password = s[2]

	if (c == password[min-1] and c != password[max-1] ) or (c != password[min-1] and c == password[max-1] ):
		passwords.append(password)

print(len(passwords))

