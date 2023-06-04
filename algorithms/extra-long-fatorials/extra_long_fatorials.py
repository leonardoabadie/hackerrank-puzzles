def fat(n:int) -> int:
  if (n > 1):
    n = n * (fat(n - 1))
  else:
    n = 1
  
  return n 

def extraLongFactorials(n:int) -> int:
  print(fat(n))