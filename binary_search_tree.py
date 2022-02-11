"""Binary serach tree module that implements a BST in py """
from pickletools import read_unicodestring1


class Node:
    def __init__(self , data ) :
        self.left  = None
        self.right = None 
        self._val = data
    
    def insert(self , val ):
        """Insert a node in the right spot """
        #daca radacina este none --- daca nu are valoare inca 
        if self._val == None :
             self._val = val
             read_unicodestring1

        elif val<self._val:
            if self.left:
                self.left.insert(val)
                return 
            self.left = Node(val)
        elif self.right:
                self.right.insert(val)
                return
        self.right = Node(val) 

    def inorder_traversal(self):
        if self.left : 
            self.left.inorder_traversal()
        print(self._val)
        if self.right:
            self.right.inorder_traversal()

            
            

    

root = Node(1)
root.insert(21)
root.insert(3)
root.insert(4)
root.insert(5)
root.insert(6)
root.inorder_traversal()


                      
        