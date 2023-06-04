def countApplesAndOranges(s, t, a, b, apples, oranges):
  land_apple = int()
  land_orange = int()

  for apple in apples:
    if (s <= a + apple <= t):
      land_apple += 1

  for orange in oranges:
    if (s <= b + orange <= t):
      land_orange += 1
    
  print(f"{land_apple}\n{land_orange}")

