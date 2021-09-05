'''
Recursive Multiply
You have been given an integer n. You need to print all the multiplication of all the digits of the n using recursion.

Note: DO NOT USE LOOP/s
Input
First line contains one integer t, denoting number of testcases. Its is followed t lines:

Each line contains one integer denoting n.
Output
One line for each testcase, denoting the result.

Example
Input:

2
12345
356045873
Output:

120
0

'''
def remultiply(n):
    if(n>=0 and n<10):
        return n
    rem = n%10
    n = n//10
    return rem * remultiply(n)
for _ in range(int(input())):
    n=int(input())
    if n<0:
        print(remultiply(n*-1))
    else:
        print(remultiply(n))