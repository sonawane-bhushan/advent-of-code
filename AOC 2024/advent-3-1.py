from pathlib import Path
import re

p = Path(__file__).with_name('advent-3-data.txt')

with p.open("r") as f:
    input = f.read()

expr = r'mul\((\d+,\d+)(?=\))'

matches = re.findall(expr, input)
res = 0

for i in matches:
    i = i.split(',')
    res = res + (int(i[0]) * int(i[1]))

print(res)