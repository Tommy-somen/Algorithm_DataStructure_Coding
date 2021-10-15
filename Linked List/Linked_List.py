"""
【Linked List】片方向連結リスト

HEAD -> | data , next | -> | data , next | -> ... -> None
というデータ構造

| data , next | ... Nodeと呼ばれる部分

"""

#Nodeクラスを作成
class Node():


    #__init__初期化
    def __init__(self,data, next_node=None):
        self.data = data
        self.next = next_node




#LinkedList全体のクラスを作成
class LinkedList():


    #LinkedListに何もないとき、head=Noneとして初期化
    def __init__(self,head=None):
        self.head = head


    #append関数の作成
    def append(self, data):
        new_node = Node(data)
        #もしノードがひとつもない時は、appendされたデータをheadにする
        if self.head == None:
            self.head = new_node
            return 
    
        #他にノードがある時、後方に追加するため、以下の処理を行う。
        #最後尾のノードとしてlast_nodeを作成し、既存のself.haedを代入する
        last_node = self.head
        #whileで先頭から走査し、.nextがNoneになるまで探索する。
        while last_node.next:
            #探索するたびに、last_nodeに各データ.nextを格納しておく
            last_node = last_node.next
        #.nextがNoneになり、whileからbreakしたときに、 次のnew_nodeを作成する。
        last_node.next = new_node


    #insert関数の作成（先頭に挿入するとき）
    def insert(self, data):
        #new_nodeを作成する
        new_node = Node(data)
        #new_nodeのnextとして現在のhead（先頭）を入れる
        new_node.next = self.head
        #現在のheadをnew_nodeに置き換える
        self.head = new_node


    #print関数を作成する(linkedlistの中身を見るときに、
    #いちいち.next.next...は面倒なので、先頭からデータを出力する)
    def print(self):
        #現在ノードとしてcurrent_nodeを作成し、headを格納する。
        current_node = self.head

        #whileでheadからNoneになるまで走査し、printする
        while current_node:
            print(current_node.data)
            #current_nodeを次の行先に更新する
            current_node = current_node.next


    #データを削除するremove関数の作成
    def remove(self, data):

        #現在ノードとしてcurrent_nodeを作成し、headを格納する
        current_node = self.head

        #もしもheadが削除対象の場合(current_nodeがある、かつデータが同じとき)
        if current_node and current_node.data == data:
            #headをheadの次のデータに変更する
            self.head =  current_node.next
            
            #current_nodeは不要なので、Noneにする
            current_node = None
            return
        
        #linkedlistの中に対象がある場合
            #previous_nodeは、cuurent_nodeを削除した場合に、ひとつ前のnode.nextと、
            #current_node.nextのデータを繋ぐ必要があるため用意する
        previous_node = None

        #whileによりデータを走査する(同じデータでない限り進む)
        while current_node and current_node.data != data:
            #previous_nodeを更新
            previous_node = current_node
            #current_nodeに次の行先をインプット
            current_node = current_node.next

        #whileからbreak後の処理
        #1. current_nodeがNoneになったとき（＝対象のデータがないとき）
        if current_node is None:
            return

        #2.current_nodeが対象のデータの時
        #1つ前のノードprevious_nodeの行先を、現在ノードの行先に更新する
        previous_node.next = current_node.next
        #不要になったcurrent_nodeをNoneに更新する
        current_node = None


#上記のクラスを呼び出して試してみる
if __name__ == "__main__":
    #LinkedListを作成
    linkedlist = LinkedList()

    #1をappend
    linkedlist.append(1)
    linkedlist.append(2)
    linkedlist.append(3)
    linkedlist.insert(0)

    #・print(linkedlist.head.data) #headのデータが出力
    #・print(linkedlist.head.next.data) #headの次の数字が出力
    #・print(linkedlist.head.next.next.data) #headから２番目のデータ
    linkedlist.print() #>>print関数により、上記の手間が省ける
    print("###############")
    linkedlist.remove(2)
    linkedlist.print() #>>2が削除され、1 -> 3となっている
