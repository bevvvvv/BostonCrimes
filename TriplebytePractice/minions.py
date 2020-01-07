# input
# number of minons (lines)
n = int(input())
# create minion class
class Minion:
    def __init__(self, min_val, max_val):
        self.min = min_val
        self.max = max_val
# parse minions
minions = []
for i in range(n):
    interval = input().split()
    interval = list(map(int, interval))
    minion = Minion(interval[0], interval[1])
    minions.append(minion)

# sort minions
minions.sort(key = lambda x: x.min)