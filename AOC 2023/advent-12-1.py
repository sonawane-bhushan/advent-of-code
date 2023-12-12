from pathlib import Path

p = Path(__file__).with_name('advent-12-data.txt')

with p.open("r") as f:
    input_array = f.read().splitlines()

