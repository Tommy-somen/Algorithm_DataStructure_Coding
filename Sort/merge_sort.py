"""
【マージソート】

リストを前半後半で分割し、それを1要素になるまで分割し続け、再びマージするときに並び替える。
これを1つのリストになるまで繰り返す。

・再帰関数により、リストの要素が1つになるまで分割する。
・分割後はマージしながら並び替えを実施する。
・インデックス管理変数としてi,j,kを用意する。
・iはマージする左側,　jは右側, kはマージするときの空リストのインデックス。
・new_list[k]にleft[i]を入れるか、right[j]を入れるかを判断してマージしていく。
・挿入した方はインクリメントして次の要素を判断材料にする。
・上記を繰り返して、マージしていく。
"""

#merge_sortの実装
def merge_sort(numbers):

    #要素が1つになるまで再帰的に呼び出して分割する
    if len(numbers) <= 1:
        return numbers
    
    #リストに複数要素ある場合の処理
    else:
        #centerによって分割点を決める
        center = len(numbers)//2
        #左と右に要素を分割する
        left = numbers[:center]
        right = numbers[center:]
    
    #左と右に対して、再帰的に分割を進める
    merge_sort(left)
    merge_sort(right)

    #whileにより、leftとrightをマージしていく
    #i, j, k を用意する
    i = 0
    j = 0
    k = 0

    #i, jがリストの要素数内であるとき
    while i < len(left) and j < len(right):
        #print(numbers,left,right)
        #どちらが小さいかを確認し、小さい方をリストのk番目に挿入する
        if left[i] >= right[j]:
            numbers[k] = right[j]
            j += 1
        else:
            numbers[k] = left[i]
            i += 1
        #次のk番目に入れるため、インクリメントする
        k += 1
        #print(numbers)

    #このままだと、入りきれていない片方のリストがあるため、それを入れ切る
    #leftに余がある場合
    while i < len(left):
        #print(numbers,left,right)
        numbers[k] = left[i]
        i += 1
        k += 1
        #print(numbers)

    #rightに余りがある場合
    while j < len(right):
        #print(numbers,left,right)
        numbers[k] = right[j]
        j += 1
        k += 1
        #print(numbers)

    return numbers

    
if __name__ == "__main__":
    import random
    num = [random.randint(0,100) for _ in range(10)]
    print(merge_sort(num))
