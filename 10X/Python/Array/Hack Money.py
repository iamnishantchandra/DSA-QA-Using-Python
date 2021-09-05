'''
Hack Money
Description
You are a bank account hacker. Initially you have 1 rupee in your account, and you want exactly N rupees 
in your account. You wrote two hacks, First hack can multiply the amount of money you own by 10, while the 
second can multiply it by 20. These hacks can be used any number of time . Can you achieve the desired 
amount N using these hacks.

Input
The first line of the input contains a single integer T denoting the number of test cases.

The description of T test cases follows.The first and only line of each test case contains a single integer N.

Output
For each test case, print a single line containing the string "Yes" if you can make exactly N rupees or "No" otherwise.

Example
Input:

5

1

2

10

25

200

Output:

Yes

No

Yes

No

Yes

Explanation
In the 5th case hacker can get Rs. 200 by first using 10x hack and using 20x hack.

'''
def hackm(n):
    if n==0:
        return False
    if n==1:
        return True
    if n%10==0 and n%20==0:
        return hackm(n//10) or hackm(n//20)
    elif n%10==0:
        return hackm(n//10)
    elif n%20==0:
        return hackm(n//20)
    else:
        return False
for i in range (int(input())):
    print("Yes"if hackm(int(input()))==True else "No")
    