'''
Find Hello
You are given a string. You are supposed to find if "hello" exists in the given string as a substring. See explanation for better understanding. If "hello" exists print "Yes" else print "No".

Note: length of string is greater than 0.

Input
First line contains n number of strings for which you need to check. After this n lines will follow. Each containing a string.

Output
Print "Yes" or "No".

Input:

2

Academy

ramhellolaxman

Output:

No

Yes

Explanation
Testcase 1: There is no hello in the word Academy.

Testcase 2: hello starts at index 3 and ends at 7.
'''
'''
def Finding_Hello(s):
    l=len(s)
    w="hello"
    f=False
    for i in range(0,(len(s)-4)):
        if w==s[i:i+5]:
            return True
    return f

for _ in range(int(input())):
    print(Finding_Hello(input()))

'''
def Finding_Hello(s,target):
    if target in s:
        return "Yes"
    else:
        return "No"
target="hello"
for _ in range(int(input())):
    print(Finding_Hello(input(),target))