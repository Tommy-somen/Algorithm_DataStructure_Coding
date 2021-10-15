"""
線形探索

先頭から走査して、valueと一致するものがあれば、そのインデックスを返す
"""

#linear_searchの実装
def liner_search(numbers, value):
  for i in range(len(numbers)):
    if numbers[i] == value:
      return i
  
  #一致するものがないなら
  return -1


  
