# https://adventofcode.com/2020/day/8
import os

class Bootmachine:
  def __init__(self, machine_code):
    self.accumulator = 0
    self.position = 0
    self.machine_code = machine_code
    self.executed_commands = set()
    self.debug = False

  def run_debug(self):
    stopped = False
    self.debug = True
    while not stopped:
      if self.position in self.executed_commands:
        stopped = True
        print(f'Debug Statement: LOOP DETECTED Accumulator({self.accumulator})')
        return False
      if self.position == len(self.machine_code):
        print(f'Debug Statement: Completed Accumulator({self.accumulator})')
        return self.accumulator
      self.executed_commands.add(self.position)
      self.execute_next_command()

  def execute_next_command(self):
    cmd, value = self.machine_code[self.position]
    if self.debug:
      print(f'{cmd}: {value}: {self.accumulator}')
    if cmd == 'jmp':
      self.position += value
    elif cmd == 'acc':
      self.accumulator += value
      self.position += 1
    elif cmd == 'nop':
      self.position += 1





def process():
  data = read_file('input')

  # part one
  bootmachine = Bootmachine(data)
  bootmachine.run_debug()

  # part two 
  for i, cmd in enumerate(data):
    if cmd[0] == 'nop' or cmd[0] == 'jmp':
      data_copy = data.copy()
      data_copy[i] = ('jmp' if cmd[0] == 'nop' else 'nop', cmd[1])
      bootmachine = Bootmachine(data_copy)
      if bootmachine.run_debug():
        break




def read_file(file):
  lines = []
  f = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), file), 'r')
  for x in f.readlines():
    cmd, val = x.replace('\n', '').split(' ')
    lines.append((cmd, int(val)))
  return lines

if __name__ == "__main__":
  process()
