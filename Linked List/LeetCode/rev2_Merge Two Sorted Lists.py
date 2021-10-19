#-->rev2. ソート処理を高速にする
#-->rev2. l1, l2をリストとして扱い、ビルトインのソートを利用する
#-->rev2. リストの内容を最後にLinkedListへADDする
#-->rev2. 80ms -> 53ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        def _ADD(head, last_node, val):
            
            new_node = ListNode(val)
            
            if head is None:
                head = new_node
                return
            
            else:
                last_node.next = new_node
                return
            
            
        def get_list(head):
            
            new_list = []
            
            current_node = head
            while current_node:
                new_list.append(int(current_node.val))
                current_node = current_node.next
            
            return new_list
        
        
        def get_lastnode(head):
            
            current_node = head
            while current_node.next:
                current_node = current_node.next
            
            return current_node
        
        
        def merge(head1, head2_list):
            
            for val in head2_list:
                
                last_node = get_lastnode(head1)
                
                _ADD(head1, last_node, val)
                last_node = last_node.next
            
            return head1
        
        #-->rev2. リストを取得して、マージし、ソートしたリストを返す
        def merge_list(head1, head2):
            merge_list = []
            
            list1 = get_list(head1)
            list2 = get_list(head2)
            
            merge_list = list1+list2
            
            merge_list.sort()
            
            return merge_list
            
            
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
        
        #-->rev2. headを初期化してリストの中身をADDする
        def make_head(sort_list):
            
            new_head = ListNode(None)
            new_node = new_head
            
            for val in sort_list:
                _ADD(new_head, new_node, val)
                new_node = new_node.next
                
            return new_head
        
        #-->rev2. 処理部分の変更
        if l1 is None and l2 is None:
            return
        
        else:
            new_list = merge_list(l1, l2)
            ans_head = make_head(new_list)
            return ans_head.next
