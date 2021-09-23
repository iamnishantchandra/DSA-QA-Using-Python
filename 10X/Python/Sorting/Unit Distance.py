'''
unit-distance
Description
Check if edit distance between two strings is one or not. If its one, print True else False. Number of 
edits done to the string a to get string b is called the edit distance.

An edit between two strings is one of the following changes:

- Add a character
- Delete a character
- Change a character
Note:
The strings are case sensitive, and they may also contain symbols or numbers.
Input format
First line denotes t, denoting the number of testcases. Each test case contains two space seperated strings
 in one line.

Output format
One line for each test case.

Sample input
2
peaks peeks
bbbbb bbbbb
Sample output
True
False
Explanation
Number of edits in first case is 1, hence True. (The edit is to change the 3rd character of first string 'a' to 'e', or vice versa)
Number of edits in first case is 0, hence False.

'''
"""
def check(x,y):
    
    if len(x)-len(y)>1 or len(y)-len(x)>1 or x==y:
        return False
    else:
        count=0
        if len(x)== len(y):
            for i in range(len(x)):
                if x[i]==y[i]:
                    count+=1
            if count==len(x)-1:
                return True
            else:
                return False
        elif len(x)-len(y)==1:
            count=0
            for i in range(len(y)):
                if x[i]!=y[i]:
                    count+=1
            if count>1:
                return False
            else:
                return True
        elif len(y)-len(x)==1:
            count=0
            for i in range(len(x)):
                if x[i]!=y[i]:
                    count+=1
            if count>1:
                return False
            else:
                return True
            


    # count=0
    # n= len(x) if len(x) >=len(y) else len(y)
    # print(n)
for _ in range(int(input())):
    x,y=input().split()
    print(check(x,y))
"""
'''
def isEditDistanceOne(string1, string2): 
    # Complete this function, and return True/False

for _ in range(int(input())):
    input_string1, input_string2 = input().split()
    print(isEditDistanceOne(input_string1, input_string2))
'''

def check(x,y):
    if len(x)-len(y)>1 or len(y)-len(x)>1 or x==y:
        return False
    else:
        count=0
        if len(x)== len(y):
            for i in range(len(x)):
                if x[i]==y[i]:
                    count+=1
            if count==len(x)-1:
                return True
            return False
        elif len(x)-len(y)==1:
            j=0
            for i in range(len(y)):
                if y[j]!=x[i]:
                    count+=1
                    j-=1
                if count>2:
                    return False
                j+=1
            return True
        elif len(y)-len(x)==1:
            j=0
            for i in range(len(x)):
                if x[j]!=y[i]:
                    count+=1
                    j-=1
                if count>2:
                    return False
                j+=1
            return True
for _ in range(int(input())):
    x,y=input().split()
    print(check(x,y))