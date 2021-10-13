"""
【バブルソート】

1. 先頭から現ポイントi と次ポイントi+1で比較する
2. i > i+1の時、適切にソートされていないため、iとi+1を並び替える
3. 計算する回数limitを用意し、一巡するたびにlimitを-1する
   >>なぜなら毎回一番大きい数は一番後方に置かれるため、それ以降は考慮しなくて良い。

"""

import random

#bubble_sortの実装
def bubble_sort(numbers):

    #limitの定義
    limit = len(numbers)

    #ソート機能
    for i in range(limit): 
        for j in range(limit-1-i):
            if numbers[j] > numbers[j+1]:
                numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
    return numbers


#ここから自分用############################
#sort関数でソートした結果と、自作bubble_sortの結果を比較するcheck関数

def check(numbers):
    bubblesort = bubble_sort(numbers)
    
    truesort = sorted(numbers)

    if truesort == bubblesort:
        print("正しくソートされています")
    else:
        print("正しくソートされていません")

#checkする
if __name__ == "__main__":
    nums = [random.randint(0,100) for _ in range(10)]
    check(nums)
