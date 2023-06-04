def diagonalDifference(arr, a=int(), b=int()):
  i = 0
  j = len(arr)-1

  while i < len(arr):
    a += arr[i][i]
    b += arr[i][j]

    i += 1
    j -= 1

  return abs(a - b)