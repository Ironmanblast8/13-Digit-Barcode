# to calculate barcode's 13th digit error.
import random

# make random 12 digits
def bar_check():
  bar = []
  for _ in range(12):
    bar.append(random.randint(0,9))
  print(bar) 
  line1tot = 0 
  line2tot = 0
  for ele in range(0,12,2):
    line1tot += bar[ele]
    line2tot += bar[ele+1]
  line1 = line1tot % 10
  line2 = line2tot % 10
  check = 10 - (((3 * line2) % 10 + line1) % 10)
  print (check) 


def barvalid():

bar_check()
