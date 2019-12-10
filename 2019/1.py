from math import floor
from sys import argv

def compute_fuel(mass):
  return floor(mass / 3) - 2

def main(file):
  sum = 0
  with open(file, "rt") as f:
    for line in f:
      mass = int(line)
      sum += compute_fuel(mass)
  return sum

def main2(file):
  sum = 0
  with open(file, "rt") as f:
    for line in f:
      mass = compute_fuel(int(line))
      while mass > 0:
        sum += mass
        mass = compute_fuel(mass)
  return sum


if __name__ == "__main__":
  if len(argv) < 2:
    print("You must specify a file to read!")
  else:
    print(f"Sum 1 {main(argv[1])}")
    print(f"Sum 2 {main2(argv[1])}")