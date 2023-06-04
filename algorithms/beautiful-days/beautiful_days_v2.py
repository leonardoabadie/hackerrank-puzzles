def filterBeautifulDays(days:list, k:int) -> int:
  beautiful_days = int() 
  for day in days:
    if (day - int(str(day)[::-1])) % k == 0:
      beautiful_days += 1
   
  return beautiful_days

def listDays(i:int, j:int) -> list:
  return range(i, j + 1)

def beautifulDays(i:int, j:int, k:int) -> int:
  days = listDays(i, j)
  beatiful_days = filterBeautifulDays(days, k)

  return beatiful_days

