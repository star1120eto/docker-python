star = {
    "ニックネーム":"ほっしー",
    "出身地":"ほぼ静岡",
    "最終学歴":"小学校"
}
print(star["出身地"])

star["出身地"] = "神奈川県"
print(star["出身地"])

star["年齢"] = "12歳"
print(star["年齢"])
print(star)

del star["最終学歴"]
print(star)

# ＫeyError: '学歴' になるので注意
# del star["学歴"]
# print(star)
