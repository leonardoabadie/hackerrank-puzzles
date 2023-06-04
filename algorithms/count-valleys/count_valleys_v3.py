def count_valleys(num_steps:int, steps:str) -> int:
  sea_level = crossed_valleys = walk = prev_walk =  0

  for step in steps:
    prev_walk = walk

    if (step == "U"):
      walk += 1
    else:
      walk -= 1

    if (walk == sea_level) and (prev_walk < sea_level):
      crossed_valleys += 1

  return crossed_valleys