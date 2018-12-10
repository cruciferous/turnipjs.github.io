# painter.py
# I condemn any use of this code anywhere without my express permission
# This program was intended to run in python 3, functionality in python 2 is unknown.

import time
start = time.time()

d = pow(2,19)
c = 0
for a in range(0,d):
  b = bin(a)[2:]
  b = (19-len(b))*'0' + b
  if ('000' in b or '11' in b):
    c = c+1
print(d-c)

print("--- %s seconds ---" % (time.time() - start))
