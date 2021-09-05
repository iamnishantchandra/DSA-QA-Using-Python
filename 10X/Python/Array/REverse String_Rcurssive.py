"""
Reverse String: Recursive
Description
You are given a string. Write a function that reverses the string.

IMPORTANT
Your function should NOT use the following.

Loops (you can use a loop to read the test cases)
In-built functions like reverse
Input format
First line contains n, the number of test cases.
This is followed by n lines, each containing one input string.

Output format
n lines, each containing one string, which is the reverse of the corresponding input string.

Sample input
2
hello
winter
Sample output
olleh
retniw
Explanation
First line contains 2, meaning there are 2 test cases.
Reverse of hello is olleh. So first line of output is olleh.
Reverse of winter is retniw. So second line of output is retniw.

"""
"""
def reverse(s):
    n=len(s)-1
    if n==0:
        print(s[n])
        return n
    print(s[n],end="")
    reverse(s[:n])
input_NO=int(input())   
for i in range(input_NO):
    reverse(input())
"""
# def reverse(s):
    
#     if len(s)==1:
#         return s[len(s)-1]
#     else:
#         return (s[-1]+reverse(s[:len(s)-1]))
    
    
# input_NO=int(input())   
# for i in range(input_NO):
#     print (reverse(input()),end="")


#########################################


# def reverse(s):
#     n=len(s)-1
#     if n==0:
#         print(s[n])
#         return n
#     print(s[n],end="")
#     reverse(s[:n])
# input_NO=int(input())   
# for i in range(input_NO):
# 	reverse(input())
################################################
def reverse(s): 
    if s=="":
        return s
    else:
        return (s[-1]+reverse(s[:len(s)-1]))

input_NO=int(input())   
for i in range(1,input_NO+1):
    print (reverse(input()))