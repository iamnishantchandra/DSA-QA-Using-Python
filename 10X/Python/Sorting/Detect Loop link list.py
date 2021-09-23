'''
Detect Loop
Given a head pointer to the linked list, check if the linked list has loop or not. If it has loop, function should return 1, else it should return 0.

Note:
This is a functional problem, so you don't need to worry about the input and output format. Simply take care of the detectLoop function.

Example & Explanation:
Suppose, given Linked List is:

76 -> 66 -> 11 -> 73 -> 77 
       ^                 |
       |_________________|  
Then, the output should be:

1
Because, the given linked list consists of a loop!

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

    def detectLoop(self):
        # YOU ONLY NEED TO COMPLETE THIS FUNCTION.
        # RETURN 1 IF LOOP IS THERE IN THE LINKED LIST, ELSE RETURN 0
        temp=self.head
        f=temp.next
        s=temp.next.next
        while s!=None:    
            if f==s:
                return 1
            f=f.next
            s=s.next.next
        return 0


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

    link = int(input())
    if(link!=-1):
        t = llist.head
        for _ in range(link-1):
            t = t.next
        curr.next = t

    # llist.printList()
    print(llist.detectLoop())