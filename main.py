# to calculate barcode's 13th digit error.
import random

# make random 12 digits
bar = []
for _ in range(12):
  bar.append(random.randint(0,9))
print(bar)