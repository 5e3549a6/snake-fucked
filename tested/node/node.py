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


		