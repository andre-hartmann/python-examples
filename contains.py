#!/usr/bin/python3

def sumsUpTo(list, result):
	size = len(list)
	if size < 1:
		return False
	first = 0
	last = size - 1
	list.sort()

	while first < size and last > 0:
		sum = list[first] + list[last]
		if sum < result:
			first += 1
		elif sum > result:
			last -= 1
		else:
			return True
	return False

def assertSumsUpTo(list, number, expected):
	result = sumsUpTo(list, number)
	print(result == expected)

assertSumsUpTo([1, 2, 4, 6, 7, 11], 10, True)
assertSumsUpTo([2, 11, 1, 4, 7, 6], 10, True)
assertSumsUpTo([-3, 3], 0, True)
assertSumsUpTo([], 0, False)
assertSumsUpTo([0], 0, False)
assertSumsUpTo([0, 1], 1, True)
