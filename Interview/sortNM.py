# -*- coding:utf-8 -*-
# 有一个数组长度为n，数组中每个元素的值的范围是1<=x<=m，其中n是大于m的
# 要求排序时间复杂度O(n)，空间复杂度O(1)


def replace(arr, index):
    if index >= len(arr):
        return
    cur = arr[index]
    if arr[index] > 0:
        arr[index] = -1
        replace(arr, cur)
    else:
        arr[index] -= 1
        return


# n大于m的表示数组中肯定有重复元素
def sort(arr):
    length = len(arr)
    for i in range(length):
        if arr[i] > 0:
            cur = arr[i]
            arr[i] = 0
            replace(arr, cur)
    end = length
    for x in reversed(range(length)):
        if arr[x] < 0:
            start = end - abs(arr[x])
            for y in range(start, end):
                arr[y] = x
            end = start
    print arr


test = [2, 3, 1, 1]
test1 = [3, 1, 4, 2, 5, 2, 1, 3, 1]
test2 = [1, 1, 1, 1]
sort(test)