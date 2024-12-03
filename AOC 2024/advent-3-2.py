from pathlib import Path
import re

p = Path(__file__).with_name('advent-3-data.txt')

with p.open("r") as f:
    input = f.read()

expr = r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))"

matches = re.findall(expr, input)

flag = True
res = 0

for a, b, do, dont in matches:
    if do or dont:
        flag = bool(do)
    else:
        if flag:
            res = res + (int(a)* int(b))

print(res)