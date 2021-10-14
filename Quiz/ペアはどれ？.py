def calc(pairs):

  dic = {}
  ans = []

  for item in pairs:
    l = list(item)
    l.sort()
    w1,w2 = str(l[0]), str(l[1])
    hashed = w1+w2
    if dic.get(hashed) == None:
      dic[hashed] = 1
    else:
      ans.append((int(w1), int(w2)))
    
  return ans

print(*calc([(1,2), (2,3), (4,5), (3,2), (4,7), (2,1)]))
