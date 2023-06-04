def flatlandSpaceStation(n, c):
  if (n == len(c)):
    return 0
  
  cities = [x for x in range(n)]
  prevNearestSpaceStation = 0
  nearestSpaceStation = min(c)
  citiesWithoutSpaceStation = []
  tmp = []
  
  for i in range(n):
    if cities[i] not in c:
      citiesWithoutSpaceStation.append(cities[i])
      continue    

    prevNearestSpaceStation = nearestSpaceStation
    nearestSpaceStation = cities[i]
    
    for city in citiesWithoutSpaceStation:
      if (abs(city - prevNearestSpaceStation) <= nearestSpaceStation - city):
        tmp.append(abs(city - prevNearestSpaceStation))
      else:
        tmp.append(nearestSpaceStation - city) 
 
    citiesWithoutSpaceStation = []
  
  for city in citiesWithoutSpaceStation:
    tmp.append(city - nearestSpaceStation)
  
  return max(tmp)
