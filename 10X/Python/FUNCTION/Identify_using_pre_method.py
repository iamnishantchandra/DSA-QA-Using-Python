'''
Identify_Alphabet
You have been given a string s. You need to find the number of non-alphabetical charcters present in the given string.

Constraints
s can contain smallcase/capitalcase alphabets, numbers, special characters, and space.
Input
One string denoting s.

Output
One integer, denoting the result.

Example
Input1:

aba@ad#$123
Output1:

6
Explanation1:

Non alphabetical characters are: @,#,$,1,2,3

'''
s=list(input())
l=len(s)
count=0
for i in s:
    if i.isalpha():
        count+=1
print(l-count)