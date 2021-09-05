"""
Increasing Subarr
Given an array containing n numbers. The problem is to find the length of the longest contiguous subarray 
such that every element in the subarray is strictly greater than its previous element in the same subarray 
and also print the resulting starting and ending index. Array is 1 index based.

Input
Fisrt line has N i.e number of elements then follow N numbers in a line.(N >= 2)

Output
Print a list of 3 elements where the first one is the length of the subarray and the next 2 are the 
starting and the ending index Note : all elements of the list must be printed in the same line.

Example
Input:

3

2 3 1

Output:

2 1 2

The longest Increasing subarray is [2, 3] and the starting index is[1 , 2]

"""
"""def count(a):
    n=len(a)
    c=1
    s=0
    e=0
    cm=1
    sf=1
    ef=1
    ar=[]

    for i in range(1,n):
        if a[i-1]<a[i]:
            c+=1
            e=i
            if c>cm:
                # cm=c
                # sf=s
                # ef=e
                ar[0]=c
                ar[1]=s+1
                ar[2]=e+1
                
        else:
                c=1
                s=i
                e=i
    # ar.append(cm)
    # ar.append(sf+1)
    # ar.append(ef+1)
    return ar

for _ in range(int(input())):
    arr=[int(x) for x in input().split()]
    print(*count(arr))

"""
def count(a):
    n=len(a)
    c=1
    s=1
    e=1
    ar=[1,1,1]
    for i in range(1,n):
        if a[i-1]<a[i]:
            c+=1
            e=i+1
        else:
                c=1
                s=i+1
                e=i+1
        if c>ar[0]:
                ar[0]=c
                ar[1]=s
                ar[2]=e
    return ar

n=(int(input()))
arr=[int(x) for x in input().split()]
print(*count(arr))

