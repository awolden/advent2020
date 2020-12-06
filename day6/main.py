# https://adventofcode.com/2020/day/6
import os

def process():
  data = read_file('input')
  part_one(data)
  part_two(data)

def part_one(groups):
  total = 0
  flat_groups = [''.join(group) for group in groups]
  for group in flat_groups:
    total += len(set(group)) 
  print(f'total: {total}')

def part_two(groups):
  total = 0
  for group in groups:
    group_total = len(group[0])
    for char in group[0]:
      for individual in group:
        if char not in individual:
          group_total -= 1
          break;
    total += group_total
  print(f'total: {total}')

def read_file(file):
  lines = []
  f = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), file), 'r')
  groups = f.read().split('\n\n')
  return [ group.split('\n') for group in groups]
if __name__ == "__main__":
  process()
