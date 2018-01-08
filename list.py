#!/usr/bin/python3

list = [ 1, 2, 4, 2, 7, 8, 9 ]

def sum(list):
	result = 0
	for i in list:
		result += i
	return result;

def average(list):
	result = 0.0
	size = len(list)

	if (size == 0):
		return 0.0

	for i in list:
		result += i

	result /= size
	return result

def median(list):
	copy = sorted(list)
	size = len(copy)
	if (size == 0):
		return 0

	middle = int((size - 1) / 2)

	if ((size % 2) == 0):
		return (copy[middle] + copy[middle + 1]) / 2.0
	else:
		return float(copy[middle])

def evens(list):
	result = 0
	for i in list:
		if ((i % 2) == 0):
			result += 1
	return result

def odds(list):
	result = 0
	for i in list:
		if ((i % 2) != 0):
			result += 1
	return result

def menu():
	print()
	print("Please choose an action:")
	print()
	print("(1) Print current values")
	print("(2) Insert value to list")
	print("(3) Remove value from list")
	print("(9) Exit program")
	print()
	return eval(input("Your choice? "))

def results():
	print("The content of the list is %s" % list)
	print("The sum of the list is %d" % sum(list))
	print("The average of the list is %.1f." % average(list))
	print("The median of the list is %.1f" % median(list))
	print("The number of evens in the list is %d" % evens(list))
	print("The number of odds in the list is %d" % odds(list))

def insert():
	position = eval(input("Insert at position? "))
	value = eval(input("Insert which value? "))

	list.insert(position, value)

def delete():
	position = eval(input("Delete value at position? "))
	
	del list[position]

print()
print("Welcome to list demonstration!")
print("==============================")

while (True):
	num = menu()

	if (num == 1):
		results()
	elif (num == 2):
		insert()
	elif (num == 3):
		delete()
	elif (num == 9):
		exit()

