'''
Intersect_Three
Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.

Input
The first line denotes n1, the size of the arr1. The next n1 lines denotes the n elements of the arr1.

The next line denotes n2, the size of the arr2. The next n2 lines denotes the n elements of the arr2.

The next line denotes n3, the size of the arr3. The next n3 lines denotes the n elements of the arr3.

Output
n lines, Each line containing 1 element of the resultant array.

Example
Input:

3

1

2

3

2

1

2

1

1

Output:

1

Explanation:
Only 1 appeared in the three arrays.

Note:
1 <= arr1.length, arr2.length, arr3.length <= 1000
1 <= arr1[i], arr2[i], arr3[i] <= 2000
Return [-1] if there is nothing common in all three arrays
'''
'''from collections import Counter
def intersect(a1,a2,a3):
    arr=[]
    d1=Counter(a1)
    d2=Counter(a2)
    d3=Counter(a3)
    for i in d1:
        if i in d2:
            if d2[i]<=d1[i]:
                d1[i]=d2[i]
        else:
            d1[i]=-1
    
    for i in d1:
        if i in d3:
            if d3[i]<=d1[i]:
                d1[i]=d3[i]
        else:
            d1[i]=-1
    for i in d1:
        if d1[i]>0:
            r=d1[i]
            arr.append((str(i)+"\n")*r)
    if arr:
        return arr
    else:
        return[-1]




a1=[int(input()) for _ in range(int(input()))]
a2=[int(input()) for _ in range(int(input()))]
a3=[int(input()) for _ in range(int(input()))]
print(intersect(a1,a2,a3))
'''
from collections import Counter
def intersect(a1,a2,a3):
    arr=[]
    d1=Counter(a1)
    d2=Counter(a2)
    d3=Counter(a3)
    for i in d1:
        if i in d2:
            if d2[i]<d1[i]:
                d1[i]=d2[i]
        else:
            d1[i]=-1
    
    for i in d1:
        if i in d3:
            if d3[i]<d1[i]:
                d1[i]=d3[i]
        else:
            d1[i]=-1
    for i in d1:
        if d1[i]>0:
            r=d1[i]
            arr.append((str(i)+"\n")*r)
    if arr:
        return arr
    else:
        return[-1]


a1=[int(input()) for _ in range(int(input()))]
a2=[int(input()) for _ in range(int(input()))]
a3=[int(input()) for _ in range(int(input()))]
result=intersect(a1,a2,a3)
[print(i,end="") for i in result]