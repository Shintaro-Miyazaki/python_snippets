#Code snipplet I got from https://www.codementor.io/jcsahnwaldt
def scale(arr):
  s = 2.0/(len(arr)-1)
  for i in range(len(arr)):
    if arr[i] != 0:
      yield -1.0+s*i

tests = [
  [1,1],
  [1,1,1],
  [1,0,1,0],
  [0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1]
]

for arr in tests:
  print arr
  for i in scale(arr):
    print i
