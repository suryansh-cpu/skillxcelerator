class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class BT:
    def __init__(self):
        self.root = None


    # def insert(self,input):
    #     # new_node = Node(input)
    #     i=0
    #     if not self.root:
    #         self.data = input[0]
    #         self.left = None
    #         self.right = None
    #         # return
    #     current = self.root
    #     # if(len(input)>1):
    #     if(current == input[0]):
    #         i+=1
    #     while(i<len(input) and current):
    #         if(current.left==None):
    #             current.left=input[i]
    #             i+=1
    #         elif(current.right==None):
    #             current.right = input[i]
    #             i+=1
    #         else:
    #             current = current.left


def printinorder(node):
        # if(root==None):
        #     # print("Empty tree")
        #     return
    if node is None:
        return
    printinorder(node.left)
    print(node.data)
    printinorder(node.right)
def preorder(node):
        # if(root==None):
        #     # print("Empty tree")
        #     return
    if node is None:
        return
    print(node.data)
    preorder(node.left)
    preorder(node.right)


    # complete later
# def input(a):
#     i = int(len(a)//2)
#     temp = Node(a[i])
#     i-=1
#     while i>-1:
#         temp.left = a[i]
#         i-=1
#         temp = temp.left
#     i = int(len(a)//2)
#     # temp = Node(a[i])
#     temp = 
#     while i<len(a):


def heightoftree(root):
    if root is None:
        return 0
    if (root.left == None and root.right == None):
        return 1
    heightofleft = heightoftree(root.left)
    heightofright = heightoftree(root.right)
    return (1+max(heightofleft,heightofright))

# maxx=0
maxx = 0
def distance(root):
    global maxx
    if root is None:
        return 0
    
    left = distance(root.left)
    right = distance(root.right)
    
    maxx = max(maxx, left + right + 1)
    
    return 1 + max(left, right)

# if __name__ == '__main__':
# bt = BT()

root = Node(10)
root.left = Node(2)
root.right= Node(35)
root.left.left = Node(44)
root.left.right = Node(51)
root.right.right = Node(600)
print(heightoftree(root))
# print(distance(root))
distance(root)
print(maxx-1)
# printinorder(root)
# print("********")
# preorder(root)


# a = [1,2,3]
# bt.insert(a)
# root = a[0]
# bt.printinorder(root)