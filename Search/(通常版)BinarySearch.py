"""
二分探索

線形探索よりも効率的な探索アルゴリズムで、
center, left, rightの変数によって、
centerより小さいか大きいか、を比較し、
探索範囲を狭めていきながら探索する

"""

def binary_search(numbers, value):
    
    left = 0
    right = len(numbers)-1

    while left <= right:
        
        #leftとrightの中間点centerを設定
        center = (left+right)//2

        #centerが探索対象かどうかを判断する。
        if numbers[center] == value:
            return center
        #centerよりも大きいときは、探索範囲を狭めるためにleftをcenter+1に設定する
        elif numbers[center] < value:
            left = center+1
        #centerよりも小さいときは、探索範囲を狭めるためにrightをcenter-1に設定する
        else:
            right = center-1
            
    #何もなかったら-1を返す
    return -1
