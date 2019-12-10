from sys import argv
from copy import copy

ADD = 1
MULTIPLY = 2
HALT = 99

def intcode_interpreter(memory):
  for i in range(0, len(memory), 4):
    # print(memory[i:i+4])
    op = memory[i]
    a = memory[i+1]
    b = memory[i+2]
    dst = memory[i+3]
    if op == ADD:
      memory[dst] = memory[a] + memory[b]
    elif op == MULTIPLY:
      memory[dst] = memory[a] * memory[b]
    elif op == HALT:
      return memory
    else:
      print(f"Invalid op {op}")
      return None

def main(file):
  res = None
  memory = None
  with open(file, "rt") as f:
    memory = f.read()
    memory = list(map(int, memory.split(",")))
  for noun in range(99):
    for verb in range(99):
      tmp_memory = copy(memory)
      tmp_memory[1] = noun
      tmp_memory[2] = verb
      res = intcode_interpreter(tmp_memory)[0]
      if res == 19690720:
        return (noun * 100) + verb
  return None

if __name__ == "__main__":
  if len(argv) < 2:
    print("You must specify a file to read!")
  else:
    print(f"Value at position 0: {main(argv[1])}")