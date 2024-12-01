from pathlib import Path

p = Path(__file__).with_name('advent-1-data.txt')

l1, l2 = [], []

with p.open("r") as f:
        input_array = f.read().splitlines() 

for i in input_array:
    d = i.split('   ')
    l1.append(int(d[0]))
    l2.append(int(d[1]))

l1 = sorted(l1)
l2 = sorted(l2)
sum = 0

for i in range(len(l1)):
    sum += abs(l1[i] - l2[i])

print(sum)
