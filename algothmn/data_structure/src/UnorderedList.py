#!/usr/bin/python3
# coding =utf-8
# 
# python实现链表

class Node:
	#python实现链表的节点
	def __init__(self,initdata):
		self.data = initdata
		self.next = None

	def getData(self):
		# 返回下一节点的数据
		return self.data

	def getNext(self):
		# 返回下一个节点
		return self.next

	def setData(self,newdata):
		# 设置下一节点数据
		self.data = newdata

	def setNext(self,newnext):
		# 设置下一节点
		self.next = newnext

"""
>>>temp = Node(89)
>>>temp.getData()
>>>89
>>>te


"""







class UnorderedList:
	def __init__(self):
		# 初始化节点为None
		self.head = None

	def isEmpty(self):
		# 直接返回None
		return self.head == None

	def add(self,item):
		# 
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp

	def length(self):
		current = self.head
		count = 0
		while current != None:
			count = count + 1
			current = current.getNext()

		return count

	def search(self):
		current = self.head
		found = False
		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()

		return found

	def remove(self,item):
		current = self.head
		previous = None
		found = False
		while not found:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()

		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())


# 练习

	def append(self,item):
		# append操作的时间复杂度为O(n)
		# append操作作为结尾追加元素函数，可以直接访问列表的最后元素
		# 但是对于无序列表来说，最后的元素是不确定的，所以应该采用遍历的方法来构造
		current = self.head






	def insert(self,item):









tempp = Node(99)
t = tempp.getData()
print(t)

temp.add(8888)

















