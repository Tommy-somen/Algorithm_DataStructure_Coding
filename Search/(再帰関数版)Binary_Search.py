"""
二分探索

再帰関数を利用する場合
"""

def binary_search(numbers, value):
  
  #内部関数を作成する########################################
  def _binary_search(numbers, value, left, right):
    
    #左が右を越してしまった場合＝見つからなかったとき
    if left > right:
      return -1
    
    #centerの設定  
    center = (left+right)/2
    
    #valueならcenterを返す
    if numbers[center] == value:
      return center
    #centerより大きければ、leftを修正して再起する
    elif numbers[center] < value:
      _binary_search(numbers, value, center+1, right)
    
    #centerより小さければ、rightを修正して再起する
    else:
      _binary_search(numbers, value, left, center-1)
  #ここまで内部関数#########################################
  
  #入力値の設定
  left = 0
  right = len(numbers)-1
  
  return _binary_search(numbers, value, left, right)
