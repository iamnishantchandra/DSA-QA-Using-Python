'''
Alternate sort
You are given an array A, you have to sort the array such that all the even position are sorted in 
Decresing order and Odd position elements are sorted in increasing order. Odd and even positions are 
with respect to (0-based indexing). note-

DO NOT place an even index element at odd position or vice-versa

DO NOT use inbuilt sort function at any stage of the problem

Input
First line is T, denoting no, of arrays that follow. T lines follow containing the T arrays.

0<T<=200, 0< length of array<=2000, -10^5<A[i]<10^5

Output
Print all the arrays(on different lines) after performing the Alternate sort operations.

Example
Input: 2

1 2 3 4 5

-1 3 2 5 5 1

Output:

5 2 3 4 1

5 1 2 3 -1 5

Explanation first array has 1 2 3 4 5 where even index elements are 1 3 5 hence they are sorted in 
reverse order i.e 5 3 1 in final array and even index elements are 2 4 which are sorted in increasing 
order in final array giving 5 2 3 4 1.
'''
n=int(input())
for j in range(n):
    arr=[int(x) for x in input().split()]
    a=[]
    d=[]
    for i in range(len(arr)):
        if i%2==0:
            d.append(arr[i])
        else:
            a.append(arr[i])
    
    d.sort(reverse=True)
    a.sort()
           
    if len(arr)%2==0:
        arr=[]
        for i in range(len(a)):
            arr.append(d[i])
            arr.append(a[i])
    else:
        arr=[]
        for i in range(len(a)):
            arr.append(d[i])
            arr.append(a[i])
        arr.append(d[len(a)])
    for i in range(len(arr)-1):
        print(arr[i],end=" ")
    print(arr[len(arr)-1])



'''
n=int(input())
for j in range(n):
    ar=[]
    arr=[int(x) for x in input().split()]
    a=[]
    d=[]
    for i in range(len(arr)):
        if i%2==0:
            d.append(arr[i])
        else:
            a.append(arr[i])
    
    for i in range(len(d)):
        for j in range(len(d)):
            if d[i]>d[j]:
                d[j],d[i]=d[i],d[j]
       
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i]<a[j]:
                a[j],a[i]=a[i],a[j]
    ar=[]
    for i in range(len(a)):
        ar.append(d[i])
        ar.append(a[i])      
    if len(arr)%2==0:
        pass
    else:
        ar.append(d[len(a)])
    print(ar)
      
'''
"""

"""