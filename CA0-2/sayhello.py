import sys

names = sys.stdin.read()

names = names.split()

for name in names:
  print("Hello " + name + "!")