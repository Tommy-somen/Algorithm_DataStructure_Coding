"""
【選択ソート】

・スタート位置はlimit_head = 0と設定する。
・リストの先頭から後方にかけて査走する。
・先頭をtmpに格納し、査走する。
・tmpより小さい数字を発見すると、tmpを更新する。
・査走が終わると、先頭とtmpを入れ替える。
・limit_haedをインクリメントして再び査走する。
"""
import random

#選択ソートの実装
def select_sort(numbers):
    
    limit_head = 0

    #limit_headがlen(numbers)になるまで査走する。
    while(limit_head < len(numbers)):

        #先頭をtmpに格納する
        tmp = numbers[limit_head]
        #先頭のindexも格納する
        tmp_index = limit_head

        #tmpより小さい数字が発見されたとき、tmpとindexを更新する
        for i in range(limit_head+1, len(numbers)):
            if tmp > numbers[i]:
                tmp = numbers[i]
                tmp_index = i
        
        #最終的に並び替える
        numbers[limit_head], numbers[tmp_index] = numbers[tmp_index], numbers[limit_head]
        #limit_headをインクリメントする
        limit_head += 1

    return numbers

print(select_sort([random.randint(0,100) for _ in range(10)]))

#ここから自分用############################
#sort関数でソートした結果と、自作select_sortの結果を比較するcheck関数

def check(numbers):
    selectsort = select_sort(numbers)
    
    truesort = sorted(numbers)

    if truesort == selectsort:
        print("正しくソートされています")
    else:
        print("正しくソートされていません")

#checkする
if __name__ == "__main__":
    nums = [random.randint(0,100) for _ in range(10)]
    check(nums)
