#!/usr/bin/python3
# encoding = utf-8
# tested on ubuntu
# 冒泡排序
# date: 0610-3-09:09

def bubbleSort(relist):
    len_list = len(relist) # 计算列表长度
    for i in range(len_list):  # 遍历列表长度
        print("第 %s 趟排序"%(i+1))  
        for j in range(0,len_list-i-1): # range = start: 0, end: length of list - i -1 
            if relist[j] > relist[j+1]: # if left value > right value, then exchange left and right
                relist[j+1], relist[j] = relist[j], relist[j+1] # use of python example: a,b = b,a. a = relist[j+1],b = relist[1]
    #return relist
    print(relist)

# 如果在其他语言中，则需要使用节点交换值在进行三次重新赋值，
# 但在python中可以同时赋值，因此以上代码省略了三次赋值
'''
def bubbleSort(alist):
	for j in range(len(alist))-1,0,-1):
		for i in range(j):
			if alist[i] > alist[i+1]:
				temp = alist[i]
				alist[i] = alist[i+1]
				alist[i+1] = temp
	return alist

'''
