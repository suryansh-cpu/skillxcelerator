class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def insert_at(self, index, data):
        if index < 0:
            print("Invalid index")
            return

        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        for _ in range(index - 1):
            if not current:
                print("Index out of bounds")
                return
            current = current.next

        if not current:
            print("Index out of bounds")
            return

        new_node.next = current.next
        current.next = new_node
    def remove(self, index):
        if not self.head or index < 0:
            print("Invalid operation")
            return

        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        for _ in range(index - 1):
            if not current or not current.next:
                print("Index out of bounds")
                return
            current = current.next

        if not current.next:
            print("Index out of bounds")
            return

        current.next = current.next.next
    def print(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert_at(2,40)
# ll.replace(40,60)
# ll.remove(20)
ll.insert_at(1,10)
ll.print()