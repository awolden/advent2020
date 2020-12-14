# https://adventofcode.com/2020/day/1
import os
import math

def process():
  data = read_file('input')
  part_one(data)
  part_two(data)

def part_one(data):
  best_bus = None
  best_diff = math.inf

  for bus in data['buses']:
    if bus == 'x':
      continue
    base_multiplier = int(data['time'] / bus)
    diff = ((base_multiplier+1) * bus) - data['time']
    if diff < best_diff:
      best_bus = bus
      best_diff = diff

  print(f'Best Bus: {best_bus}: Time: {best_diff + data["time"]} Diff: {best_diff}')
  print(f'answer: {best_diff * best_bus}')

def part_two(data):
  base = 0
  multiplier = data['buses'][0]
  for i, bus in enumerate(data['buses'][1:], start=1):
    if bus == 'x':
      continue
    diff = i
    for j in range(base, multiplier*bus, multiplier):
        if not (j + diff) % bus:
            multiplier = multiplier*bus
            base = j    
  print(f'start time {base}')

def read_file(file):
  lines = []
  f = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), file), 'r')

  time, buses = f.readlines()
  return {
    'time': int(time.replace('\n', '')),
    'buses': [(int(bus) if not bus == 'x' else 'x') for bus in buses.replace('\n', '').split(',')]
  }

if __name__ == "__main__":
  process()
