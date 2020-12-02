# https://adventofcode.com/2020/day/2
import re
import os

def process():
  data = read_file('input')
  valid_passwords = 0
  for password_object in data:
    if test_password_part_two(password_object):
      valid_passwords += 1
  print(f'Valid Passwrds: {valid_passwords}')

def test_password(password_object):
  char_count = 0
  for char in password_object['password']:
    if char == password_object['char']:
      char_count += 1
    if char_count > password_object['max_count']:
      return False
  if char_count < password_object['min_count']:
    return False
  else:
    return True

def test_password_part_two(password_object):
  char_count = 0
  if password_object['password'][password_object['min_count'] - 1] == password_object['char']:
    char_count += 1
  if password_object['password'][password_object['max_count'] - 1] == password_object['char']:
    char_count += 1

  if char_count == 1:
    return True
  else:
    return False

def read_file(file):
  lines = []
  f = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), file), 'r')
  for line in f.readlines():
    match = re.search('(?P<min_count>\d+)-(?P<max_count>\d+) (?P<char>[a-z]): (?P<password>[a-z]+)', line)
    lines.append({
      'min_count': int(match.group('min_count')),
      'max_count': int(match.group('max_count')),
      'char': match.group('char'),
      'password': match.group('password')
    })
  return lines

if __name__ == "__main__":
  process()
