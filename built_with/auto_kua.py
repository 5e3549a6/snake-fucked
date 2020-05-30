#!/usr/bin/python3
# coding = utf-8
# 
# stack实现匹配括号

from pythonds.basic import Stack 

def par(symbol):
	s = Stack()
	balanced = True
	index = 0
	while index < len(symbol) and balanced:
		sym = symbol[index]
		if symbol == "(":
			s.push(sym)
		else:
			if s.isEmpty():
				balanced = False
			else:
				s.pop()
		index = index + 1

	if balanced and s.isEmpty():
		#return True
		print(True)
	else:
		#return False
		print(False)


par("()")