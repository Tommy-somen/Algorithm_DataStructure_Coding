# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:   
        
        #check関数 --> 重複しているかをdictに格納している情報をもとに確認する。
        #重複していなければTrue、していればFalseを返す
        def check(val):
            
            global check_dict 
            
            #ないとき
            if check_dict.get(val) == None:
                check_dict[val] = 1
                return True
            
            #あるとき
            else:
                return False
            
        
        
        #remove関数　--> ノードを削除する関数
        def remove(previous_node, current_node):
            
            previous_node.next = current_node.next
            
            return
        
        
        ##########実装############
        
        if head is None:
            return
        
        
        #ダミーノードの作成
        new_node = ListNode(None)
        
        #headとの接続
        new_node.next = head
        new_head = new_node
        
        global check_dict
        check_dict = {}
        check_dict[new_node.val] = 1
        
        previous_node = new_head
        current_node = new_node.next
        
        while current_node.next:
            next_node = current_node.next
            
            if not check(current_node.val):
                remove(previous_node, current_node)
                next_node = previous_node.next
                current_node = next_node
                
            else:
                previous_node = current_node
                current_node = next_node
        
        if not check(current_node.val):
            remove(previous_node, current_node)
                
        return new_head.next
   
