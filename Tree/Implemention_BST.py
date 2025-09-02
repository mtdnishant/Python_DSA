## Binary search tree

class Node:
    def __init__(self,item=None,left=None,right=None):
        self.item = item
        self.left= left
        self.right= right
        
class BST:
    def __init__(self,root=None):
        self.root = root
    
    def is_empty(self):
        return self.root == None
    
    def insert(self,data):
        self.root = self.rInsert(self.root,data)
        
    def rInsert(self,root,data):
        if root is None:
            return Node(data)
        if data < root.item:
            root.left = self.rInsert(root.left,data)
        elif data > root.item:
            root.right=self.rInsert(root.right,data)
        return root
           
    
    def search(self,data):
        return self.rSearch(self.root,data)
    def rSearch(self,root,data):
        if root is None or root.item == data:
            return root
        if data < root.item:
            return self.rSearch(root.left,data)
        else:
            return self.rSearch(root.right,data)
        
    def inOrder(self):
        result=[]
        self.rinOrder(self.root,result)
        return result
    
    def rinOrder(self,root,result):
        if root:
            self.rinOrder(root.left,result)
            result.append(root.item)
            self.rinOrder(root.right,result)
            
    def preOrder(self):
        result=[]
        self.rPreOrder(self.root,result)
        return result
    
    def rPreOrder(self,root,result):
        if root:
            result.append(root.item)
            self.rPreOrder(root.left,result)
            self.rPreOrder(root.right,result)
            
    def postOrder(self):
        result=[]
        self.rPostOrder(self.root,result)
        return result
    
    def rPostOrder(self,root,result):
        if root:
            self.rPostOrder(root.left,result)
            self.rPostOrder(root.right,result)
            result.append(root.item)
            
    def min_value(self,temp):
        current = temp
        while current.left is not None:
            current = current.left
        return current.item
    
    def min_value(self,temp):
        current = temp
        while current.right is not None:
            current = current.right
        return current.item
    
    def delete(self,data):
        self.root = self.rDelete(self.root,data)

    def rDelete(self, root, data):
        if root is None:
            return root
        if data < root.item:
            root.left = self.rDelete(root.left, data)
        elif data > root.item:
            root.right = self.rDelete(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
             # Two children case:
            root.item = self.min_value(root.right)
            root.right = self.rDelete(root.right, root.item)
        return root
    
    def size(self):
        return len(self.inOrder())
    
bs = BST()
bs.insert(50)
bs.insert(30) 
bs.insert(10)
bs.insert(40)
bs.insert(35)
bs.insert(80)
bs.insert(70)
bs.insert(100)           
bs.insert(75)
bs.insert(65)

print("InOrder: ",bs.inOrder())
print("preOrder:",bs.preOrder())
print("postOrder:",bs.postOrder())
  
bs.delete(80)        

print("InOrder: ",bs.inOrder())
print("preOrder:",bs.preOrder())
print("postOrder:",bs.postOrder())  




# def rDelete(self,root,data):
    #     if root is None:
    #         return root
    #     if data < root.item:
    #         root.left = self.rDelete(root.left,data)
    #     elif data > root.item:
    #         root.right = self.rDelete(root.right,data)
    #     else:
    #         if root.left is None:
    #             return root.right
    #         elif root.right is None:
    #             return root.left
    #         root.item = self.min_value(root.right)
    #         self.rDelete(root.right,root.item)
    #     return root
            
                