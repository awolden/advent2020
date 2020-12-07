# https://adventofcode.com/2020/day/7
import os
import re
from collections import defaultdict

def process():
  data = read_file('input')
  contained = defaultdict(set)
  contains = defaultdict(list)
  for datum in data:
    search = re.findall('((?P<count>\d+)*\s*(?P<color>\w+ \w+)) bags*', datum)
    for color in search[1::]:
      if color[2] != 'no other':
        contained[color[2]].add(search[0][2])
        contains[search[0][2]].append({ 'color': color[2], 'count': int(color[1])})

  print(f'part_one total: {len(part_one(color = "shiny gold", dictset=contained))}')
  print(f'part_two total: {part_two(color = "shiny gold", dictlist=contains)}')

def part_two(color, memo={'count': 0}, dictlist = None, multiplier = 1):
  if dictlist[color]:
    for subcolor in dictlist[color]:
      memo['count'] += multiplier * subcolor['count']
      part_two(color=subcolor['color'], memo=memo, dictlist=dictlist, multiplier=multiplier * subcolor["count"])
  return memo


def part_one(color, memo = set(), dictset = None):
  if dictset[color]:
    for container_color in list(dictset[color]):
      memo.add(container_color)
      part_one(color=container_color, memo=memo, dictset=dictset)
  return memo


def read_file(file):
  f = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), file), 'r')
  return f.readlines()

if __name__ == "__main__":
  process()
