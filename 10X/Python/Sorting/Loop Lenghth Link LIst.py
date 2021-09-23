'''
Loop Length
Given a head pointer to the linked list, complete the function detectAndCountLoop() that checks whether a given Linked List contains loop and if loop is present then returns count of nodes in loop. For example, the loop is present in below-linked list and length of the loop is 4. If the loop is not present, then the function should return 0.

Note:
This is a functional problem, so you don't need to worry about the input and output format. Simply take care of the detectAndCountLoop function.

Example & Explanation:
Suppose, given Linked List is:

76 -> 66 -> 11 -> 73 -> 77 
       ^                 |
       |_________________|  
Then, the output should be:

4
Because, the given linked list consists of a loop and the length of the loop is 4!


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

    def detectAndCountLoop(self):
        # YOU ONLY NEED TO COMPLETE THIS FUNCTION.
        # RETURN Length-of-the-loop IF LOOP IS THERE IN THE LINKED LIST, ELSE RETURN 0
        temp=self.head
        dic={}
        c=0
        while temp!=None:
            if temp in dic:
                dic[temp]+=1
                if dic[temp]==2:
                    c+=1
                elif dic[temp]==3:
                    return c
            else:
                dic[temp]=1
            temp=temp.next
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

    print(llist.detectAndCountLoop())