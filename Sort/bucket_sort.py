"""
【バケットソート】

insertion_sortを活用したソート方法。

あらかじめデータがとりうる値すべての容器(バケット)を順番どおりに並べて用意しておき、
値を対応する容器に移すことでソートを行う整列アルゴリズムです。

データがとりうる値がわかっていなければソートのためのバケット [Bucket] を
準備することができないのでこのアルゴリズムは使えません。比較を用いない整列アルゴリズムです。

アルゴリズム分析
前提としてソート対象のデータは 1 から 10 の整数とします。

1 から 10 に対応する10個のバケットを順に並べて用意する
データを対応するバケットに入れる
バケットから順にデータを取り出す
このような方法で整列されたデータを得ることができます。

ソート対象のデータは必ず10個存在するとは限りません。
1 から 5 までの5個しかデータがなくてもバケットは10個用意する必要があります。
6 から 10 のバケットはデータを取り出す際に無視することで 1 から 5 のデータだけを整列させるのです。
"""
import random

#insertion_sortの関数
def insertion_sort(numbers):
    
    len_numbers = len(numbers)
    
    for i in range(1,len_numbers):
        tmp = numbers[i]
            
        j = i -1
        while j >= 0 and numbers[j] > tmp:
            numbers[j+1] = numbers[j]
            j -= 1
            
        numbers[j+1] = tmp
    return numbers

#bucket_sortの実装
def bucket_sort(numbers):

    #最大値の取得
    max_num = max(numbers)

    #リストの長さの取得
    len_numbers = len(numbers)

    #bucketのサイズを最大値//長さと定義する
    size = max_num // len_numbers

    #bucketの作成
    buckets = [[] for _ in range(size)]

    #numbersの中身をバケットに振り分ける。
    for num in numbers:

        #numをsizeで割り、その値によって振り分け先のバケットを決定する。
        x = num//size

        if x != size:
            buckets[x].append(num)
        else:
            buckets[size-1].append(num)

    #振り分けたバケットの中身をinsertion_sortする
    for y in range(size):
        insertion_sort(buckets[y])

    #result[]に、ソートされたバケットの中身を追加する。
    result = []

    for k in range(size):
        result += buckets[k]

    return result

#ここから自分用############################
#sort関数でソートした結果と、自作bucket_sortの結果を比較するcheck関数

def check(numbers):
    bucketsort = bucket_sort(numbers)
    
    truesort = sorted(numbers)

    if truesort == bucketsort:
        print("正しくソートされています")
    else:
        print("正しくソートされていません")

#checkする
if __name__ == "__main__":
    nums = [random.randint(0,1000) for _ in range(10)]
    check(nums)
