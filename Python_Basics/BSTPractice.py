class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def getData(self):
        return self.data

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def __str__(self):
        return str(self.data)

class BinarySearchTree:
    def __init__(self, data):
        self.root = Node(data)

    def insertTree(self, data):
        if self.root.data is None:
            print(data, "Added at root")
            self.root = Node(data)
        else:
            self.insertHelper(self.root, data)

    def insertHelper(self, start, data):
        if start.data >= data:
            print(data, "Going Left")
            if start.left is None:
                print(data, "Added")
                start.left = Node(data)
            else:
                self.insertHelper(start.left, data)
        else:
            print(data, "Going Right")
            if start.right is None:
                print(data, "Added")
                start.right = Node(data)
            else:
                self.insertHelper(start.right, data)

#       7 <-- Root
#    /      \
#   6        8
#  / \      / \
# 4   7   7.5   9
    def search(self, item):
        if self.root == item:
            return self.root
        else:
            self.searchHelper(self.root, item)

    def searchHelper(self, start, item):
        if start.data == item:
            return start
        else:
            # if the element is less than the data at the node then the element will be in the left subtree if left subtree exists
            if item <= start.data and start.left is not None:
                self.searchHelper(start.left, item)
            # if the element is greater than the data at the node then the element will be in the right subtree if right subtree exists
            elif item >= start.data and start.right is not None:
                self.searchHelper(start.right, item)
        return "NOT FOUND"

    def inorderPrint(self, start):
        if start.left is not None:
            self.inorderPrint(start.left)
        print(start)
        if start.right is not None:
            self.inorderPrint(start.right)


bst1 = BinarySearchTree(7)
bst1.insertTree(6)
bst1.insertTree(8)
bst1.insertTree(4)
bst1.insertTree(7)
bst1.insertTree(9)
bst1.insertTree(7.5)
bst1.inorderPrint(bst1.root)
print(bst1.search(4))

