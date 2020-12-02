# https://adventofcode.com/2020/day/1
import math
import os

def process():
  data = read_file('input')
  for i, value in enumerate(data):
    for j, add_value in enumerate(data[i+1:]):
      for add_value2 in data[j+1:]:
        if value + add_value+ add_value2 == 2020:
          print(f'{value} * {add_value} * {add_value2} = {value * add_value * add_value2}')
          return

def read_file(file):
  lines = []
  f = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), file), 'r')
  for line in f.readlines():
    lines.append(line)
  return [int(x) for x in lines]

if __name__ == "__main__":
  process()
