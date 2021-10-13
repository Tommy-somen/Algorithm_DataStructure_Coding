"""
【カクテルソート】

bubble_sortが片方に向けてソートするのに対し、
cocktail_sortは両方向に対してソートを行う。

両端にlimit要素、limit_head, limit_tailを設定し、
先頭から後方に向けて査走を実施。
後方まで進めば、limit_tailを-1して、先頭に向けて査走を実施。
先頭まで進むと、limit_headを+1して範囲を狭めていく。

ソーティングの過程でスワップをした場合、
スワップ判定を格納するswapにTrueを格納する。
先頭または後方からの査走中に、一度もスワップがなければソートを終了する。

"""

import random

def cocktail_sort(numbers):

    limit_head = 0
    limit_tail = len(numbers)

    swap = True

    while swap:

        swap = False

        #head -> tail
        for i in range(limit_head, limit_tail-1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swap = True
        
        #tailにはもっとも大きい数が格納されているので、limitをデクリメント
        limit_tail -= 1

        #tail -> head
        for j in range(limit_tail-1, limit_head, -1):
            print(numbers[j],numbers[j-1])
            if numbers[j] < numbers[j-1]:
                numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
                swap = True

        #headには一番小さい数が格納されているはずなのでlimitをインクリメント
        limit_head += 1

        #print(numbers)

    return numbers

nums = [1,4,5,7,8,3,5,8]
print(cocktail_sort(nums))

#ここから自分用############################
#sort関数でソートした結果と、自作cocktail_sortの結果を比較するcheck関数

def check(numbers):
    cocktailsort = cocktail_sort(numbers)
    
    truesort = sorted(numbers)

    if truesort == cocktailsort:
        print("正しくソートされています")
    else:
        print("正しくソートされていません")

#checkする
if __name__ == "__main__":
    nums = [random.randint(0,100) for _ in range(10)]
    check(nums)
