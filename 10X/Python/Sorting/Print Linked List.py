'''

Print Linked List
You are given a Linked list of integers. Complete the display function which prints the elements of the linked list starting from "head" to "None" where each link is represented by

"->".

You dont need to implement your own linked list from scratch, just complete the 'display' function given in the template below. Also you dont need to worry about taking the input.

Example
Lets say the linked list in the input was

1->2->3->4

then the expected output will be

head->1->2->3->4->None
'''
class Node:
    def __init__(self, key):
        self.data = key
        self.next = None


class LL:
    def __init__(self):
        self.head = None
        
    #complete the Display function given below
    # def display(self):
    #     temp=self.head
    #     while(temp.next != None):
    #         print(temp.data, end="->")
    #         temp=temp.next
    #     print(temp.data)

    def display(self):
        temp=self.head
        print("head", end="->")
        while(temp.next != None):
            print(temp.data, end="->")
            temp=temp.next
        print(temp.data, end="->")
        print(None)
    @staticmethod
    def insert_node(val, current):
        temp = Node(val)
        current.next = temp
        current = current.next
        return current


ll = LL()
num = [int(i) for i in input().split("->")]
ll.head = Node(num[0])
curr = ll.head
for i in num[1:]:
    curr = LL.insert_node(i, curr)
ll.display()