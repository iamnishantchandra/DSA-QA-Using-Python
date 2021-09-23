'''
Scoring Exam
Milly is at the examination hall where she is reading a question paper. She checked the question paper and discovered that there are N questions in that paper. Each question has some score value. Ideally it's like questions requiring more time have more score value and strangely no two questions on the paper require same time to be solved.

She is very excited by looking these questions. She decided to solve K questions while maximizing their score value. Could you please help Milly to determine the exact time she needs to solve the questions.

Input
First line of input contains two space separated integers N and Q, where N is the number of questions available and Q is number of queries

Next line contains N space separated integers denoting the time Ti of N questions

Next line contains N space separated integers denoting the scores Si of N questions

Next Q lines contains a number K each, the number of questions she wants to solve

Output
Print the time required for each query in a separate line.

Example
Input:

5 2

2 3 9 4 5

3 5 11 6 7

5

3

Output:

23

18

'''
"""
x,y=map(int,input().split())
ti=[int(x) for x in input().split()]
mar=[int(x) for x in input().split()]
d={}
for i in range(len(mar)):
    if mar[i] in d:
        d[mar[i]]=ti[i]
    else:
        d[mar[i]]=ti[i]
mar.sort(reverse=True)
for j in range(y):
    time=0
    n=int(input())
    for i in range(n):
        if mar[i] in d:
            time+=d[mar[i]]
    print(time)

"""
x,y=map(int,input().split())
ti=[int(x) for x in input().split()]
mar=[int(x) for x in input().split()]
d={}
for i in range(len(mar)):
    if mar[i] in d:
        d[mar[i]]=ti[i]
    else:
        d[mar[i]]=ti[i]
newt=[]       
mar.sort(reverse=True)

for i in range(len(mar)):
    if mar[i] in d:
            newt.append(d[mar[i]])

tsum=[]
tsum[0]=newt[0]
for i in range(1,len(newt)):
    tsum[i]=tsum[i-1]+tsum[i]
for i in range(y):
    n=int(input())
    print(tsum[n])
