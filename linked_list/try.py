class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_node(self,pos,data):
        new_node = Node(data)
        temp = self.head
        if pos==1:
            new_node.next = self.head
            self.head = new_node
            return
        else:
            while pos-1 != -1 and temp.next != None:
                temp=temp.next
                pos-=1
            new_node.next=temp.next
            temp.next=new_node
    def update_node(self,pos,data):
        if pos==1:
            self.head.data = data
        temp = self.head
        while(pos!=1 and temp.next!=None):
            temp=temp.next
            pos-=1
        temp.head = data
    

    # def display(self):
    #     current = self.head
    #     while current:
    #         print(current.data, end=" -> ")
    #         current = current.next
    #     print("None")
    # def insert(self, data):
    #     node = Node(data)
    #     if not self.head:
    #         self.head = node
    #         # LinkedList.display()
    #         current = self.head
    #         while current:
    #             print(current.data, end=" -> ")
    #             current = current.next
    #         print("None")
    #         return None
    #     current = self.head
    #     while current.next:
    #         current = current.next
    #     current.next = node
    #     current = self.head
    #     while current:
    #         print(current.data, end=" -> ")
    #         current = current.next
    #     print("None")
        # LinkedList.display()
ll = LinkedList()
ll.insert(10)