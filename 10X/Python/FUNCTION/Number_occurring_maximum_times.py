'''
Number occurring maximum times
Given a list of N integers sorted in ascending order, Please find the number which occurs 4 times in the array

Input
First number is N (the number of integers given) Followed by the N numbers

Output
Print the number which occurs 4 times. print -1 if such a number doesnt exist

Example
Input: 10

1

2

3

4

4

4

4

5

6

6

Output: 4

'''
'''
def occurence_check(list):
    l=sorted(list)
    prev=l[0]
    ma=False
    count=0
    l2=0
    for i in range(0,len(l)):
        print(i)
        if (prev==l[i]):
            count+=1
            if(count==4):
               l2=prev
               ma=True
        else:
            prev=l[i+1]
            count=0
                                                     
    if ma:
        return l2
    else:
        return-1




if __name__ == "__main__":
    n=int(input())
    numbers = []
    for i in range(n):
        numbers.append(int(input()))
 
    print(occurence_check(numbers))

n=int(input())
s=[int(input()) for i in range(n)]
count=0
prev=s[0]
m=True
b=[]
for i in range(0,n):
    if (prev==s[i]):
        count+=1
        if count==4:
            print(s[i])
            m=False
    else:
        prev=s[i+1]
        count=0
    
if m:
    print(-1)

'''
n=int(input())
s=[int(input()) for i in range(n)]
arr=[]
count=0
prev=s[0]
m=0
for i in range(n):
    if (prev==s[i]):
        count+=1
        if(count==4):
            arr.append(s[i])
        m=max(m,count)
    else:
        prev=s[i]
        count=1    

if arr:
    for i in arr:
         print(i) 
else:
    print(-1)
    