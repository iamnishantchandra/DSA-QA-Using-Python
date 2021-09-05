'''
Socks
You have n socks in the cupboard as a large pile of socks that must be paired by color. Given an array of 
integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

Input Format
The first line contains an integer n, the number of socks represented in arr. The second line contains n 
space-separated integers, arr[i], the colors of the socks in the pile.

Output Format
A single integer denoting the number of pairs.

Sample Input
9
10 20 20 10 10 30 50 10 20
Sample Output
3
'''
n=int(input())
ar=[int(x) for x in input().split()]
d={}
count=0
for i in ar:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in d:
    count+=d[i]//2
print(count)