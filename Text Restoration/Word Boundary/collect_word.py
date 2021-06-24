import sys
text = ""
infile = open(sys.argv[1])
for line in infile:
	line = line.strip()
	if line.startswith("_ _ _ _ _ _ _"):
		if line.endswith("1"):
			text += line.split()[7]
			text += " "
		else:
			text += line.split()[7]

	else:
		if line.endswith("1"):
			text += line.split()[7] + " "
		else:
			text += line.split()[7]
text = text.strip().split()