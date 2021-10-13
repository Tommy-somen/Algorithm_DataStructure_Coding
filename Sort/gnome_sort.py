"""
【ノームソート】

バブルソートと類似のソート方法。
隣同士を比較して、問題なければそのまま後方へ進む。
適切に並んでいなかった場合、並び替えを行い、1つ前にインデックスを戻す。
これを繰り返し、最後尾に到達するまで処理を繰り返す。

"""

import random

#ノームソートの実装
def gnome_sort(numbers):

    len_numbers = len(numbers)
    index = 0

    #indexが最後尾に行くまで繰り返す。
    while index < len_numbers:

        if index == 0:
            index += 1
        
        if numbers[index] >= numbers[index-1]: #右が左よりも大きいとき（適切に並んでいる場合）
            index += 1 #並び替えをせず、先に進める

        else:#適切に並んでいなかった場合は並び替えを行い、一つ前に戻る
            numbers[index], numbers[index-1] = numbers[index-1], numbers[index]
            index -= 1

    return numbers

print(gnome_sort([random.randint(0,100) for _ in range(10)]))

#ここから自分用############################
#sort関数でソートした結果と、自作bubble_sortの結果を比較するcheck関数

def check(numbers):
    gnomesort = gnome_sort(numbers)
    
    truesort = sorted(numbers)

    if truesort == gnomesort:
        print("正しくソートされています")
    else:
        print("正しくソートされていません")

#checkする
if __name__ == "__main__":
    nums = [random.randint(0,100) for _ in range(10)]
    check(nums)
