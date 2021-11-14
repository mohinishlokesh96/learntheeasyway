# Given the head of a singly linked list, reverse the list, and return the reversed list.
#Class definition Linked List
class Node:
    def __init__(self,val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    #Approach1:(Iterative)
    #Time Complexity:O(N) Where N is the number of nodes we have to traverse
    #Space Complexity:O(1)
    def reverselinkedlisti(self,head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev
    #Approach2:Recrusive)
    #Time Complexity:O(N) Where N is the number of nodes we have to traverse:
    #Space Complexity:O(N) Where N is the stack frame used to store recursive calls
    def reverselinkedlistr(self,head):
        if head is None or head.next is None:
            return head
        prev = self.reverselinkedlistr(head.next)
        head.next.next = head
        head.next = None
        return prev
    def printinglist(self,head):
        while head:
            print(head.val)
            head = head.next
sol = Solution()
ans = Node(1)
ans.next = Node(2)
ans.next.next = Node(3)
ans.next.next.next = Node(4)
head = sol.reverselinkedlistr(ans)
print(sol.printinglist(head))