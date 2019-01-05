#讀取檔案
def read_file(filename):
    data = []
    count = 0
    with open(filename, "r") as f:
        for line in f:
            data.append(line)
            count += 1
            if count % 1000 == 0:
                print(len(data))
    print("檔案讀取完了，總共有：", len(data), "筆資料！")
    return data

#統計資料
def count_result(data):
    sum_len = 0
    for d in data:
        sum_len += len (d)
    print("留言的平均長度是", sum_len/len(data))


    new = []
    for d in data:
        if len(d) < 100:
            new.append(d)
    print("一共有", len(new), " 筆留言長度小於100")
    #print(new[0])
    #print(new[1])


    good = []
    for d in data:
        if "good" in d:
            good.append(d)
    print("一共有", len(good), " 筆留言提到good")
    #print(good[0])
    #good = [d for d in data if "good" in d]

def word_count(data):
    while True:
        word = input("請輸入欲統計的關鍵詞(離開請輸入q)： ")
        if word == "q":
            break
        new = []
        for w in data:
            if word in w:
                new.append(w)
        print("一共有", len(new), " 筆留言提到",word)
        while True:
            order = input("想查閱第幾筆留言呢？(離開請輸入q) ")
            if order == "q":
                break
            elif type(order) != int:
                print("請輸入數字")
            else:
                print(new[int(order)-1])
                print("一共有", len(new), " 筆留言提到",word)
    print("感謝使用本查詢功能")

#文字計數
def word_search(data):
    wc = {} #word_count
    for d in data:
        words = d.split()
        for word in words:
            if word in wc:
                wc[word] += 1
            else:
                wc[word] = 1 #新增key

    for word in wc:
        if wc[word] > 1000000:
               print (word, wc[word])
    print (len(wc))

    #查詢文字功能
    while True:
            word = input("請問你想查什麼字？(離開請輸入q)")
            if word == "q":
                break
            if word in wc:
                print(word, "出現過的次數為: ", wc[word])
            else:
                print("這個字沒有出現喔！")
    print("感謝使用本查詢功能")

def main():
    data = read_file("reviews.txt")
    count_result(data)
    word_search(data)
    word_count(data)

main()