def fairRations(B):
  n = 0
  for i in range(len(B)):
    if (B[i] % 2 != 0) and (not (i == len(B) - 1)):
      B[i] += 1
      B[i + 1] += 1
      n += 2

  j = len(B) - 1
  
  for i in range(len(B)):
    if (B[i] % 2 != 0) or (B[j] % 2 != 0):
      return "NO"
    j -= 1
    
  return str(n)