from sys import argv, maxsize
import re

UP = "U"
DOWN = "D"
RIGHT = "R"
LEFT = "L"

class Coordinate():
  def __init__(self):
    self.x = 0
    self.y = 0

def manhattan_distance(p1, p2):
  dist = 0
  if len(p1) != len(p2):
    return None
  for i in range(len(p1)):
    dist += abs(p1[i] - p2[i])
  return dist

def pos_set(path):
  path_set = set()
  coord = Coordinate()
  for move in path:
    d, i = list(filter(None, re.split("(\D+)", move)))
    i = int(i)
    if d == UP:
      for j in range(i):
        coord.y += 1
        path_set.add((coord.x, coord.y))
      # coord.y += i
    elif d == DOWN:
      for j in range(i):
        coord.y -= 1
        path_set.add((coord.x, coord.y))
      # coord.y -= i
    elif d == RIGHT:
      for j in range(i):
        coord.x -= 1
        path_set.add((coord.x, coord.y))
      # coord.x -= 1
    elif d == LEFT:
      for j in range(i):
        coord.x += 1
        path_set.add((coord.x, coord.y))
      # coord.x += 1
    else:
      print(f"Invalid direction {d}")
      return None
    # path_set.add((coord.x, coord.y))
  return path_set

def main(file):
  paths = []
  with open(file, "rt") as f:
    for path in f:
      path_set = pos_set(path.replace("\n", "").split(","))
      paths.append(path_set)
  intersection = paths[0].intersection(paths[1])
  min_dist = maxsize
  for p in intersection:
    min_dist = min(manhattan_distance(p, (0, 0)), min_dist)
  return min_dist
    

if __name__ == "__main__":
  if len(argv) < 2:
    print("You must specify the name of the file to use")
  else:
    print(f"Manhattan Distance of Closest Point {main(argv[1])}")