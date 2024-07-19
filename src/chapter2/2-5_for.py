# リストをforでprintする
hsn = ["ゆう", "ひと", "じん", "よう", "みう"]
for human in hsn:
    print(human)

# 分数の計算
monk_fish_team = [158, 157, 163, 157, 145]
total = sum(monk_fish_team)
length = len(monk_fish_team)
mean = total / length

variance = 0

for height in monk_fish_team:
    variance += (height - mean) ** 2

variance = variance / length
print(variance)

# 標準偏差
print(variance**0.5)
