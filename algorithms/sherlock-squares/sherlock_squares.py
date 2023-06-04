def squares(a:int, b:int):
  numbers = [n for n in range(a, b + 1)]

  for n in range(a, b + 1):
    base = 2
    while abs(base - (n * base)) > 0.00001:
      p = (base + (n / base)) / 2
      base = p

      print(p, end=" ")
