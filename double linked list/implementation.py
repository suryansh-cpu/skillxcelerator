class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class DLL:
    def __init__(self):
        self.head = None
    def insertt(self,input):
        new_node = Node(input)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
        new_node.next = None

    def insert(self, pos, data):
        new_node = Node(data)
        if pos < 0:
            print("Invalid location!!!!")
            return
        if pos == 0:
            if self.head:
                new_node.next = self.head
                self.head.prev = new_node
            self.head = new_node
            return

        current = self.head
        for _ in range(pos - 1):
            if not current:
                print("Index out of bound!!")
                return
            current = current.next

        if not current:
            print("Index out of bound!!")
            return

        new_node.next = current.next
        if current.next:
            current.next.prev = new_node
        current.next = new_node
        new_node.prev = current



    # def insert(self,pos,data):
    #     i=0
    #     new_node = Node(data)
    #     if(pos < 0):
    #         print("Invalid location!!!!")
    #         return
    #     if(pos==0):
    #         new_node.next = self.head
    #         self.head.prev = new_node
    #         self.head = new_node
    #         return
    #     current = self.head
    #     for _ in range(pos-1):
    #         if not current:
    #             print("Index out of bound!!")
    #             return
    #         current = current.next  
    #         if not current:
    #             print("Index out of bound!!")
    #             return   
    #         new_node.next = current.next
    #         current.next = new_node
    #         new_node.prev = current
    #         # temp = new_node.next
    #         new_node.prev = new_node



    # def display(self):
    #     current = self.head
    #     if not current:
    #         print("Empty doule linked list error!!")
    #         return
    #     else:
    #         print(f"{current.data}<-->")
    #         current = current.next
    #         while current:
    #             print(f"{current}<-->")
    #             current = current.next
    def display(self):
        current = self.head
        if not current:
            print("Empty double linked list error!!")
            return
        while current:
            print(f"{current.data}<-->", end="")
            current = current.next
        print("NULL")

ll = DLL()
ll.display()
ll.insertt(1)
# ll.insertt(2)
ll.insert(1,15)
ll.insert(2,12)
ll.display()
        
        