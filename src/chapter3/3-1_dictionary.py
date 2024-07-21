star = {"ニックネーム": "ほっしー", "出身地": "ほぼ静岡", "最終学歴": "小学校"}
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


def convert_arabia_number(num):
    roman_nums = {
        1: "Ⅰ",
        2: "Ⅱ",
        3: "Ⅲ",
        4: "Ⅳ",
        5: "Ⅴ",
        6: "Ⅵ",
        7: "Ⅶ",
        8: "Ⅷ",
        9: "Ⅸ",
        10: "Ⅹ",
    }

    if num in roman_nums:
        return roman_nums[num]
    else:
        return "[変換できません]"


print(convert_arabia_number(1))
print(convert_arabia_number(8))
print(convert_arabia_number(99))
