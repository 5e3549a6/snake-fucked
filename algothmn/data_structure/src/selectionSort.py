#!/usr/bin/python3
# encoding = utf-8
# tested on ubuntu
# 选择排序
# date: 0610-3-09:09

def selectionSort(alist):
	for j in range(len(alist)-1,0,-1): 
		pm = 0
		for i in range(1,j+1):
			if alist[i] > alist[pm]:
				pm = i
		temp = alist[j]
		alist[j] = alist[pm]
		alist[pm] = temp

# 方法一
def selectSort(relist):
    len_list = len(relist) # length of list
    for i in range(len_list):
        min_index = i
        for j in range(i+1,len_list):  # 这个循环会找到值比第i个索引所代表值小的索引
            if relist[j] < relist[min_index]:
                min_index = j
        relist[i] ,relist[min_index] = relist[min_index], relist[i]  # 互换两个索引位置
    return relist

fn selectSort(alist: &[T,N])->[T,N] {
	let mut len_list:i32 = alist.len();
	for i in len_list.iter() {
		let min_index = &i;
		for j in &i+1..len_list {
			if alist[&i] < alist[min_index] {
				min_index = &j
				let alist[i] = &alist[min_index];
				let alist[min_index] = &alist[i];
			}
		}
	}
	&alist
}


# 方法二，更加简便，但是注意和冒泡法进行区分
def selectSort(relist):
    for i in range(len(relist)):
        for j in range(len(relist)-i):
            if relist[i] > relist[i+j]:
                relist[i],relist[i+j] = relist[i+j],relist[i]
    return relist
