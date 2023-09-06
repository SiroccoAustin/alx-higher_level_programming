#!/usr/bin/python3
def uppercase(str):
	for i in str:
		character = i
		if ord(i) >= ord('a') and ord(i) <= ord('z'):
			character = chr(ord(i) - 32)
		print(character, end='')
