# Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s.
# A subtree of s is a tree consists of a node in s and all of this node's descendants.
# The tree s could also be considered as a subtree of itself.
#Class Node is the basic definition for left and right for the node
class Node:
    def __init__(self,val = 0,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    #Approach1:(Depth first search)
    #Time Complexity:O(N)
    #Space Complexity:O(N)
    def subtree(self,root1,root2):
        def dpreorder(root):
            if root is None:
                return "N"
            preorder = "|"+str(root.val)+"|"
            preorder+=dpreorder(root.left)
            preorder+=dpreorder(root.right)
            return preorder
        preorder1 = dpreorder(root1)
        preorder2 = dpreorder(root2)
        return True if preorder2 in preorder1 else False
sol = Solution()
root1 = Node(3)
root1.right = Node(5)
root1.left = Node(4)
root1.left.left = Node(1)
root1.left.right = Node(2)
root2  =Node(4)
root2.left = Node(1)
root2.right  = Node(2)
print(sol.subtree(root1,root2))