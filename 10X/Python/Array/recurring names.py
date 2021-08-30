"""
Recurring Names
We are given a list of names in a town and a number k. Find all the names which has occured more than k times.

Names are case Sensitive.

Input format
First lines contains k.

Second line contains names of people in the town. Names are separated by a space.

Output format
N lines, each line containing a name which has occured more than k times.

Print the names in the alphabetical order.

If no such names exists, print exactly no such names in this town!!!

Sample input
2

hughie homelander noir maeve hughie noir a-train stormfornt hughie noir a-train A-train

Sample output
hughie

noir

Explanation
hughie and noir has occured 3 times which is more than given k = 2.

"""
n=int(input())
arr=list(input().split())
n1={}
f=True
for i in arr:
        if i in n1:
            n1[i]+=1
        else:
            n1[i]=1
for i in sorted(n1):
    if n1[i]>n:
        print(i)
        f=False
if f:
	print("no such names in this town!!!")
