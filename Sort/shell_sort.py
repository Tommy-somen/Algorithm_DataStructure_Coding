"""
【シェルソート】

挿入ソートでは、未整列の中から1つずつずらして
並び替え比較を実施していたものを、
一定の間隔で効率的に並び替えるよう改良されたソート

・リストの長さ//2でgapを求める→間隔として扱う
・gapを指標にして間隔間で比較をする。
一度並び替えが発生した場合は、さらに先頭まで等間隔さかのぼり、並び替えを行う（挿入ソートの活用）
・一巡したらgapを gap//2で更新して、gapが0になるまで繰り返す。 

"""

import random

#シェルソートの実装
def shell_sort(numbers):
  #gapの定義
  gap = int(len(numbers)/2)
  #長さを取得
  len_numbers = len(numbers)

  #gapが0になるまで繰り返す
  while gap > 0:
    
    #[gap]からスタートし、[i],[i-gap]で比較する
    #この辺から挿入ソートの活用
    #1つずらすのではなく、gapでずらして査走する。
    for i in range(gap,len_numbers):

      tmp = numbers[i]
      j = i - gap
      
      while j >= 0 and numbers[j] > tmp:
        
        numbers[j+gap] = numbers[j]
        j -= gap
  
      numbers[j+gap] = tmp

    gap = gap//2

  return numbers
		
if __name__ == "__main__":
	num = [random.randint(0,100) for _ in range(10)]
	print(shell_sort(num))
