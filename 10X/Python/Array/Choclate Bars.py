'''
Chocolate Bars
There are N chocolates denoted by array A where A[i] is the length of the i-th chocolate. Alice can 
melt each chocolate and then convert it into a chocolate whose length is any divisor of the number A[i].
So, a chocolate of length A[i] can be converted into X different types of chocolate where X is the count 
of divisors of the number A[i]. So you need to count the total unordered pair (i, j) of chocolates such 
that their X value is same.

Input
The first line contains an integer N as input denoting the total number of elements in the array A. 
The next line contains N space-separated integers that denote the elements of the array A.

Output
In the output, print the total number of ways as mentioned in the statement.

Example
Input:

3

2 3 4

Output:

1

Explanation
X values of each number .

A[1] = 2 , divisors of A[1] are 1, 2.Thus X value of A[1] is 2.

similarly, A[2] = 3, divisors of A[2] are 1, 3.Thus X value of A[2] is 2.

A[3] = 4, divisors of A[3] are 1, 2, 4. Thus X value of A[3] is 3.

Thus we have only one pair (1, 2) for which X value is 2.

'''
import math

def factor(n):
    count=0
    for i in range(1,1+int(math.sqrt(n))):
        if n%i==0:
            count+=1
            if n//i!=i:
                count+=1
    return count

def result(ar,n):
    d={}
    for i in ar:
        x=factor(i)
        if x in d:
            d[x]+=1
        else:
            d[x]=1
    res=0
    for x in d:
        res+=(d[x]*(d[x]-1))//2
    return res


n=int(input())
ar=[int(x) for x in input().split()]
print(result(ar,n))

# Help.....