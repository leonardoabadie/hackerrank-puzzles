def isSumTheSameDay(s, d):
  return s == d

def birthday(choco_bar, day, month):
  ways_to_share = int()

  for i, _ in enumerate(choco_bar):
    if (isSumTheSameDay(choco_bar[i:i+month],day)) and(
      len(choco_bar[i:i+month])==month):
      ways_to_share += 1
    
  return ways_to_share
