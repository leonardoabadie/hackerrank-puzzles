def takeHourglass(a, i, j, t):
    hourglass = int()

    if j != 6:
        hourglass = sum(a[i][t:j]) + a[i+1][t+1] + sum(a[i+2][t:j])
    else:
        hourglass = sum(a[i][t:]) + a[i+1][t+1] + sum(a[i+2][t:])

    return hourglass

def hourglassSum(arr:int) -> int:
    """
    a   b   c
        d
    e   f   g
    """

    hourglass_total = list()
    i = 0

    while i <= 3:
        tpm = 0
        j = 3

        while j <= 6:
            hourglass_total.append(takeHourglass(arr, i, j, tpm))
            tpm += 1
            j += 1

        i += 1

    return max(hourglass_total)
