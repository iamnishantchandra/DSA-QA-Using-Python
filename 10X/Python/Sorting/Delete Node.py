'''
Delete Node
Given a singly linked list and a position, delete a linked list node at the given position.

Note:
This is a functional problem, so you don't need to worry about the input and output format. Simply take care of the deleteNode function. Make sure to take care, whether the given position is valid or not!

Constraint:
Position value will non-negative.

Example & Explanation:
Input: position = 1, Linked List = 8->2->3->1->7
Output: Linked List =  8->3->1->7
Input: position = 0, Linked List = 8->2->3->1->7
Output: Linked List = 2->3->1->7
In the first example, the node at position 1 is removed. And in the second example, the node at position 0 is removed.


'''
# Python program to detect loop in the linked list 

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

# Do not change anything above this line
    def deleteNode(self, position): 
        # YOU ONLY NEED TO COMPLETE THIS FUNCTION.
        temp=self.head
        c=0
        if position==0:
            self.head=temp.next
            del(temp)
        else:   
            while c<=position and temp!=None:
                if c==position-1:
                    delt=temp.next
                    temp.next=temp.next.next
                    del(delt)
                else:   
                    temp=temp.next
                c+=1
                
  
    # Utility function to print the linked LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print(temp.data, end=" ")
            temp = temp.next


# Do not change anything below this line
if __name__ == '__main__':
    
    n = int(input())

    # Start with the empty list 
    llist = LinkedList() 

    temp = [int(x) for x in input().split()]

    if(n<1):
        llist.head = None
    elif(n<2):
        llist.head = Node(temp[0])
    else:
        llist.head = Node(temp[0])
        second = Node(temp[1])
        llist.head.next = second
        curr = llist.head.next


    for i in range(2,n):
        t = Node(temp[i])
        curr.next = t
        curr = curr.next

    pos = int(input())

    llist.deleteNode(pos)
    llist.printList()