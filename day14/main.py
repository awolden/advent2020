# https://adventofcode.com/2020/day/14
import math
import re
import os

def process():
  data = read_file('input')

  part_one(data)
  part_two(data)

def part_one(data):
  memory_addresses = {}

  for i,maskops in enumerate(data):
    mask = maskops['mask']
    for op in maskops['ops']:
      memory_addresses[op['address']] = apply_mask('{:036b}'.format(op['bin']), mask)
 
  sum = 0
  for key in memory_addresses:
    sum += int(memory_addresses[key], 2)
  print(f'part_one: {sum}')


def part_two(data):
  print()


def apply_mask(string, mask):
  new_str = ['0'] * len(string) 
  for i, char in enumerate(string):
    if mask[i] == 'X':
      new_str[i] = char
    else:
      new_str[i] = mask[i]
  return ''.join(new_str)

def read_file(file):
  lines = []
  f = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), file), 'r')

  agg = None
  for line in f.readlines():
    parts = line.split(' = ')
    if parts[0] == 'mask':
      if agg:
        lines.append(agg)
      agg = {
        'mask': parts[1].replace('\n', ''),
        'ops': []
      }
    else:
      mem_address = re.search("mem\[(\d+)\]", parts[0]).group(1)
      agg['ops'].append({
        'address': mem_address,
        'bin': int(parts[1])
      })
  lines.append(agg)
  return lines

if __name__ == "__main__":
  process()
