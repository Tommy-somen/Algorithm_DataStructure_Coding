# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import copy

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        new_list = []
        
        current_node = head
        
        while current_node:
            new_list.append(int(current_node.val))
            current_node = current_node.next
        
        original_list = copy.copy(new_list)
        reverse_list = (copy.copy(new_list))
        reverse_list.reverse()
        
        if original_list == reverse_list:
            return True
        else:
            return False
