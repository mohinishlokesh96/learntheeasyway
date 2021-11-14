# Given the root of a binary tree, invert the tree, and return its root.
#Tree class defintion
class Node:
    def __init__(self,val = 0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    #Approach1:(DFS)
    #Time Complexity:O(N) Where N is the number of Nodes
    #Space Complexity:O(N) Where N is the number of Stack frames
    def inverttree1(self,root):
        if not root:
            return None
        right = self.inverttree1(root.right)
        left = self.inverttree1(root.left)
        root.left = right
        root.right = left
        return root
    #Approach2:(BFS)
    #Time Complexity:O(N) where N is the number of Nodes
    #Space Complexity:O(N) Where N length of the q used in storing the nodes
    def inverttree2(self,root):
        if not root:
            return root
        q = [root]
        while q:
            length = len(q)
            for _ in range(length):
                current = q.pop(0)
                current.left,current.right = current.right,current.left
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
        return root
    def printinglist(self,root):
        q = [root]
        while q:
            length = len(q)
            for _ in range(length):
                current = q.pop(0)
                print(current.val,end=" ")
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
sol = Solution()
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(sol.printinglist(root))
head = sol.inverttree2(root)
print(sol.printinglist(head))