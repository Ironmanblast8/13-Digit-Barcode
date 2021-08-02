# to calculate barcode's 13th digit error.
import random


def bar_check(bar):
    line1 = sum(bar[::2])
    line2 = sum(bar[1::2])
    check_digit = 10 - (((3 * line2) + line1) % 10)
    return check_digit
  
def bar_valid(bar_code):
  check = bar_check(bar_code)
  return check == bar_code[-1]

if __name__ == "__main__":
  bar = [9,3,1,1,5,9,9,4,1,6,4,6] # headgear check 4
  # make random 13 digits
  bar2 = []
  for _ in range(12):
   bar2.append(random.randint(0,9))
  print(bar, bar2) 
  print (bar_check(bar)) 
  print (bar_valid(bar2))