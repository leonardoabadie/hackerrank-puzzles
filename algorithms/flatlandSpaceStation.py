# solution 1

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

# solution 2

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


# Solution 3 inspired by ''

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
