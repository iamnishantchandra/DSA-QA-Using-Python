'''
Skip M delete N
Description
Given a linked list and two integers M and N. Traverse the linked list such that you retain M nodes then delete next N nodes, continue the same till end of the linked list.

You only need to implement a Function in the template.

Input
For each testcase, first line of input contains number of elements in the linked list and next M and N respectively space separated. The last line contains the elements of the linked list.

Output
Print the final LL

Input:

8

2 1

9 1 3 5 9 4 10 1

Output:

9 1 5 9 10 1


'''
# Python program to delete M nodes after N nodes 
  
# Node class  
class Node: 
  
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
    # Function to insert a new node at the beginning 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  
    # Utility function to prit the linked LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print (temp.data, end=' ') 
            temp = temp.next
  
    def skipMdeleteN(self, M, N): 
        # Implment This 
        temp=self.head
        p=1
        while (temp!=None):
            if M+N-1>=p>=M and temp.next!=None  :
                    delt=temp.next
                    temp.next=temp.next.next
                    del(delt)
############ Faster Above #################
        # while (temp!=None):
            
        #     if M==0:
        #         self.head=temp.next
        #         del(temp)
        #     elif M>1 and M+N-1>=p>=M and temp.next!=None  :
        #             delt=temp.next
        #             temp.next=temp.next.next
        #             del(delt)
                        
            else:
                temp=temp.next
            if p==M+N:
                p-=M+N
            p+=1

          
  
# Driver program to test above function 
  

n = int(input())
M,N = map(int, input().split())
llist = LinkedList() 
l = list(map(int, input().split()))
l.reverse()
for i in l:
    llist.push(i)

llist.skipMdeleteN(M, N) 
  
llist.printList()