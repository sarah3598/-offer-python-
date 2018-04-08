# -- coding: utf-8 --
# 面试题3
import numpy as np
a=np.array([[1,2,3],[4,5,6],[8,7,3],[6,4,9]])
test1=0
test2=9
test3=18
test4=''
# print len(array[0])
def find(array, target):
    row = len(array) - 1
    col = len(array[0]) - 1
    i = row
    j = 0
    while i >= 0 and j <= col:
        if array[i][j] > target:
            i -= 1
        elif array[i][j] < target:
            j += 1
        else:
            return True
    return False

print find(a,test1)
print find(a,test2)
print find(a,test3)
print find(a,test4)
