# Merge two sorted linked lists and return it as a sorted list.
# The list should be made by splicing together the nodes of the first two lists.
#Class Definition of Linked List
class Node:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
class Solution:
    #Approach1:(Itreative)
    #Time Complexity:O(m+n)
    #Space Complexity:O(1)
    def mergetwolists(self,l1,l2):
        cur = head = Node(0)
        while l1 and l2:
            if l1.val<=l2.val:
                head.next = l1
                l1 = l1.next
                head = head.next
            elif l1.val>l2.val:
                head.next = l2
                l2 = l2.next
                head = head.next
        if l1:
            head.next = l1
        if l2:
            head.next = l2
        return cur.next
    #Approach2:(Recrusive)
    #Time Complexity:O(m+n)
    #Space Complexity:O(m+n)
    def mergetwolists1(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergetwolists1(l1.next,l2)
            return l1
        else:
            l2.next = self.mergetwolists1(l1,l2.next)
            return l2
    def printinglist(self,head):
        while head:
            print(head.val,end=" ")
            head = head.next
sol = Solution()
ans = Node(1)
ans.next = Node(2)
ans.next.next = Node(4)
ans1 = Node(1)
ans1.next = Node(3)
ans1.next.next = Node(4)
ans1.next.next.next = Node(5)
head = sol.mergetwolists1(ans,ans1)
print(sol.printinglist(head))
