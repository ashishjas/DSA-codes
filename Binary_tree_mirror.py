class Treenode :
    def __init__(self,data) :
        self.data=data
        self.left=None
        self.right=None
    
class Binary_tree :
    def __init__(self):
        self.root=None
    
    def get_binary_tree(self) :
        #below are hardcoded
        self.root=Treenode(5)
        self.root.left=Treenode(4)
        self.root.right=Treenode(1)
        self.root.left.left=Treenode(8)
        self.root.left.right=Treenode(23)
        self.root.right.left=Treenode(54)
        self.root.right.right=Treenode(41)
        self.root.right.right.right=Treenode(81)
        #Tree formed :
        '''

                 5
                / \
               4   1  
              / \  / \
             8  23 54 41
                        \
                         81
        
        '''
    
    def inorder(self,root) :
        if root is None :
            return
        self.inorder(root.left)
        print(root.data," ",end="")
        self.inorder(root.right)

    def preorder(self,root) :
        if root is None :
            return
        print(root.data," ",end="") 
        self.preorder(root.left)
        self.preorder(root.right)

    def level_order(self,tnode) :
        if tnode is None : 
            return 
        Q=[]
        Q.append(tnode) 

        while (len(Q)>0) :
            temp=Q.pop(0)
            print(temp.data," ",end="")

            if temp.left is not None :
                Q.append(temp.left)
            if temp.right is not None :
                Q.append(temp.right)
    
    def mirror(self,tnode) :
        if tnode is None :
            return
        self.mirror(tnode.left)
        self.mirror(tnode.right)
        temp=tnode.left
        tnode.left=tnode.right
        tnode.right=temp

#driver code 

if __name__=='__main__' :
    tree=Binary_tree()
    tree.get_binary_tree()
    print("\ninorder traversal-->"," ",end="")
    tree.inorder(tree.root)
    print("\nlevel_order traversal-->"," ",end="")
    tree.preorder(tree.root)
    print("\nlevel_order traversal-->"," ",end="")
    tree.level_order(tree.root)
    print("\n\nTaking mirror image of the tree")
    tree.mirror(tree.root)
    print("\nTraversal after mirror image of the tree")
    print("\ninorder traversal-->"," ",end="")
    tree.inorder(tree.root)
    print("\npreorder traversal-->"," ",end="")
    tree.preorder(tree.root)
    print("\nlevel_order traversal-->"," ",end="")
    tree.level_order(tree.root)
    

