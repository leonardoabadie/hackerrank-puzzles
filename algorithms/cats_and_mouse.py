"""
To be or not to be I am that. A Random Man.
| Matias | (07/18/22) | 7:52PM | from HackerRank | Challenge: Cats and a mouse |
"""

def catAndMouse(x, y, z):
    result = ""
    
    if abs(z - x) == abs(z - y):
        result = "Mouse C"
    elif abs(z - x) < abs(z - y):
        result = "Cat A"
    else:
        result = "Cat B"

    return result
