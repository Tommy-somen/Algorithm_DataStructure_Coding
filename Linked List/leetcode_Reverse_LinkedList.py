# Definition for singly-linked list.
#class Node():
#    def __init__(self, val, next=None):
#        self.val = val
#        self.next = 
#

#class LinkedList():
#    
#    def __init__(self,head=None):
#        self.head = head
#

#LinkedListをheadという入力として受け取る
class Solution:
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.head = head
        
        #LinkedListがなければreturn
        if self.head is None:
            return
        
        #先にheadの処理をする。
        #head -> Noneと変更しておく
        current_node = self.head.next
        previous_node = self.head
        previous_node.next = None
        
        #現在ノードをcurrent_nodeとして参照しながらNoneになりまで進む
        while(current_node):
            #あらかじめ次の行先を格納しておく（後で変更するため）
            next_node = current_node.next
            
            #行先をprevious_nodeに変更する
            current_node.next = previous_node
            
            #次のステップでのprevious_nodeは現在地なので、current_nodeを格納
            previous_node = current_node      
            
            #current_nodeには予め予め退避させて置いたnext_nodeを格納
            current_node = next_node
            
        #一番最後のnodeをheadに変更して終了
        self.head = previous_node
        
        return self.head
