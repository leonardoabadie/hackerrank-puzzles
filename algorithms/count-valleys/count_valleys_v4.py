def count_valleys(num_steps:int, steps:str) -> int:
  sea_level = crossed_valleys = walk = 0

  for step in steps:
    walk += 1 if (step == "U") else -1

    if (walk == sea_level) and (step == "U"):
      crossed_valleys += 1

  return crossed_valleys
