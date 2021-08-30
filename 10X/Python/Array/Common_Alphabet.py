'''
Common Alphabets
Given list of strings. The task is to find the frequency of the elements which are common in all strings 
given in the list of strings.

Input:
First line contains N, number of strings.

Next N lines contians a string in each line.

Output:
N linese each line contains an alphabet and it's frequency in sorted order for each of the input string.

alphabet and the frequency are separated by a space

Problem Constraints:
1<=A.length<=500

1<=A[0].length<=100

Examples:
Input :

3

gefgek

gfgk

kinfgg

Output :

f 1

g 2

k 1

Explanation :
f occurs once in all Strings.

g occurs twice in all the strings.

k occurs once in all string.

Output is in ascending order

'''
from typing import Counter
n=int(input())
arr=[]
for i in range(n):
    arr.append(input())
dic=Counter(arr[0])
for i in range(1,n):
    d=Counter(arr[i])
    for i in dic:
        if d[i]==0:
            dic[i]=-1
        else:
            dic[i]=min(dic[i],d[i])
for i in sorted(dic):
    if(dic[i]>0):
        print(i+" "+str(dic[i]))

