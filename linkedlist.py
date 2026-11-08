class Node:
    def __init__(self,data):
        self.data=data
        self.next=None



class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_Node=Node(data)
        if self.head is None:
            self.head=new_Node

        current=self.head
        current.next=new_Node



    def display(self):
        self=current.self

        while current:
            print(current.data)

            currrent=current.next
            

    