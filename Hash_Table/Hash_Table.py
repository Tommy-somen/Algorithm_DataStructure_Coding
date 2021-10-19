
"""
ハッシュテーブルのアルゴリズムを実装する。
Pythonであればdict型があるが、
今回はdict型のアルゴリズムを実装。

リストを用意し、インプットした入力を
ハッシュ化したインデックスに変換する。
そのインデックスデータを格納する。

ハッシュ化には、hashlibのmb5を利用する

"""

import hashlib


class HashTable():

    #初期化
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]


    #ハッシュ化する関数
    def hash(self, key):
        #hashlib.md5(key.encode())
        #>>hashlib.md5は入力データkeyを.encode()しないとハッシュ化できない

        #hashlib.md5(key.encode()).hexdigest()
        # >>そのハッシュ化した情報を.hexdigest()で16進数の情報に変換する->文字列へ

        #int(hashlib.md5(key.encode()).hexdigest(), base=16)
        #>>16進数に変換された文字列をintに変換するときは、base=16を指定する

        #int(hashlib.md5(key.encode()).hexdigest(), base=16)%self.size
        #>>hashtableに格納しているリストの数=sizeで割ることで、
        #>>keyをhashtableにあるリストのどれかに割り振ることができる。
        return int(hashlib.md5(key.encode()).hexdigest(), base=16)%self.size


    #keyをハッシュ化したインデックスにvalueを格納するadd関数
    def add(self, key, value):
        #keyをハッシュ化したintegerをindexとして受け取る
        index = self.hash(key)
        #もしもtable内に同じkeyがあった場合は、
        #valueを更新し、なければappendする
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                break
        
        #なければtableにkey, valueをappendする
        self.table[index].append([key, value])
        return


    #keyを指定すると、valueがあるかNoneかを返すget関数
    def get(self, key):
        index = self.hash(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        
        return None


if __name__ == "__main__":
    hashtable = HashTable()
    hashtable.add("car", "Tesla")
    print(hashtable.get("car"))
    #>>Tesla
