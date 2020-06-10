#!/usr/bin/python3
# encoding = utf-8
# Chapter 3
#
# python实现队列
#
# 队列的头部位于列表的0索引处



class queue:

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self,item):
		self.items.insert(0,item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)


