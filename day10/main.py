# https://adventofcode.com/2020/day/10
import os
from collections import defaultdict

def process():
  data = read_file('input')
  data.sort()

  part_one(data.copy())
  part_two(data.copy())

def part_one(jolts):
  diffs = defaultdict(int)
  for i, jolt in enumerate(jolts):
    if i == 0:
      diffs[f'{jolt - 0}'] += 1
    else:
      diffs[f'{jolt - jolts[i-1]}'] += 1
  diffs['3'] += 1 # final adapter
  print(f'part_one: {diffs["1"] * diffs["3"]}')


def part_two(jolts):
  jolts.append(max(jolts)+3)
  jolts.sort()

  memo = defaultdict(int)
  result = generate_permutations(current_jolt=0, jolts=jolts, memo=memo)
  print(f'part_two: {result}')


def generate_permutations(jolts, current_jolt, memo):

  if not len(jolts):
    return 1

  if memo[current_jolt] :
    return memo[current_jolt]

  branches = 0
  for i in range(0,3):
    if (i >= len(jolts)):
      break
    if jolts[i] - current_jolt <= 3:
      branches += generate_permutations(jolts=jolts[i+1::], current_jolt=jolts[i], memo=memo)

  memo[current_jolt]+=branches
  return branches


def read_file(file):
  f = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), file), 'r')
  return [int(x) for x in f.readlines()]

if __name__ == "__main__":
  process()
