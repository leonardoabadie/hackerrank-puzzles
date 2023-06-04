def beautifulDays(i:int, j:int, k:int) -> int:
  return len(list(filter(lambda n: n - int(str(n)[::-1]) % k == 0, [n for n in range(i, j + 1)])))

