# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        #ADD関数　->後方にappendする
        def _ADD(head, last_node, val):
            
            new_node = ListNode(val)
            
            if head is None:
                head = new_node
                return
            
            else:
                last_node.next = new_node
                return
            
        #headからlistを取得する
        def get_list(head):
            
            new_list = []
            
            current_node = head
            while current_node:
                new_list.append(int(current_node.val))
                current_node = current_node.next
            
            return new_list
        
        #一番最後のノードを探索する
        def get_lastnode(head):
            
            current_node = head
            while current_node.next:
                current_node = current_node.next
            
            return current_node
        
        #LinkedListとlistをマージする
        def merge(head1, head2_list):
            
            for val in head2_list:
                
                last_node = get_lastnode(head1)
                
                _ADD(head1, last_node, val)
                last_node = last_node.next
            
            return head1
            
        #LinkedListをソートする
        def sort(head):
            
            current_node = head
            
            while current_node.next:
                
                next_node = current_node.next
                
                while next_node:
                    if current_node.val > next_node.val:
                        current_node.val, next_node.val = next_node.val, current_node.val
                    
                    next_node = next_node.next
                
                current_node = current_node.next
            
            return head
        
        #実装部分
        if l1 is None and l2 is None:
            return
        
        elif l1 is None and l2 is not None:
            return sort(l2)
        
        elif l1 is not None and l2 is None:
            return sort(l1)
        
        else:
            head1 = l1
            head2 = get_list(l2)
            merge_head = merge(head1,head2)
            return sort(merge_head)

                
