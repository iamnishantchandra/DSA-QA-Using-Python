'''
Bulb
There is a bulb. Just like other bulbs, this bulb can be either ON or OFF at a time. You can provide 3 types of instruction to the bulb-

"ON"-> turn the bulb on.(no matter the previous state)
"OFF"-> turn the bulb off.(no matter the previous state)
"Toggle"-> If the bulb was initially on, turn it off. If the bulb was initially off, turn it on.
You provide the bulb with 'N' number of Queries, each containing either of the above 3 instructions. Count the number of times bulb was turned ON from a OFF position.(ON->OFF)

Note- Intially assume that the bulb was OFF.

Input
First line of the input contains N, representing the number of instructions. The following N lines contain one of the 3 types of instructions "ON","OFF","Toggle".

Output
Finally print the number of times the bulb was turned ON from a OFF position.

Example
Input:

5

Toggle

Toggle

OFF

Toggle

ON

Output:

2

Explanation:

Intially : OFF

| BEFORE | INSTRUCTION | RESULT |
------------------------------------
| OFF        | TOGGLE           | ON |
| ON          | TOGGLE           |OFF|
| OFF        | OFF                  | OFF |
| OFF        | TOGGLE           | ON |
| ON          | ON                   | ON |
As we can see that the bulb has been switched from OFF to ON 2 times once during the first(TOGGLE) instruction and then during the 4th(TOGGLE) instruction. So the output is 2
'''
'''
n=int(input())
a=[]
for i in range(n):
    a.append(input())
b=0
count=0
for j in range(n):
    if a[i]=="Toggle":
        if b==0:
            b=1
            count+=1
        else:
            b=0
    elif a[i]=="ON":
        if b==0:
            b=1
            count+=1
        else:
            b=1
    elif a[i]=="OFF":
            b=0
print(count)
'''
n=int(input())
a=[]
for j in range(n):
    a.append(input())
b=0
count=0
for i in range(n):
    if b==0 :
        if a[i]=="Toggle" or a[i]=="ON":
            b=1
            count+=1
        else:
            b=1
    elif b==1:
        if(a[i]=="Toggle") or (a[i]=="OFF") :
            b=0
        else:
            b=1
print(count)

