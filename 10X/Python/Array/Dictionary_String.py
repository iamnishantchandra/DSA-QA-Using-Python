'''
Dictionary String
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by 
deleting some characters of the given string. You have to print the length of the longest string only.

Input
First line of input contains the String. Second line of the input contains the Dictionary of strings that 
need to be found in the String.

Output
Print the length of the longest string in the dictionary which can be made by deleting the characters in 
the main String

Constraints
The size of the dictionary won't exceed 1,000.

The length of all the strings in the input won't exceed 1,000.

Example
Input:

abcdabcdpple

apple bad desk banana me this that a abc abcd pple

Output:

5

Explanation
the words apple, bad, a, abc, abcd, pple can be made from the main string. The longest among these is 
"apple" with length=5
'''
'''
from collections import Counter
s=input()
stri=list(input().split())
d={}
ma=0
count=0
st=""
a=[]
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in range(len(stri)):
    a=Counter(stri[i])
    for j in a:
        if (j in d )and (a[j]<=d[j]) and count!=-1:
           count+=a[j]
        else:
            count=-1
    if count>ma:
        ma=count
        st=a
    count=0  
print(ma)
# print(str(ma)+" "+st)
'''
"""
# your code goes here
from collections import Counter
s=input()
stri=list(input().split())
d={}
ma=0
count=0
st=""
a=[]
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in range(len(stri)):
    a=Counter(stri[i])
    for j in a:
        if (j in d )and (a[j]<=d[j]) and count!=-1:
           count+=a[j]
        else:
            count=-1
    if count>ma:
        ma=count
        st=a
    count=0  
print(ma)

"""
s=input()
stri=list(input().split())
ma=0
count=0
st=""
a=[]
for j in stri:
    if len(j)<=len(s):
        k=0
        i=0
        while i<len(s) and k<len(j):
            if s[i]==j[k]:
                k+=1
                count+=1
                i+=1
            else:
                i+=1
    if count==len(j) and ma<count:
        ma=count
        st=j
    count=0
print(ma)
# print(str(ma)+" "+st)