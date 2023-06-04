
# Be happy coding ~ My original solution :~
def beautifulDays(i:int, j:int, k:int) -> int:
    return len(list(filter(lambda n: abs(int(n) - int(n[::-1])) % k == 0, [str(n) for n in range(i, j + 1)])))
    
# My alternative solution 1 ~ by navjotahuja92
def beautifulDays(i:int, j:int, k:int) -> int:
    return len(list(filter(lambda n: n - int(str(n)[::-1]) % k == 0, [n for n in range(i, j + 1)])))

# My alternative solution 2 ~ by coslic sugestion

def filterBeautifulDays(days:list, k:int) -> int:
    beautiful_days = list()
    for day in days:
        if day - int(str(day)[::-1]) % k == 0:
            beautiful_days.append(day)
   
    return len(beatiful_days)

def listDays(i:int, j:int) -> list:
    return [n for n in range(i, j + 1)]

def beautifulDays(i:int, j:int, k:int) -> int:
    days = listDays(i, j)
    beatiful_days = filterBeautifulDays(days, k)

    return beautiful_days

# My alternative solution 3 ~ by 

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

""" Coslic Sugestion about navjotahuja92 solution
Nice, but I don't like the entaglement in beautifulDays of the looping through range with the algorithm itself that decides to put an 1 or not depending on the (day - reverse of the day) is divisible or not by k. I would disentangle the looping and the filtering by the problem condition in 2 separate functions, and the algorithm will become more readable.
"""

# navjotahuja92 solution
def beautifulDays(i:int, j:int, k:int) -> int:
    beautifulDays = [1 for day in range(i, j+1) if (day - int(str(day)[::-1])) % k == 0]
    return (sum(beautifulDays))