

## 冒泡排序



```python
def bubbleSort(alist):
    for i in range(len(alist)):
        for j in range(0,len(alist)-i-1):
            if alist[j] > alist[j+1]:
                alist[j+1],alist[j] = alist[j],alist[j+1]
    return alist
# 优化后，如果没有一次交换，则已经有序，不再进行遍历
def bubbleSort(alist):
    for i in range(len(alist)):
        flag = False
        for j in range(0,len(alist)-i-1):
            if alist[i] > alist[j+1]:
                alist[j+1],alist[j] = alist[j],alist[j+1]
                flag = True
        if flag is False:
            return alist

```



## 选择排序

```python
def selectionSort(alist):
	for i in range(len(alist)):
		mid = i
        for j in range(i+1,len(alist)):
            mid = j
        alist[i],alist[mid] = alist[mid],alist[i]
    return alist

# 方法2
def selectionSort(alist):
    for i in range(len(alist)):
        for j in range(len(alist)-i):
            if alist[i] > alist[i+j]:
				alist[i],alist[i+j] = alist[i+j],alist[i]
    return alist

```



## 快速排序

1.  先从数列中取出一个数作为基准数。
1.  分区过程，将比这个数大的数全放到它的右边，小于或等于它的数全放到它的左边。
1.  再对左右区间重复第二步，直到各区间只有一个数。

```python
# 快排 分片的思想+递归的思想，这是取了第一个为基准值，栈高为O(log(n)),栈长O(n),所以运行时间为栈高x栈长，也就是算法平均运算时间为O(nlog(n))
def quickSort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i < pivot]
        greater = [j for j in array[1:] if j >= pivot]
        return quickSort(less) + [pivot] + quickSort(greater)
```





## 插入排序

































