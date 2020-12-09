# https://adventofcode.com/2020/day/1
import math
import os

PREAMBLE_LEN = 25

def process():
  data = read_file('input')

  invalid = part_one(data)
  part_two(data, invalid)

def part_two(data, invalid):
  for i, i_num in enumerate(data):
    bucket = []
    for j, j_num in enumerate(data[i::]):
      bucket.append(j_num)
      sum_bucket = sum(bucket)
      if sum_bucket < invalid:
        continue
      elif sum_bucket == invalid:
        bucket.sort()
        print(f'{bucket[0]+bucket[len(bucket) - 1]}')
        return bucket.sort()
      else:
        break

def part_one(data):
  position = PREAMBLE_LEN
  for i in range(position, len(data)):
    num = data[i]
    preamble = list(set(data[i-PREAMBLE_LEN:i:]))
    if not is_list_sum(num, preamble):
      print(f'invalid: {num}')
      return num

def is_list_sum(num_to_compare, l):
  # brute force maybe use a more clever look up like quicksort
  for i, i_num in enumerate(l):
    for j, j_num in enumerate(l):
      if (j_num + i_num) == num_to_compare:
        return True
  return False

def read_file(file):
  f = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), file), 'r')
  return [int(x) for x in f.readlines()]

if __name__ == "__main__":
  process()
