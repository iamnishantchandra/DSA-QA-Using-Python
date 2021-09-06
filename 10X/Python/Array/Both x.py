'''
both-x
Description
Given two strings (string1 and string2) and a number x, return a list of all the characters that appear 
exactly x times in both the strings (in sorted order). Ignoring the case.

Input format
First line denotes t, denoting the number of testcases. Each test case contains 3 space seperated elements 
in one line, denoting string1 , string2 and x respectively.

Output format
One line for each test case.

Sample input
1
Sample Pampe 1
Sample output
a e m
Explanation
a, m, e (all the 3 chars appear exactly once in both the strings).
'''
"""for _ in range(int(input())):
    x,y,no=map(str,input().split())
    no=int(no)
    print(count)
print(x,y,no)
for i in string1:
        if string1[i] in s1 and string1[i] in s2:
            s3[string1[i]]=min(s1[string1[i]],s2[string2[i]])
    for i in s3:
"""
def bothCountX(string1, string2, x):
    # Complete this function, and return the list of resultant characters in sorted order
    s1={}
    s2={}
    s3={}
    a=[]
    string1=string1.casefold()
    string2=string2.casefold()
    for i in range(len(string1)):
        if string1[i] in s1:
            s1[string1[i]]+=1
        else:
            s1[string1[i]]=1
    for i in range(len(string2)):
        if string2[i] in s2:
            s2[string2[i]]+=1
        else:
            s2[string2[i]]=1
    
    for i in s1:
        if i in s1 and i in s2 and s1[i]==x and s2[i]==x:
            a.append(i)
    #         s3[i]=min(s1[i],s2[i])
    # for i in s3:
    #     if s3[i]==x:
    #         a.append(i)
    b=sorted(a)
    return(b)


for _ in range(int(input())):
    string1, string2, x = input().split()
    x = int(x)
    print(*bothCountX(string1, string2, x))