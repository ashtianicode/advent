
with open("input","r") as f:
	lines = f.readlines()

def count_encounter(slope):	
	width = len(lines[0])
	multiplier = int( (slope[0] * len(lines))/ width) + 2
	for i in range(len(lines)):
		s =  "".join(lines[i].strip("\n") * multiplier)
		lines[i] = s
		
	encounter = 0 
	col = 0
	for i,line in enumerate(lines[slope[1]::slope[1]]):
		col += slope[0]
		# print(i,col,slope)
		if len(line) > 0  and line[col] == "#":
			encounter += 1
		else:
			pass
	return encounter



slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]

for slope in slopes:
	print(count_encounter(slope))
	

