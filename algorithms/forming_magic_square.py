"""
To be or not to be I am that. A Random Man.
| Matias | (07/18/22) | 8:18PM | from HackerRank | Challenge: Forming a magic square |
"""
"""
square... The resulting magic square must contain distinct intergers in the inclusive range | 1, 9 |
-----------
|i | i | i|
|---------|
|i | i | i|
|---------|
|i | i | i|
-----------

        | [0][0] | [0][1] | [0][2] |
        | [1][0] | [1][1] | [1][2] |
        | [2][0] | [2][1] | [2][2] |
"""

def is_magic_square(square, total, missing):
    # números pares ocupam a borda, enquanto números ímpares formam uma cruz no centro.
    somatory = sum(total[0]) + sum(total[1]) + sum(total[2])
    even_n =  [square[0][0], square[0][2], square[2][2], square[2][0]]
    odd_n =  [square[0][1], square[1][2], square[2][1], square[1][0], square[1][1]]
    for num in missing:
        if num % 2 == 0:
            positions = even_n[:]
        else:
            positions = odd_n[:]

        for i,position in enumerate(positions):
            positions[i] = num


    return

def divide_square(square):
    ln = square[:]
    cl = [
        [square[0][0], square[1][0], square[2][0]],
        [square[0][1], square[1][1], square[2][1]],
        [square[0][2], square[1][2], square[2][2]]
        ]
    dg = [
        [square[0][0], square[1][1], square[2][2]],
        [square[0][2], square[1][1], square[2][0]]
        ]

    return ln, cl, dg

def forming_magic_square(square):
    minimum_possible_cost = int()
    ln, col, diag = divide_square(square)
    total = [sum(n) for n in ln], [sum(n) for n in col], [sum(diag[0]), sum(diag[1])]
    missing = list()
    for num in range(1,10,1):
        if (num not in square[0]) and (num not in square[1]) and (num not in square[2]):
            missing.append(num)
    repeat = list()
    for num in range(1,10,1):
        if (square[0].count(num) + square[1].count(num) + square[2].count(num)) > 1:
            repeat.append(num)
    minimum_possible_cost = is_magic_square(square, total, missing)

def main():
    # ([15, 15, 14], [15, 15, 14], [14, 15])
    forming_magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 5]])

    return

if __name__ == "__main__":
    main()
