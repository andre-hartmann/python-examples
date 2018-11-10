#!/usr/bin/python3

import os.path
import random

greetings = [ "Hello", "Hola", "Bonjour", "Hey" ]
settings = "greeter.txt"
choice = ''

random.seed()

if os.path.exists(settings):
	with open(settings, "r") as f:
		choice = f.read()

if (choice == ''):
	with open(settings, "w") as f:
		index = random.randint(0, len(greetings) - 1)
		choice = greetings[index]
		f.write(choice)

print(choice)

