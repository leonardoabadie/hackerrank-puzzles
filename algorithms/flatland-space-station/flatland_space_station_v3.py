def flatlandSpaceStation(n, c):
  if (n == len(c)):
    return 0
  
  c.sort()
  maxD = min(c)  
  tmp = 0
  
  for spaceStation in c:
    middleCity = (spaceStation + tmp) // 2
    distance = min(middleCity - tmp, spaceStation - middleCity)
    if (distance > maxD): 
      maxD = distance
          
    tmp = spaceStation
      
  if ((n - 1) - spaceStation > maxD):
    maxD = (n - 1) - spaceStation
      
  return maxD
