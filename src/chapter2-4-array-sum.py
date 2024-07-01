import matplotlib.pyplot as plt

monk_fish_team = [158, 157,163,157,145]
len_fish = len(monk_fish_team)
sum_fish = sum(monk_fish_team)
max_fish = max(monk_fish_team)
min_fish = min(monk_fish_team)

print(sum_fish)
print(max_fish)
print(min_fish)

mean_fish = sum_fish/len_fish
print(mean_fish)

plt.bar([0,1,2,3,4], monk_fish_team)
plt.plot([0,len_fish],[mean_fish, mean_fish], color = 'red')
plt.show()