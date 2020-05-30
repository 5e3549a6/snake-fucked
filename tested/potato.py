# 传土豆游戏



from pythonds.basic import Queue

def hot(names,num):
	simque = Queue()
	for name in names:
		simque.enqueue(name)

	while simque.size() > 1:
		for i in range(num):
			simque.enqueue(simque,dequeue())

		simque.dequeue()

	return simque.dequeue()



hot(['bill','kill','kandy'],3)