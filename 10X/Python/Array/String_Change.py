'''
String change
Given 2 string check if the first can be rearrange to get the 2nd one. If it is possible print 1 else 
Print 0.

Input
First line : String 1

Second Line: String 2

Output
Print 1 or 0 depending on the condition satisfied

Example
Input:

"abc"

"cab"

Output:

1
'''
s1=input()
s2=input()
d1={}
d2={}
if len(s1)==len(s2):
    for i in range(len(s1)):
        j=s1[i]
        if j in d1:
            d1[j]+=1
        else:
            d1[j]=1
    for i in range(len(s2)):
        j=s2[i]
        if j in d2:
            d2[j]+=1
        else:
            d2[j]=1
    if d1==d2:
        print(1)
    else:
        print(0)
else:
        print(0)