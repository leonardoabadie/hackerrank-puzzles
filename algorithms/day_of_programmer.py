# Autor: Matias
# Data: 12/07/22
#

# My solution ;)
def bissextoCalendarioGreg(y:int) -> int:
    dd = int()

    if (y % 4 == 0) and (y % 100 != 0):
        dd = 12
    elif (y % 400 == 0):
        dd = 12
    else:
        dd = 13

    return dd

def bissextoCalendarioJuliano(y:int) -> int:
    return 12 if (y % 4 == 0) else 13


def dayOfProgrammer(year):
    dd = int()
    
    if not(year == 1918):
        if (year > 1918):
            dd = bissextoCalendarioGreg(year)
        else:
            dd = bissextoCalendarioJuliano(year)
    else:
        dd = 26
                
    return f"{dd}.09.{year}"