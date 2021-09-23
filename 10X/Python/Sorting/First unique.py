'''
First Unique
Description
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, 
return -1.

Note: A non repeating character is the one that occcurs only one time.

Input
First line of each input contains an integer T denoting the number of test cases.

First line of each test case contains a string .

Output
For each test case print the index of first non-repeating character or else return -1 if no non-repeating 
character exists.

Example
Input:

2

abc

aa

Output:

0

-1

Explanation
In first test case, 'a' is the first non repeating character and its index is 0.

In second test case, 'a' occurs 2 times thus only repeating character exists hence answer is -1.


'''
def check(n):
    d={}
    for i in range(len(n)):
        if n[i] in d:
            d[n[i]]+=1
        else:
            d[n[i]]=1
    for i in range(len(n)):
        if n[i] in d and d[n[i]]==1:
            return i
    return -1
            
for _ in range(int(input())):
    n=input()
    print(check(n))