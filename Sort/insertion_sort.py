"""
【挿入ソート】

数値の列を先頭から小さい順（昇順）に並べる場合を考える。
まず、先頭から2つの値を比較して小さい方を先頭に、大きい方を2番目に置く。次に3番目の値を取り出し、
先頭・2番目と順に比較し、適切な位置に挿入する。

"""
import random

def insertion_sort(numbers):
    
    len_numbers = len(numbers)
    
    for i in range(1,len_numbers):
        tmp = numbers[i]
            
        j = i -1
        while j >= 0 and numbers[j] > tmp:
            numbers[j+1] = numbers[j]
            j -= 1
    
        numbers[j+1] = tmp
        
    return(numbers)

print(insertion_sort([random.randint(0,100) for _ in range(10)]))

#ここから自分用############################
#sort関数でソートした結果と、自作insertion_sortの結果を比較するcheck関数

def check(numbers):
    insertionsort = insertion_sort(numbers)
    
    truesort = sorted(numbers)

    if truesort == insertionsort:
        print("正しくソートされています")
    else:
        print("正しくソートされていません")

#checkする
if __name__ == "__main__":
    nums = [random.randint(0,1000) for _ in range(10)]
    check(nums)
