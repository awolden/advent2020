# https://adventofcode.com/2020/day/11
import math
import os

def process():
  floorplan = read_file('input')

  part_one(floorplan)
  part_two(floorplan)

def part_one(floorplan):
  new_state = floorplan
  existing_state = gen_state(floorplan)
  generations = 0


  while not existing_state == new_state:
    generations += 1
    existing_state = new_state
    new_state = gen_state(floorplan)
    for y, row in enumerate(existing_state):
      for x, col in enumerate(row):
        new_state[y][x] = get_seat_state(existing_state, x, y, False)
    # print_state(new_state)
  print(f'{count_seated(new_state)}')

def part_two(floorplan):
  new_state = floorplan
  existing_state = gen_state(floorplan)
  generations = 0

  while not existing_state == new_state:
    generations += 1
    existing_state = new_state
    new_state = gen_state(floorplan)
    for y, row in enumerate(existing_state):
      for x, col in enumerate(row):
        new_state[y][x] = get_seat_state(existing_state, x, y, True)
    # print_state(new_state)
  print(f'{count_seated(new_state)}')

def print_state(state):
  print('---')
  for row in state:
    print(f'{"".join(row)}')

def count_seated(state):
  flat = [item for sublist in state for item in sublist]
  return sum(c == '#' for c in flat)

def gen_state(state):
  return [['.'] * len(state[0]) for i in range(0, len(state))]

def get_seat_state(state, x, y, sight_line):
  if state[y][x] == '.':
    return '.'
  if state[y][x] == 'L' and not sight_line and get_neighbors(state, x, y) == 0:
    return '#'
  if state[y][x] == 'L' and sight_line and get_sightline_neighbors(state, x, y) == 0:
    return '#'
  if state[y][x] == '#' and not sight_line:
    return '#' if get_neighbors(state, x, y) < 4 else 'L'
  if state[y][x] == '#' and sight_line:
    return '#' if get_sightline_neighbors(state, x, y) < 5 else 'L'
  return 'L'

def get_neighbors(state, x, y):
  seated_neighbors = 0
  for x_mod in range(-1,2):
    if x_mod + x >= len(state[0]) or x_mod + x < 0:
      continue
    for y_mod in range(-1,2):
      if y_mod + y >= len(state) or y_mod + y < 0:
        continue
      if x_mod + x == x and y_mod + y == y:
        continue
      if state[y+y_mod][x+x_mod] == '#':
        seated_neighbors += 1
  return seated_neighbors

def get_sightline_neighbors(state, x, y):
  seated_neighbors = 0
  for x_mod in range(-1,2):
    for y_mod in range(-1,2):
      y_adjusted = y
      x_adjusted = x
      if x_mod == 0 and y_mod == 0:
        continue
      while True:
        y_adjusted += y_mod
        x_adjusted += x_mod
        if y_adjusted >= len(state) or y_adjusted < 0:
          break
        if x_adjusted >= len(state[0]) or x_adjusted < 0:
          break
        if state[y_adjusted][x_adjusted] == '#':
          seated_neighbors += 1
          break
        if state[y_adjusted][x_adjusted] == 'L':
          break
  return seated_neighbors

def read_file(file):
  f = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), file), 'r')
  return [list(line.replace('\n', '')) for line in f.readlines()]

if __name__ == "__main__":
  process()
