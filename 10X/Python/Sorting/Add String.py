'''
Add Strings
Description
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.

Both num1 and num2 contains only digits 0-9.

Both num1 and num2 does not contain any leading zero.

You MUST NOT convert the inputs to integer directly.

Complete the addStrings function. It takes the input as two strings & you need to return the string (which will same as the addition of two number as integers).

'''
########################################################################
# Complete this addStrings() function
# converting string into list and then adiition as 
"""
def digit(d):
    if d=="0":
        return 0
    elif d=="1":
        return 1
    elif d=="2":
        return 2
    elif d=="3":
        return 3
    elif d=="4":
        return 4
    elif d=="5":
        return 5
    elif d=="6":
        return 6
    elif d=="7":
        return 7
    elif d=="8":
        return 8
    elif d=="9":
        return 9
def addStrings(num1, num2):     
    ### Here num1 & num2 are strings [Return the addition of these two strings as string]
    a1=[]
    a2=["0"]
    a=""
    no=0
    if len(num1)>=len(num2):
        a1=["0"]*len(num1)
        a2=["0"]*len(num1)
    elif len(num2)>len(num1):
        a1=["0"]*len(num2)
        a2=["0"]*len(num2)
    for i in range(len(num1)):
        a1[len(a1)-1-i]=num1[len(num1)-1-i]
    for i in range(len(num2)):
        a2[len(a2)-1-i]=num2[len(num2)-1-i]

    c=0#carry

    for i in range(len(a1)):
        n=digit(a1[len(a1)-1-i])+digit(a2[len(a2)-1-i])+c
        if n==10:
            c=1
            n-=10
        elif n>10:
            c=1
            n-=10
        else:
            c=0
        a+=str(n)
        no+=n*(10**i)
    if c==1:
        a+=str(c)
        no+=c*(10**len(a1))
    b=a[::-1]#String Formate
    print(b)
    return no
## Do not change anything below this line:

for _ in range(int(input())):
    n1, n2 = input().split()
    print(addStrings(n1,n2))

"""

def digit(d):
    if d=="0":
        return 0
    elif d=="1":
        return 1
    elif d=="2":
        return 2
    elif d=="3":
        return 3
    elif d=="4":
        return 4
    elif d=="5":
        return 5
    elif d=="6":
        return 6
    elif d=="7":
        return 7
    elif d=="8":
        return 8
    elif d=="9":
        return 9
def addStrings(num1, num2):     
    ### Here num1 & num2 are strings [Return the addition of these two strings as string]
    a1=[]
    a2=[]
    no=0
    if len(num1)>=len(num2):
        a1=["0"]*len(num1)
        a2=["0"]*len(num1)
    elif len(num2)>len(num1):
        a1=["0"]*len(num2)
        a2=["0"]*len(num2)
    for i in range(len(num1)):
        a1[len(a1)-1-i]=num1[len(num1)-1-i]
    for i in range(len(num2)):
        a2[len(a2)-1-i]=num2[len(num2)-1-i]

    c=0#carry

    for i in range(len(a1)):
        n=digit(a1[len(a1)-1-i])+digit(a2[len(a2)-1-i])+c
        if n==10:
            c=1
            n-=10
        elif n>10:
            c=1
            n-=10
        else:
            c=0
        no+=n*(10**i)
    if c==1:
        no+=c*(10**len(a1))
    return no
## Do not change anything below this line:
for _ in range(int(input())):
    n1, n2 = input().split()
    print(addStrings(n1,n2))

####               83%               ####

