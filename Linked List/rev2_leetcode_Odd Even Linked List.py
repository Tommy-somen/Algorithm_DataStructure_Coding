# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #後方にappendする_ADD関数の作成
        def _ADD(head, node, data):
            
            new_node = ListNode(data)
            
            if head is None:
                return 
            
            #-->rev2. 計算量を減らすために、引数nodeで最後尾のnodeをもらうように変更する。
            node.next = new_node
            return

        

        #ダミーノードの作成とheadへの連結
        dummy_node = ListNode(None)
        dummy_node.next = head
        new_list = dummy_node
        current_node = new_list
        
        #一時格納用のリスト
        temp_list = []
        #cntが偶数の時にtemp_listにvalをappendしておく
        cnt = 0
       
        #先頭から走査していき、cnt%2==0でtemp_listに格納し、new_listからremoveする
        while current_node.next:
            next_node = current_node.next
            cnt += 1
            if cnt%2 == 0:
                temp_list.append(int(current_node.next.val))
                current_node.next = next_node.next
            else:
                current_node = next_node
        
        #temp_listのvalについて、_ADD関数を適用し、new_listへappendする
        #-->rev2. 先にnew_listの最後尾を用意してあげる ->上のwhileでbreakしたcurrent_nodeを利用する。
        for val in temp_list:
            _ADD(new_list,current_node,val)
            #-->rev2. current_nodeを更新して次の処理に引き渡す
            current_node = current_node.next

        return new_list.next
