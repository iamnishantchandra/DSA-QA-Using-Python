'''
nth from back
Description
Given a Linked List and a number n, print the value at the n’th node from the end of the Linked List.

Where n > 0 and n <= N. N = length of the LL. You just need to implement return n_th_from_back.

Input
First line contains an integer N and n denoting the size of the Linked List and the required n-th node.

Next line contain N space separated integers dentoing the LL.

Output
Print a single integer i.e the n-th node from back

Input:

5 4

1 2 3 4 5

Output:

2

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
 
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
 
 
def length_llist(llist):
    length = 0
    current = llist.head
    while current:
        current = current.next
        length = length + 1
    return length
 
 
def return_n_from_last(llist, n):
   #Implement this
    count=length_llist(llist)
    index=count-n
    c=0
    if index<0:
        return None
    temp=llist.head
    while(temp!=None) and c<=index:
        if index==c:
            return temp.data
        c+=1
        temp=temp.next
    
    return count

   
 

N, n = map(int, input().split(' ')) 
a_llist = LinkedList()

l = list(map(int, input().split(' ')))
for i in l:
    a_llist.append(i) 

value = return_n_from_last(a_llist, n)
 
print(value)