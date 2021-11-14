# Given the head of a linked list and an integer val, remove all the
# nodes of the linked list that has Node.val == val, and return the new head.
#Class node is the definition for the linked list
class Node:
    def __init__(self,val = 0,next=None):
        self.val = val
        self.next = next

class Solution:
    #Approach1:
    #Time Complexity:O(N)
    #Space Complexity:O(1)
    def removelinkedlist(self,head,val):
        cur = Node(-1,head)
        prev = cur
        while head:
            if head.val == val:
                prev.next = head.next
                head = head.next
            else:
                prev = head
                head = head.next
        return cur.next
    def printinglist(self,head):
        while head:
            print(head.val,end=" ")
            head = head.next

ans = Node(1)
ans.next = Node(2)
ans.next.next = Node(6)
ans.next.next.next = Node(3)
ans.next.next.next.next = Node(4)
ans.next.next.next.next.next = Node(5)
ans.next.next.next.next.next.next = Node(6)
sol = Solution()
print(sol.printinglist(ans))
head = sol.removelinkedlist(ans,1)
print(sol.printinglist(head))
