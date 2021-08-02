'''

Len of Longest Word
Given a string S, find the length of the longest word in the string. The words are separated by Spaces. 
If no such word exists, print 0

Input
one line containing the String S

Output
one line containing the length of the longest word in the String S

Example
Input: hello world

Output: 5 - because both words are of length 5

Input: helloooooo world

Output: 10 - because "helloooooo" is of length 10
'''
s=input().split()
count=0
max=0
f=False
for i in range(len(s)):
    count=len(s[i])
    if(count>max):
        max=count
        
        f=True
if f:
    print(max)
else:
    print(0)