'''
Remove Spaces
Given a string, remove spaces from it.

Input
One line denoting the input string.

Output
One line, denoting the resultant string.

Example
Input:

Love for cricket
Output:

Loveforcricket

'''
#print(input().replace(" ",""))

print("".join(map(str,input().split())))