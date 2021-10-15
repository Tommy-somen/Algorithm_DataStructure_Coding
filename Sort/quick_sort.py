"""
【クイックソート】

最後尾の数字をピボットとして扱い、それを軸に走査し、
ピボットの左右に大小のグルーピングを行う。
そして、左右の要素について、同様の処理を行い、
全体的なソートを実施する。

・最後尾をピボットとする
・ピボットをベースに先頭から走査する
・インデックス変数でi =先頭-1、と、ループ変数をjとする
・要素<ピボットの時、i += 1を行い、iとjをスワップする
・要素>ピボットの時は、無視する
・一巡し終わったら,左右について同様の処理を実施

"""

import random

#iやjに関する走査処理を行い、
#ピボットであった数字が最終的にどこにいるのかのインデックスを返す関数
#numbersは受け取るリスト、lowは先頭インデックス、highは最後尾のインデックス
def partition(numbers, low, high):

    i = low-1
    pivot = numbers[high-1]

    for j in range(low, high-1):
        if numbers[j] <= pivot:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]

    #最後尾はピボットなので、自分自身と比較をしてしまうため別途走査処理を追加する。
    #今まで蓄積したi番目の次にピボットが来るため、i+1にピボットを挿入する。
    numbers[i+1], numbers[high-1] = numbers[high-1], numbers[i+1]

    #ピボットのいるインデックスを返す
    return i+1

#quick_sortの実装
def quick_sort(numbers):

    #内部関数を作成する -> ピボットの左右について同様にソートをするため
    def _quick_sort(numbers, low, high):

        if low < high:
            #numbersの初期並び替え & ピボットのインデックス取得
            partition_index = partition(numbers, low, high)
            
            #ピボットの左側（小さいほう：昇順なら）をソート
            _quick_sort(numbers, low, partition_index)
            #ピボットの右側（大きいほう：〃）をソート
            _quick_sort(numbers, partition_index+1, high)

    _quick_sort(numbers, 0, len(numbers))

    return numbers

if __name__ == "__main__":
    num = [random.randint(0, 100) for _ in range(10)]
    print(quick_sort(num))
