# python 数据结构与算法



+   **大O记法**
+   **线性数据结构** 
+   **底层数据存储方法** 
+   **基本算法**



## **Order**

### 列表字典方法的大O性能

列表方法的大O性能：

| method  | order |
| ------- | ----- |
| append  | O(n)  |
| replace | O(n)  |
| remove  | O(n)  |





## 线性数据结构

1.  栈
1.  链表
1.  队列
1.  双端队列

### **栈** 



```python
#以pyhton内部数据结构元组或者列表实现栈
#自定义列表或元组的任意端为栈的底端和顶端

class Stack:
	def __init__(self):
        self.items = []   
    def pop(self):
        return self.items.pop()
    def peek(self): # 返回顶端元素
        return self.items[len(self.items) - 1]
    def push(self,item):
        return self.items.append(item)
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    
#反转列表的stack实现
#push 方法中使用insert替换pop
#栈的底端为列表的左端
```



栈的应用：

+   匹配括号

```python
from pythonds.basic import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False
```

+   进制转换

```python
from pythonds.basic import Stack

def divideBy2(decNumber):
    remstack = Stack()
    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2
    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())
    return binString

```





### **队列** 

```python

class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.items == []
```







### **双端队列** 

```python
class Deque:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def addFront(self,item):
        self.items.append(item)
    def addRear(self,item):
        self.items.insert(0,item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
    
```







### **链表**



**无序列表**



#### 节点实现

```python
#Node 类
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newdata):
        self.data = newdata
    def setNext(self,newnext):
        self.next = newnext
 
class Unorderedlist:
	def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head = None
    def add(self,item):
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
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return fonud
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
```













