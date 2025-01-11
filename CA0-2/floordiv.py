
# read two numbers from input
#do floor div and return result

import sys

div_nums = sys.stdin.read()

div_nums = div_nums.split()

if len(div_nums) != 2:
  print("Error: incorrect number of input")
else:
  try:
    print(int(div_nums[0]) // int(div_nums[1]))
  except ZeroDivisionError:
    print("division by zero!!")