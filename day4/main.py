# https://adventofcode.com/2020/day/4
import os
import re

class Validator():
  required_props = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid' ]
  def has_required_props(self, entry): 
    for prop in self.required_props:
      if prop not in entry.keys():
        return False
    return True
  def all_props_valid(self, entry): 
    if not self.has_required_props(entry):
      return False

    for prop in self.required_props:
      foo = getattr(self, prop)
      validation = foo(entry[prop])
      if prop not in entry.keys() or not validation:
        # print(f'{entry[prop]} failed for {prop}')
        return False
    return True
  def byr(self, val):
    return re.match('\d{4}', val) and (1920 <= int(val) <= 2002)
  def iyr(self, val):
    return re.match('\d{4}', val) and (2010 <= int(val) <= 2020)
  def eyr(self, val):
    return re.match('\d{4}', val) and (2020 <= int(val) <= 2030)
  def hgt(self, val):
    search = re.search('(?P<num>\d*)(?P<type>cm|in)', val)
    if not search:
      return False
    if search.group('type') == 'in':
      return 59 <= int(search.group('num')) <= 76
    elif search.group('type') == 'cm':
      return 150 <= int(search.group('num')) <= 193
    else:
      return False
  def hcl(self, val):
    return re.match('^#[a-f0-9]{6}$', val)
  def ecl(self, val):
    return val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
  def pid(self, val):
    return re.match('^\d{9}$', val)

def process():
  clean_entries = read_file('input')
  print(f'part two valid {part_two_validate(clean_entries)}')


def part_one_validate(entries):
  validator = Validator()
  valid = len(entries)
  for entry in entries:
    if not validator.has_required_props(entry):
      valid -= 1
  return valid

def part_two_validate(entries):
  validator = Validator()
  valid = len(entries)
  for entry in entries:
    if not validator.all_props_valid(entry):
      valid -= 1
    else:
      print(entry)
  return valid

def entries_to_dict(entry):
  new_dict = {}
  keyvals = entry.split()
  for keyval in keyvals:
    key, val = keyval.split(':')
    new_dict[key] = val
  return new_dict

def read_file(file):
  lines = []
  f = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), file), 'r')
  return [
    entries_to_dict(entry) for entry in f.read().split('\n\n')
  ]

if __name__ == "__main__":
  process()