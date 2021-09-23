'''
find nth node in linkedlist
Write a function that takes a linked list and an integer index and returns the data value stored in the node at that index position. If index doesnot exist return None.

Input
First line is an integer T, representing total number of test cases. For each testcase, 1st line containing space separated integers of linked list from left to right. For each testcase, 2nd line containing index to be found.

Output
T lines, each line containing the node value for each test case.

Example
Input: 2

2 2 4 5 6

4

11 1 1 1 3

0

Output: 5

None

'''
class Node: 
    def __init__(self, value): 
        self.data = value 
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
  
    def push(self, new_value): 
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node 
          
    def getNth(self, index): 
        ####WRITE CODE HERE###
        c=1
        if index<=0:
            return None
        temp=self.head
        while(temp!=None) and c<=index:
            if index==c:
                return temp.data
            c+=1
            temp=temp.next
        if index>c-1:
            return None


def read_list_input():
    vals = input().split(' ')
    linkedList = LinkedList() 
    for val in vals:
        linkedList.push(val)
    return linkedList

test_cases = int(input())
for i in range(test_cases):
    linkedList = read_list_input()
    index=int(input())
    print(linkedList.getNth(index))