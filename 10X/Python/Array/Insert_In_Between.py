"""
Insert in Between
You have been given a sorted array arr and one integer x. You need to insert x into the given array, 
such that the array still remains sorted.

Input
Two space seperated values, denoting n and x respectively. One line containing n space seperated values, 
denoting the elements of the array.

Output
Resultant array.

Example
Input1:

5 3
1 2 3 4 5
Output1:

1 2 3 3 4 5

"""
x,n=map(int,input().split())
ar=list(map(int,input().split()))
ar.append(n)
i=len(ar)-1
while(i>0)and ar[i-1]>ar[i]:
    ar[i],ar[i-1]=ar[i-1],ar[i]
    i-=1
[print(x,end=" ") for x in ar]