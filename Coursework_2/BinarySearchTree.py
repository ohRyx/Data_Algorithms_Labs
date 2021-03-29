import os
import sys

class BST:
    root=None

    def put(self, key, val):
        self.root = self.put2(self.root, key, val)

    def put2(self, node, key, val):
        if node is None:
            #key is not in tree, create node and return node to parent
            return Node(key, val)
        if key < node.key:
            # key is in left subtree
            node.left = self.put2(node.left, key, val)
        elif key > node.key:
            # key is in right subtree
            node.right = self.put2(node.right, key, val)
        else:
            node.val = val
        node.count = 1 + self.size2(node.left) + self.size2(node.right)
        return node

    def createTree(self, a): 
        for x in a:
            n = x.split(":")
            self.put(n[0], n[1])
    
    #Create a AVL Tree, you are allowed to create other helper functions
    def createBalancedTree(self, a): 
        self.root = None
        for x in a:
            n = x.split(":")
            self.insert2(n[0], n[1])
        
    def insert2(self, key, val):
        self.root = self.insert(self.root, key, val)

    def insert(self,root,key, val):
        if root is None:
            return Node(key, val)
        elif key < root.key:
            root.left = self.insert(root.left, key, val)
        else:
            root.right = self.insert(root.right, key, val)

        root.height3 = 1 + max(self.getHeight(root.left), (self.getHeight(root.right)))

        balance  = self.getBalance(root)

        if balance > 1 and key < root.left.key:
            return self.rightRotate(root)

        if balance < -1 and key > root.right.key:
            return self.leftRotate(root)

        if balance > 1  and key > root.left.key:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        
        if balance < -1 and key < root.right.key:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        
        return root

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
 
        y.left = z
        z.right = T2
 
        z.height3 = 1 + max(self.getHeight(z.left),
                         self.getHeight(z.right))
        y.height3 = 1 + max(self.getHeight(y.left),
                         self.getHeight(y.right))
 
       
        return y
  
    def rightRotate(self, z):
 
        y = z.left
        T3 = y.right
 
        y.right = z
        z.left = T3
 
        z.height3 = 1 + max(self.getHeight(z.left),
                        self.getHeight(z.right))
        y.height3 = 1 + max(self.getHeight(y.left),
                        self.getHeight(y.right))
 
        return y  
    
    def getHeight(self, root):
        if not root:
            return 0
        return root.height3
    
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)
            
    #preOrder Traversal, this should be a recursive function
    def preOrder(self, node):
        preOrderList = []
        if node:     
           preOrderList.append(node.key + ":" + node.val)
           preOrderList += self.preOrder(node.left)
           preOrderList += self.preOrder(node.right)
        return preOrderList
        
    #inOrder Traversal, this should be a recursive function
    def inOrder(self, node):
        inOrderList = []
        if node:
            inOrderList += self.inOrder(node.left)
            inOrderList.append(node.key + ":" + node.val)
            inOrderList += self.inOrder(node.right)
        return inOrderList
             
    #postOrder Traversal, this should be a recursive function
    def postOrder(self, node):
        postOrderList = []
        if node:
           postOrderList +=  self.postOrder(node.left)
           postOrderList +=  self.postOrder(node.right)
           postOrderList.append(node.key + ":" + node.val)
        return postOrderList
      
    #given a key, obtain its value
    def get(self, key):
        p = self.root
        while p is not None:
            if p.key == key:
                return p.val
            elif p.key > key:
                p = p.left
            else:
                p = p.right
        return None
         
    #given a key, find the node and obtain the depth, you are allowed to create other helper functions
    def depth(self, key):
        d = self.root
        dist = 0
        
        while d is not None:
            if d.key == key:
                return dist
            elif d.key > key:
                    d = d.left
                    dist += 1
            else:
                 d = d.right
                 dist += 1
        return None
        
    #given a key, find the node and obtain the height, you are allowed to create other helper functions
    def height(self, key):
        r = self.root

        while r is not None:
            if r.key == key:
                return self.height2(r)
            elif r.key > key:
                    r = r.left
            else:
                 r = r.right
        return None

    def height2(self, node):
        if node is None:
            return -1
        left = self.height2(node.left)
        right = self.height2(node.right)

        return 1 + max(left, right)
         
    #given a key, find the node and obtain the size, you are allowed to create other helper functions
    def size(self, key):
        p = self.root
        while p is not None:
            if p.key == key:
                return p.count
            elif p.key > key:
                p = p.left
            else:
                p = p.right
        return None

    def size2(self, n):
        if n is None:
            return 0
        else:
            return n.count
    
    #given a key, delete the node, you are allowed to create other helper functions
    def delete(self, key):
        if(self.getNode(key) is None):
            return False
        else:
            self.root = self.delete2(self.root, key)
            return True
    
    def delete2(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self.delete2(node.left, key)
        elif key > node.key:
            node.right = self.delete2(node.right, key)
        else:
            if node.right is None:
                return node.left
            if node.left is None:
                return node.right
            t = node
            node = self.min(t.right)
            #Create a min function
            node.right = self.deleteMin2(t.right)
            node.left = t.left
        node.count = self.size2(node.left) + self.size2(node.right) + 1
        return node

    def deleteMin(self):
        self.root = self.deleteMin2(self.root)

    def deleteMin2(self, node):
        if node.left is None:
            return node.right
        node.left = self.deleteMin2(node.left)
        node.count = 1 + self.size2(node.left) + self.size2(node.right)
        return node
    
    def min(self, node):
        current = node

        while(current.left is not None):
            current = current.left
        
        return current

    def getNode(self,key):
        p = self.root
        while p is not None:
            if p.key ==key:
                return p
            elif p.key > key:
                p = p.left
            else:
                p = p.right
      	
class Node:
    left = None
    right = None
    key = 0
    count = 0
    val = 0

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.count = 1
        self.height3 = 1
        self.left = None
        self.right = None

array = input("Enter a list of key:value pairs separated by commas:\n")
array = [str(x) for x in array.split(",")]

bst = BST()
bst.createTree(array)

# ###testcase 0 (get())
# for i in range(2):
#     key1 = input("Input key for get() method:\n")
#     if key1 != '-':
#         print("The value of", key1, "is", bst.get(key1))

# ###testcase 1 (size(),depth(),height())
# key1 = input("Input key for size() method:\n")
# if key1 != '-':
#     print("The size of", key1, "is", bst.size(key1))
# key1 = input("Input key for depth() method:\n")
# if key1 != '-':
#     print("The depth of", key1, "is", bst.depth(key1))
    
# key1 = input("Input key for height() method:\n")
# if key1 != '-':
#     print("The height of", key1, "is", bst.height(key1))


##testcase 2 (preOrder(), inOrder(), postOrder())
# print("The preOrder traversal is", bst.preOrder(bst.root))
# print("The inOrder traversal is", bst.inOrder(bst.root))
# print("The postOrder traversal is", bst.postOrder(bst.root))
# print()


###testcase 3 delete()
# for i in range(2):
#     key1 = input("Input key for delete() method:\n")
#     if key1 != '-':
#         print("Deleting", key1, "is", bst.delete(key1))
#         print("The preOrder traversal is", bst.preOrder(bst.root))
#         print("The inOrder traversal is", bst.inOrder(bst.root))
#         print("The postOrder traversal is", bst.postOrder(bst.root))


# ###testcase 4 createbalancedTree()
key1 = input("Test balanced Tree? \n")
if key1 == 'Y':
    bst.createBalancedTree(array)
    print("The preOrder traversal is", bst.preOrder(bst.root))
    print("The inOrder traversal is", bst.inOrder(bst.root))
    print("The postOrder traversal is", bst.postOrder(bst.root))