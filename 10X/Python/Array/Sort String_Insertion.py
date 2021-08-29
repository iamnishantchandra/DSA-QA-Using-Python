'''
String Insertion
The task is to complete the stringInsertionSort() function which is used to implement Insertion Sort, for string.

The resultant string should have characters in lexicographically sorted order. You don't need to worry about input/output.

Input
One string

Output
Sorted string

Example
Input1:

adcb
Output1:

abcd


'''
def stringInsertionSort(str):
    # Your code goes here
    
    a=[]
    for i in range(len(str)):
        a.append(ord(str[i]))
    # a.sort()
    
    for i in range(1,len(a)):
        j=i
        while(j>0)and a[j-1]>a[j]:
            a[j],a[j-1]=a[j-1],a[j]
            j-=1
    
    w=""
    for i in a:
        w+=chr(i)
        #w+=str(chr(i))
    return w




### DO NOT CHANGE ANYTHING BELOW THIS LINE

if __name__=='__main__':
    input_string = input()
    print(stringInsertionSort(input_string))

