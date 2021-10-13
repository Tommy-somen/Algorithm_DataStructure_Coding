"""
【コムソート】

・リストの長さをGapとして設定する
・毎回Gapを割るDivider = 1.3を設定する。
・リストを査走するときに、Interval = Gap//Dividerの間隔で比較する。
(e.g.)Intervalが5なら、[0]と[5], [1]と[6]...などのように

・査走が終了すると、Interval = Interval//Dividerと更新して、同様の処理を行う。
・Intervalが1になるまで上記を繰り返す。

・Intervalが1になったとき、swapがFalseになるまで先頭から査走する。
・swapした場合はTrueにして、再度繰り返し査走＆ソートする。
"""

import random

def comb_sort(numbers):

    gap = len(numbers)
    divider = 1.3

    interval = int(gap/divider)

    #gap(len(numbers)) --> 1
    while interval > 1:
        
        for i in range(0, len(numbers)-interval):
            #先頭から後方にかけて、左が大きいときに並び替える
            if numbers[i] > numbers[interval]:
                numbers[i], numbers[interval] = numbers[interval], numbers[i]     
        interval = int(interval/divider)

    #swap = Falseになるまで査走
    swap = True

    while swap:

        swap = False

        for j in range(len(numbers)-1):
            #先頭から後方にかけて、左が大きいときに並び替える
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                swap = True
    
    return numbers   

print(comb_sort([random.randint(0,100) for _ in range(10)]))

#ここから自分用############################
#sort関数でソートした結果と、自作bubble_sortの結果を比較するcheck関数

def check(numbers):
    combsort = comb_sort(numbers)
    
    truesort = sorted(numbers)

    if truesort == combsort:
        print("正しくソートされています")
    else:
        print("正しくソートされていません")

#checkする
if __name__ == "__main__":
    nums = [random.randint(0,100) for _ in range(10)]
    check(nums)
