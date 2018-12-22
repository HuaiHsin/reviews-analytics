data = []
count = 0
with open("reviews.txt", "r") as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
print("檔案讀取完了，總共有：", len(data), "筆資料！")

"""
sum_len = 0
for d in data:
    sum_len += len (d)

print("留言的平均長度是", sum_len/len(data))

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print("一共有", len(new), " 筆留言長度小於100")
print(new[0])
print(new[1])

good = []
for d in data:
	if "good" in d:
		good.append(d)
print("一共有", len(good), " 筆留言提到good")
print(good[0])
"""

#good = [d for d in data if "good" in d]

while True:
	word = input("請輸入欲統計的關鍵詞： ")
	new = []
	for w in data:
		if word in w:
			new.append(w)
	print("一共有", len(new), " 筆留言提到",word)
	while True:
		order = input("想查閱第幾筆留言呢？(離開請輸入q)")
		if order == "q":
			break
		else:
			print(new[int(order)-1])
			print("一共有", len(new), " 筆留言提到",word)
		"""
		else:
			print("查無資料")
			break
			"""
