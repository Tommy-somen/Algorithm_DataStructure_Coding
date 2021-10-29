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


#insert functionn --> ノードに対して、ノードを階層的に追加していく関数
def insert(parent_node, val):
    
    #引数親ノードのvalに何も含まれていないとき
    if parent_node is None:
        #nodeを作成する
        return Node(val)
    
    #すでに親ノードが存在する場合の処理
    #１. nodeのvalが親のvalよりも小さい場合 --> 左に追加する。ノードは親ノード.left
    if val < parent_node.val:
        parent_node.left = insert(parent_node.left, val)
    #2. nodeのvalが親のval以上の場合 --> 右に追加する。ノードは親ノード.right
    else:
        parent_node.right = insert(parent_node.right, val)

    return parent_node

#root_nodeを引数にすると、構造内のvalを小さい順に出力する
#Inorder順に出力する
def order_print(node):


    if node is not None: #ノードがあるなら
        order_print(node.left) #ノードの左側を探索する
        print(node.val) #左探索が終了したら自分自身の値を出力する
        order_print(node.right) #右側にも同様に行う
    else:
        return #何もなければreturn


#search関数 --> 比較するノードと比べて、等しいか、小さいか、大きいかによって
#再帰関数にノードの行先を指定することで、高速に検索を行う。
#どの探索にも引っ掛からず、ノードがNoneのところまで来ると検索不能により、Falseを返す。
def search(node, target):
    
    #再帰関数が繰り返されて、行き場がなくなるとFalseを返す
    if node is None:
        return False
    
    #node.valとtargetが等しければTrueを返す
    if node.val == target:
        return True
    
    #次の探索に向けて、現在の値とtargetを比較して、右を探索するか、左にするかを決める
    elif target < node.val:
        return search(node.left, target)

    else:
        return search(node.right, target)
    

####実装####

if __name__ == "__main__":
    #root_nodeの作成(初期値はNone)
    root_node = None

    root_node = insert(root_node, 3)
    root_node = insert(root_node, 1)
    root_node = insert(root_node, 5)
    root_node = insert(root_node, 2)

    #print(root_node.val) #root_node >> 3
    #print(root_node.right.val) #root_nodeから右のノード >> 5
    #print(root_node.left.val) #root_nodeから左のノード >> 1
    #print(root_node.left.right.val) #root_nodeから左のノードのさらに右ノード >> 2

    #order_print(root_node)
    print(search(root_node, 5))
