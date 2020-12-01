# https://adventofcode.com/2020/day/1
import math
import os

def process():
  data = readFile('input')
  for i, value in enumerate(data):
    for j, addValue in enumerate(data[i+1:]):
      for addValue2 in data[j+1:]:
        if value + addValue+ addValue2 == 2020:
          print(f'{value} * {addValue} * {addValue2} = {value * addValue * addValue2}')
          return

def readFile(file):
  lines = []
  f = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), file), 'r')
  for line in f.readlines():
    lines.append(line)
  return [int(x) for x in lines]

if __name__ == "__main__":
  process()
