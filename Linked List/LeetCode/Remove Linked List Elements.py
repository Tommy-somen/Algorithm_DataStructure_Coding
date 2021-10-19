# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        #1つ前のノードがNoneだとエラーになるため、ダミーノードを追加する
        new_node = ListNode(None)
        #headに連結させる
        new_node.next = head
        new_list = new_node
        
        current_node = new_list
        
        #現在ノードの次ノードを確認する
        while current_node.next:
            #1つ先のノードを取得する
            next_node = current_node.next
            
            #1つ先のノードが一致していたら、現在ノードのnextをnext_node.nextに書き換える
            if next_node.val == val:
                #現在ノードの次の行き先を、next_nodeの行き先に書き換える ->whileで自動的に次のノードを参照してくれる
                current_node.next = next_node.next
            else:
                #変更がなければ次ノードへ
                current_node = next_node
                
        #ダミーノードを除いたLikedListを返す
        return new_list.next
