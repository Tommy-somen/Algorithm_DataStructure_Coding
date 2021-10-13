"""
【ボゴソート】

非常に効率の悪いソートアルゴリズム
1. データをランダムに並び替える List -> List
2. ソート済かどうかを判断する List -> Bool
3. 適切にソートされるまで繰り返す。ソートされたらそのListを返す。Bool -> List

遅すぎ。
"""

import random

#リスト(変数:numbers)を引数として受け取り、ソートの順序を判断する
    #左の要素が、右の要素より大きい場合はFalseを返す。
def in_order(numbers) -> bool:
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            return False
    return True

#ボゴソートの実装
    #適切にソートされるまで、numbersをシャッフルする。適切にソートされると、そのリストを返す。
def bogo_sort(numbers) -> list[int]:
    while not in_order(numbers): #Falseが返される間は繰り返す。
        random.shuffle(numbers)
    return numbers

#関数の実行
if __name__ == "__main__":
    #引数になるLits[int]を作成する。手打ち or random.randintで作成する。
    nums = [random.randint(0,100) for _ in range(10)]
    print(bogo_sort(nums))
