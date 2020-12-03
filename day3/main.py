# https://adventofcode.com/2020/day/3
import os
import operator
import functools

slopes = [
  { 'x': 1, 'y': 1},
  { 'x': 3, 'y': 1},
  { 'x': 5, 'y': 1},
  { 'x': 7, 'y': 1},
  { 'x': 1, 'y': 2}
]

def process():
  topography = read_file('input')
  trees_hit = functools.reduce(operator.mul, [
    get_tree_collisions(slope, topography) for slope in slopes
  ])
  print(f'Trees Hit: {trees_hit}')

def get_tree_collisions(slope, topography):
  trees_hit = 0
  y = 0
  x = 0
  row_length = len(topography[y])

  while (y < len(topography)):
    if topography[y][x] == '#':
      trees_hit += 1
    y += slope['y']
    x = (x + slope['x']) % (row_length - 1)

  return trees_hit

def read_file(file):
  lines = []
  f = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), file), 'r')
  for line in f.readlines():
    lines.append(line)
  return lines
if __name__ == "__main__":
  process()
