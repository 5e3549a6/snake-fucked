#!/usr/bin/python3
# encoding = utf-8
# 
# python实现栈

class Stack:

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self,item):
		return self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		# 返回栈顶端元素
		return self.items[len(self.items) - 1]

	def sizi(self):
		return len(self.items)


