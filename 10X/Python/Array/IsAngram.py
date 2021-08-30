"""
IS Anagram
You are given two strings A and B, you have to check whether they are anagrams of one another. An anagram 
is a word that can be obtained by rearranging the characters of the initial word.

Note- DO NOT use the inbuilt sort function at any stage of the code

Input
First line contains the string A and second line contains the string B 1<=len(A),len(B)<=2000

Output
Print "1" if they are anagrams and print "0" if they are not anagrams

Example
Input:

ABABCD

AABBCD

Output:

1

explanation

Since ABABCD can be rearranged to get AABBCD we print "1" as output
"""
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
    if sorted(d1)==sorted(d2):
        print(1)
    else:
        print(0)
else:
    print(0)

'''
#######################################
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
    #if sorted(d1)==sorted(d2):
    if d1==d2:
        print(d1)
        print(d2)
        print(1)
    else:
        print(0)
else:
        print(0)

