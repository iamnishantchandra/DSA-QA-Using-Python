'''
Recursive Sequence
A function f is defined as follows F(n)= (1) +(2x3) + (4x5x6) ... n. Given an integer n the task is to print the F(n)th term.

Problem Constraints:
1 <= T <= 10
1 <= N <= 10
Input
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test contains an integer n.

Output
T lines, each line should contain an integer F(n).

Example
Input:

4

1

2

5

7

Output:

1

7

365527

6006997207

Explanation:
F(5) = 1+(2x3)+(4x5x6)+(7x8x9x10)+(11x12x13x14x15) = 365527
'''
def recurssive(n):
    if n==1:
        return 1
    sp=((n-1)*(n-1+1)//2)+1
    ep=sp+n
    mult=1
    for i in range(sp,ep):
        mult*=i

    return recurssive(n-1)+mult
for _ in range(int(input())):
    print(recurssive(int(input())))
