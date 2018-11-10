#!/usr/bin/python3

lines = 20

spaces = lines - 1
stars  = 1
for line in range(0, lines):
	for i in range(0, spaces):
		print(" ", end = "")
	for i in range(0, stars):
		print("*", end = "")
	print("")
	spaces -= 1
	stars  += 2
