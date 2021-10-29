"""
【二分探索木】

Rootを起点に、
2つ以内のノードへリンクする木構造。
親ノードに対し、左側のノードは、親ノードの値よりも小さく、
親ノードに対し、右側のノードは、親ノードの値以上のものを格納していく。

       | root |
      /        \
    /           \
 |root < val| |val <= root |
 /      \       /       \


"""
#Nodeに関するクラス
class Node():
     
     #初期化 --> Nodeのデータであるval, 左先ノード:left(初期値None), 右先ノード:right(初期値None)
     def __init__(self, val):
         self.val = val
         self.left = None
         self.right = None

class BinarySearchTree():

    def __init__(self):
        self.root = None
        
    #insert functionn --> ノードに対して、ノードを階層的に追加していく関数
    def insert(self,val):
        #引数親ノードのvalに何も含まれていないとき

        if self.root is None:
            #nodeを作成する
            self.root = Node(val)
            return

        def _insert(parent_node, val):

            if parent_node is None:
                return Node(val)
 
            #すでに親ノードが存在する場合の処理
            #１. nodeのvalが親のvalよりも小さい場合 --> 左に追加する。ノードは親ノード.left
            if val < parent_node.val:
                parent_node.left = _insert(parent_node.left, val)
            #2. nodeのvalが親のval以上の場合 --> 右に追加する。ノードは親ノード.right
            else:
                parent_node.right = _insert(parent_node.right, val)

            return parent_node
        
        _insert(self.root,val)


    #root_nodeを引数にすると、構造内のvalを小さい順に出力する
    #Inorder順に出力する
    def order_print(self):

        def _order_print(node):
            if node is not None: #ノードがあるなら
                _order_print(node.left) #ノードの左側を探索する
                print(node.val) #左探索が終了したら自分自身の値を出力する
                _order_print(node.right) #右側にも同様に行う
            else:
                return #何もなければreturn

        _order_print(self.root)


    #search関数 --> 比較するノードと比べて、等しいか、小さいか、大きいかによって
    #再帰関数にノードの行先を指定することで、高速に検索を行う。
    #どの探索にも引っ掛からず、ノードがNoneのところまで来ると検索不能により、Falseを返す。
    def search(self,target):

        def _search(node, target):
            
            #再帰関数が繰り返されて、行き場がなくなるとFalseを返す
            if node is None:
                return False
            
            #node.valとtargetが等しければTrueを返す
            if node.val == target:
                return True
            
            #次の探索に向けて、現在の値とtargetを比較して、右を探索するか、左にするかを決める
            elif target < node.val:
                return _search(node.left, target)

            else:
                return _search(node.right, target)
        
        return _search(self.root, target)


    #最も小さい値を出力する
    def min_value(self):

        def _min_value(node):
            current = node
            while current.left is not None:
                current = node.left
            
            return current.val

        return _min_value(self.root)

    #remove関数
    def remove(self,target):

        def _remove(node, target):
            if node is None:
                return node

            if target < node.val:
                node.left = _remove(node.left,target)

            elif target > node.val:
                node.right = _remove(node.right, target)

            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left

                tmp = self.min_value(node.right)
                node.val = tmp.val
                node.right = _remove(node.right, tmp.val)
            
            return node
        
        _remove(self.root,target)



####実装####

if __name__ == "__main__":
    #root_nodeの作成(初期値はNone)
    root_node = BinarySearchTree()
    root_node.insert(3)
    root_node.insert(1)
    root_node.insert(2)
    root_node.insert(5)
    root_node.insert(7)
    root_node.insert(10)
    root_node.insert(9)
    root_node.insert(8)
    root_node.insert(13)
    #print(root_node.val) #root_node >> 3
    #print(root_node.right.val) #root_nodeから右のノード >> 5
    #print(root_node.left.val) #root_nodeから左のノード >> 1
    #print(root_node.left.right.val) #root_nodeから左のノードのさらに右ノード >> 2

    root_node.order_print()
    root_node.remove(5)
    print("################")
    root_node.order_print()
    #print(root_node.search(5))
    #print(root_node.min_value())
