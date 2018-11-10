#!/usr/bin/python3

spaces = 3
stars  = 1
for line in range(0, 4):
	for i in range(0, spaces):
		print(" ", end = "")
	for i in range(0, stars):
		print("*", end = "")
	print("")
	spaces -= 1
	stars  += 2
