def catAndMouse(x, y, z):
  result = ""
    
  if abs(z - x) == abs(z - y):
    result = "Mouse C"
  elif abs(z - x) < abs(z - y):
    result = "Cat A"
  else:
    result = "Cat B"

  return result
