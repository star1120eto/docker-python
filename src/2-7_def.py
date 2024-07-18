def destiny_tanks2(num):
    stars = ['勇太','仁美','迅','耀']
    idx = num % len(stars)
    print("あなたの運命の相手は")
    print(stars[idx])
    
num_str = input('あなたの好きな数字は？：')
num = int(num_str)
destiny_tanks2(num)
