'''
Delete same
Description
You are given the pointer to the head node of a sorted linked list, where the data in the nodes is in ascending order. Delete nodes and return a sorted list with each distinct value in the original list. The given head pointer may be null indicating that the list is empty.

Input
The first line contains an integer t, the number of test cases.

The format for each test case is as follows:

The first line contains an integer n, the number of elements in the linked list.

The second line contains n spaced integers.

Output
For each query, print the new list.

Example
Input:

1

5

1 2 2 3 4

Output:

1 2 3 4

Explanation
Initial list-: 1->2->2->3->4.

Final list-: 1->2->3->4.


'''
class Node:  
  
    # Constructor to initialize  
    # the node object  
    def __init__(self, data):  
        self.data = data  
        self.next = None
  
class LinkedList:  
  
    # Function to initialize head  
    def __init__(self):  
        self.head = None
  
    # Function to insert a new node  
    # at the beginning  
    def push(self, new_data):  
        new_node = Node(new_data)  
        new_node.next = self.head  
        self.head = new_node  
  
    
    
  
    # Utility function to print the  
    # linked LinkedList  
    def printList(self):  
        temp = self.head  
        while(temp):  
            print(temp.data , end = ' ') 
            temp = temp.next
        print('')
      
    # This function removes duplicates  
    # from a sorted list          
    def removeDuplicates(self): 
        #Implement this only
        temp=self.head
        if temp==None:
            return 
        while temp.next!=None:
            if temp.data==temp.next.data:
               delt=temp.next
               temp.next=temp.next.next
               del(delt)
            else:
                temp=temp.next

         
  
# Driver Code  
testCase = int(input())
for _ in range(testCase):
	listSize = int(input())
	givenElements = list(map(int, input().split()))
	givenElements.reverse()
	llist = LinkedList()
	for element in givenElements:
		llist.push(element)
	llist.removeDuplicates()
	llist.printList()