# Given the head of a singly linked list, return true if it is a palindrome.
# Class Definition for Linked List
class Node:
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next =next
class Solution:
    #Approach1:
    #Time Complexity:O(N)
    #Space Complexity:O(N)
    def palindromelinkedlist1(self,head):
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack==stack[::-1]
    #Approach2:
    #Time Complexity:O(N)
    #Space Complexity:O(1)
    def palindromelinkedlist2(self,head):
        if head is None:
            return True
        first_half_end=self.end_of_first_half(head)
        second_half_start=self.reverse_list(first_half_end.next)
        result=True
        first_position=head
        second_position=second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result=False
            first_position=first_position.next
            second_position=second_position.next
        first_half_end.next=self.reverse_list(second_half_start)
        return result

    def end_of_first_half(self, head):
        fast=head
        slow=head
        while fast.next is not None and fast.next.next is not None:
            fast=fast.next.next
            slow=slow.next
        return slow

    def reverse_list(self, head):
        previous=None
        current=head
        while current is not None:
            next_node=current.next
            current.next=previous
            previous=current
            current=next_node
        return previous
sol = Solution()
ans = Node(1)
ans.next = Node(2)
ans.next.next = Node(3)
ans.next.next.next = Node(2)
ans.next.next.next.next = Node(1)
print(sol.palindromelinkedlist2(ans))