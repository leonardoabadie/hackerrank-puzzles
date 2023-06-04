def breakingRecords(score):
  last_min_score = last_max_score = score[0]
  min_score = int()
  max_score = int()

  for point in score:
    if point > last_max_score:
      last_max_score = point
      max_score += 1

    if point < last_min_score:
      last_min_score = point
      min_score += 1

  return [max_score, min_score]
