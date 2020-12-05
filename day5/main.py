# https://adventofcode.com/2020/day/5
import math
import os

ROWS = 128
COLUMNS = 8

def process():
  data = read_file('input')
  part_one(data)
  part_two(data)

def part_two(data):
  seats = [get_seat_id(boarding_pass) for boarding_pass in data]
  seats.sort()
  for i, seat in enumerate(seats):
    if i+1 < len(seats) and seat+1 != seats[i+1]:
      print(f'missing seat {seat+1}')

def part_one(data):
  highest_seat = 0
  for boarding_pass in data:
    seat_id = get_seat_id(boarding_pass)
    if seat_id > highest_seat:
      highest_seat = seat_id
  print(highest_seat)

def get_seat_id(boarding_pass):
  row_tree = boarding_pass[0:7:]
  column_tree = boarding_pass[7::]
  row = traverse_tree(row_tree, ROWS, 'F', 'B')
  column = traverse_tree(column_tree, COLUMNS, 'L', 'R')
  return row * 8 + column


def traverse_tree(tree, depth, left_char, right_char):
  state = list(range(0, depth, 1))
  for node in tree:
    if node == left_char:
      state = state[0:len(state)//2]
    elif node == right_char:
      state = state[len(state)//2::]
  return state.pop()

def read_file(file):
  f = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), file), 'r')
  return [ line.replace('\n', '') for line in f.readlines() ]

if __name__ == "__main__":
  process()
