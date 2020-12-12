# https://adventofcode.com/2020/day/12
import math
import os

DIRECTIONS = ['W','N','E','S']

def process():
  instructions = read_file('input')
  part_one_result = part_one(instructions)
  print(part_one_result)
  print(f'part one: {abs(part_one_result[0]) + abs(part_one_result[1])}')


  part_two_result = part_two(instructions)
  print(part_two_result)
  print(f'part two: {abs(part_two_result[0]) + abs(part_two_result[1])}')


def part_one(instructions):
  
  starting = [0,0]
  current_direction = 'E'

  for d,i in instructions:
    direction = d if not d == 'F' else current_direction
    amount = i

    if direction == 'L' or direction == 'R':
      turns = int(amount / 90)
      direction = DIRECTIONS[DIRECTIONS.index(current_direction) - turns] if direction == 'L' else DIRECTIONS[int((DIRECTIONS.index(current_direction) + turns) % len(DIRECTIONS))]
      current_direction = direction
      continue

    if direction == 'E':
      starting[0] += amount
    if direction == 'W':
      starting[0] -= amount
    if direction == 'N':
      starting[1] += amount
    if direction == 'S':
      starting[1] -= amount

  return starting

def part_two(instructions):
  
  starting = [10,1]
  ship = [0,0]

  for d,i in instructions:
    amount = i

    if d == 'L' or d == 'R':
      starting = rotate(starting, amount if d == 'L' else (360-amount))
      continue

    if d == 'F':
      ship[0] += starting[0] * amount
      ship[1] += starting[1] * amount
    if d == 'E':
      starting[0] += amount
    if d == 'W':
      starting[0] -= amount
    if d == 'N':
      starting[1] += amount
    if d == 'S':
      starting[1] -= amount

  return ship


def rotate(point, deg):
    px, py = point
    angle = math.radians(deg)
    x = 0 + math.cos(angle) * (px - 0) - math.sin(angle) * (py - 0)
    y = 0 + math.sin(angle) * (px - 0) + math.cos(angle) * (py - 0)
    return [round(x), round(y)]

def read_file(file):
  f = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), file), 'r')
  return [[line[0], int(line[1::])] for line in f.readlines()]

if __name__ == "__main__":
  process()
