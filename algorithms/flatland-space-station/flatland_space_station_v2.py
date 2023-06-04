def flatlandSpaceStation(n, c):
  if (n == len(c)):
    return 0
  
  noSpaceStation = []
  prevNearestSpaceStation = min(c)
  maxD = 0
  
  for i in range(n):
    if i not in c:
      noSpaceStation.append(i)
      continue
      
    for city in noSpaceStation:
      tmp = [abs(city - prevNearestSpaceStation), abs(city - i)]
      nearestDistance = min(tmp)
      if (nearestDistance > maxD):
        maxD = nearestDistance
      
    prevNearestSpaceStation = i
    noSpaceStation = []
      
  nearestDistance = max(noSpaceStation) - prevNearestSpaceStation
  if (nearestDistance > maxD):
    maxD = nearestDistance            

  return maxD
