'''
Counting Stars
One day Professor Xavier saw alphabets appearing on the stars. He was so fascinated by them that he started making a list of numbers and for every new star, he inserted a number X into the list. This X is equal to the no. of times the alphabet on the current star has previously appeared.

After seeing N stars, he decided to stop and calculate the sum of all the N numbers.

Professor Xavier has spent all his life watching stars and do not know how to add. Can you help him in finding the sum?

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.

The first line contains a single integer – N, denoting the number of stars.

The next line contains a string S of length N, describing the characters that appeared on the N stars sequentially.

Output
For each query, print a single line containing one integer – the sum of all the N numbers.

Example
Input: 1

5

abaab

Output:

4

Explanation
There are 5 stars.

The list (say L) is initially empty. L = {}.

The 1st star had alphabet ‘a’ on it. Since ‘a’ has not appeared previously, 0 is inserted in the list. L = {0}.

The 2nd star had alphabet ‘b’ on it. Since ‘b’ has not appeared previously, 0 is inserted in the list. L = {0, 0}.

The 3rd star had alphabet ‘a’ on it. Since ‘a’ has previously appeared 1 time, 1 is inserted in the list. L = {0, 0, 1}.

The 4th star had alphabet ‘a’ on it. Since ‘a’ has previously appeared 2 times, 2 is inserted in the list. L = {0, 0, 1, 2}.

The 5th star had alphabet ‘b’ on it. Since ‘b’ has previously appeared 1 time, 1 is inserted in the list. L = {0, 0, 1, 2, 1}.

Sum of all elements in L = 4.
'''
def countStar(s,n):
    d={}
    l=[]
    for i in range(n):
        if s[i] in d:
            d[s[i]]+=1
            l.append(d[s[i]])
        else:
            d[s[i]]=0
            l.append(d[s[i]])
        
    return sum(l)

tc=int(input())
for _ in range(tc):
    n=int(input())
    s=input()
    print(countStar(s,n))


