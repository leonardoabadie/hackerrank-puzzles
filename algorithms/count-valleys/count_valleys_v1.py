def count_valleys(steps:int, path:str) -> int:
  sea_level, crossed_valleys, walk, i = 0

  while i < steps:
    if (path[i] == "U"):
      walk += 1
    else:
      walk -= 1

    if (walk == sea_level) and (path[i-1] < sea_level):
      crossed_valleys += 1

    i += 1

  return crossed_valleys