'''
TREK
You went on a trek with HEC(Himalayan Explorers' Club). The trek was to a very beautiful place known as 
Valley of Flowers'.

For each step you took on the trek, you noted it down as U for Upward and D as Downward. (

Assume, these are the only two possible types of steps possible on the trek.
Trek/Hike always start and end at sea level, and each step up or down represents a unit change in altitude.
A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and 
ending with a step down to sea level.
A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and 
ending with a step up to sea level.
Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.

Input Format
First line denotes the number of testcases. For each testcase:

First line denotes the number of steps, N.
The next line contains a string of length N containing only U and D.
Output Format
For each testcase, print the number of valleys walked through in a new line.

Sammple Input
1
8
UDDDUDUU
Sample Output
1
Explanation
If we represent _ as sea level, a step up as /, and a step down as \, the hike can be drawn as:

_/\      _
   \    /
    \/\/

The hiker enters and leaves one valley.

'''
def trek(s):
    su=0
    c=0
    for i in range(len(s)):
        if s[i]=="U":
            su+=1
        elif s[i]=="D":
            su-=1
        if su==0 and s[i]=="U":
            c+=1
    return c

for _ in range(int(input())):
    n=int(input())
    s=input()
    print(trek(s))