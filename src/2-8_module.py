import random
from statistics import median

print(random.random())
print(random.randint(0,6))
a_list = [0,1,2,3,4,5]
random.shuffle(a_list)
print(a_list)
print(random.choice(a_list))

mkt = [158,154,163,153,126]
vt = [143,142,186,154]
print(median(mkt))
print(median(vt))