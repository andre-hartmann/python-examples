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
	size = len(list)
	if (size == 0):
		return 0

	middle = int((size - 1) / 2)

	if ((size % 2) == 0):
		return (list[middle] + list[middle + 1]) / 2.0
	else:
		return float(list[middle])

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

print("The content of the list is %s" % list)
print("The sum of the list is %d" % sum(list))
print("The average of the list is %.1f." % average(list))
print("The median of the list is %.1f" % median(list))
print("The number of evens in the list is %d" % evens(list))
print("The number of odds in the list is %d" % odds(list))

