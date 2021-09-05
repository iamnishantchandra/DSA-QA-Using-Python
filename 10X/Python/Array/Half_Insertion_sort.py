'''
Half Insertion
You have been given a string containing numbers, alphabets and special characters. You only need to sort the secoond half of the string using Insertion sort. (If the length of the string is odd, consider the middle character as the part of the second half as well.)

Input
One string

Output
Resultant string, with first half unsorted & second half sorted.

Example
Input1:

adcbe
Output1:

adbce
'''
def stringInsertionSort(str):
    # Your code goes here
    
    a=[]
    for i in range(len(str)):
        a.append(ord(str[i]))
    # a.sort()
    b=(len(a)//2)
    for i in range(b+1,len(a)):
        j=i
        while(j>b)and a[j-1]>a[j]:
            a[j],a[j-1]=a[j-1],a[j]
            j-=1
    
    w=""
    for i in a:
        w+=chr(i)
        #w+=str(chr(i))
    return w
if __name__=='__main__':
    input_string = input()
    print(stringInsertionSort(input_string))
