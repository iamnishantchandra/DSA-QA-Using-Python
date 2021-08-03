'''
College
Everyone is missing college these days. So the college admin has decided a digital reunion.

Just as a fun event, everyone is asked to find the sum of the divisors of your roll number (given).

Complete the given function to compute and return the sum of the divisors of the integer n.

Input
One integer, denoting n.

Output
One Integer, denoting the result.

Example
Input1:

15
Output1:

21
Explanation1:

Divisors of 15 are 1,3,5,15.

So, 1 + 3 + 5 + 15 = 24

'''

def sumofdivisors(n):
    # Code here
    sum=0
    for i in range(1,n+1):
        if n%i==0:
            sum+=i
    return sum
    

n = int(input())
print(sumofdivisors(n))