from random import randint


def destiny_human2(num):
    stars = ["勇太", "仁美", "迅", "耀"]
    idx = num % len(stars)
    print("あなたの運命の相手は")
    print(stars[idx])


num_str = input("あなたの好きな数字は？：")
num = int(num_str)
destiny_human2(num)

num_rand = randint(0, 10)
print("ランダム")
destiny_human2(num_rand)


def destiny_human3(num):
    stars = ["勇太", "仁美", "迅", "耀"]
    idx = num % len(stars)
    return stars[idx]


print("ランダム + return")
num_rand = randint(0, 10)
star = destiny_human3(num_rand)
print("今日あなたと出会う可能性のある人は", star, "です。")
print("出会う確率は", num_rand * 10, "％です。")
