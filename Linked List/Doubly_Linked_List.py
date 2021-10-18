"""
【Doubly Linked List】両方向連結リスト

HEAD -> | prev, data , next | -> | prev, data , next | -> ... -> None
というデータ構造

| prev,  data , next | ... Nodeと呼ばれる部分

"""

#Node classの作成(prev, data, next)
from typing import Counter


class Node():
    def __init__(self, data, prev_node=None, next_node=None):
        self.data = data
        self.prev = prev_node
        self.next = next_node


#DoublyLinkedList classの作成
class DoublyLinkedList():

    #初期化
    def __init__(self, head=None):
        self.head = head

    #append関数
    def append(self, data):
        
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next

            current_node.next = new_node
            new_node.prev = current_node
    
    #print関数
    def print(self):

        if self.head is None:
            return None

        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

   #print_more関数
    def print_more(self):

        if self.head is None:
            return None

        #head
        print("data :", self.head.data)
        print("next :", self.head.next.data)
        print("################")

        #in
        current_node = self.head.next
        while current_node.next:

            if current_node.prev.data is not None:
                print("prev: ",current_node.prev.data)
            else:
                print("prev :","None")
            
            print("data: ",current_node.data)
            
            if current_node.next.data is not None:
                print("next: ",current_node.next.data)
            else:
                print("next :","None")
            
            print("################")
            current_node = current_node.next
        
        #tail
        print("prev :", current_node.prev.data)
        print("data :", current_node.data)
        print("################")         

    #insert関数
    def insert(self,data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    #remove関数
    def remove(self,data):

        current_node = self.head

        #1. headが対象の時
        if current_node and current_node.data == data:
            self.head = current_node.next
            self.head.prev = None
            current_node = None
            return

        #2. linkedlistの中身の場合
        previous_node = None
        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next

        #何も発見できなかった時
        if current_node is None:
            return
        
        #発見した時
        previous_node.next = current_node.next
        current_node.next.prev = previous_node
        current_node = None

    #reverse関数(iteration)
    def reverse_iteration(self):

        #current_nodeをheadに初期化
        current_node = self.head
        #head.prevはNoneなので設定
        previous_node = None

        #current_node existsの時
        while current_node:
            #previous_nodeに現在ノードの1つ前を設定(nextに代入するための退避)
            previous_node = current_node.prev
            #現在ノードのprevを本来次来るはずのnextに変更
            current_node.prev = current_node.next
            #現在ノードのnextを本来のprevに変更
            current_node.next = previous_node

            #previous_nodeに現在ノードを格納
            previous_node = current_node
            #current_nodeを1つ先に進める
            current_node = current_node.prev
        
        #current_nodeがNoneまできてbreakした後、
        #最後ノードであったprevious_nodeをheadに更新して終了。
        if previous_node:
            self.head = previous_node

    #reverse関数(再帰関数)
    def reverse_recursive(self):

        #内部関数
        def _reverse_recursive(current_node, previous_node):
            
            #内部関数の最終地点を設定 -> current_nodeがNoneまで行けばprevious_nodeを返す
            if current_node is None:
                return previous_node

            #★iterationと同様にprevious_node,prev,next,current_nodeの変更処理

            #previous_nodeに現在ノードの1つ前を設定(prev,nextを変更するための退避として)
            previous_node = current_node.prev
            #現在ノードのprevを本来次来るはずのnextに変更
            current_node.prev = current_node.next
            #現在ノードのnextを本来のprevに変更
            current_node.next = previous_node

            #previous_nodeに現在ノードを格納
            previous_node = current_node
            #current_nodeを1つ先に進める
            current_node = current_node.prev

            #新たに変更された変数で再帰関数を実施
            return _reverse_recursive(current_node, previous_node)
        
        self.head = _reverse_recursive(self.head, None)


    #LinkedListをソートする関数の作成(interview_quiz)
    def sort(self):

        if self.head is None:
            return
        
        current_node = self.head
        while current_node.next:
            next_node = current_node.next
            while next_node:
                if current_node.data > next_node.data:
                    current_node.data, next_node.data = next_node.data, current_node.data
                
                next_node = next_node.next

            current_node = current_node.next

    #自作のバブルソート
    def sort2(self):

        if self.head is None:
            return
        
        #bubble_sort
        flg = True
        while flg:

            flg = False

            header_node = self.head
            next_node = header_node.next

            while next_node:
                if header_node.data > next_node.data:
                    flg = True
                    header_node.data, next_node.data = next_node.data, header_node.data
                
                header_node = next_node
                next_node = next_node.next


if __name__ == "__main__":
    import random
    linkedlist = DoublyLinkedList()
    linkedlist.append(random.randint(0,100))
    linkedlist.append(random.randint(0,100))
    linkedlist.append(random.randint(0,100))
    linkedlist.append(random.randint(0,100))
    linkedlist.append(random.randint(0,100))
    linkedlist.append(random.randint(0,100))
    #linkedlist.print()
    print("#################")
    #linkedlist.remove(2)
    #linkedlist.reverse_iteration()
    #linkedlist.reverse_recursive()
    linkedlist.sort()
    linkedlist.sort2()
    linkedlist.print_more()
