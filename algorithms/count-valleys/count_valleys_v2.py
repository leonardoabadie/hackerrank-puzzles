def count_valleys(steps:int, path:str) -> int:
  sea_level, crossed_valleys, count, prev_count = 0

  for step in path:
    if (step == "U"):
      prev_count = count
      count += 1
    else:
      prev_count = count
      count -= 1

    if (count == sea_level) and not(prev_count > sea_level):
      crossed_valleys += 1

  return crossed_valleys