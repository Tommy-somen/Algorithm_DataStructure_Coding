#入力のインプット
s = list(input())

#chr()を用いて、アルファベット列を作成
alphabet = [chr(i) for i in range(97, 97+26)]

#最大カウント数とその時の文字列を格納する変数を用意。
max_count = 0
tmp_word = ""

#アルファベットをa->zで走査していく。
for word in alphabet:
  #max_countを超える文字列があれば更新する
  if s.count(word) > max_count:
    max_count = s.count(word)
    tmp_word = word

print(tmp_word, " : ",max_count)
