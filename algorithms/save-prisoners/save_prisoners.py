def saveThePrisoner(prisoners, sweets, start):
  rest = start - 1
  
  if prisoners >= sweets:
    chair = sweets + rest
    if chair > prisoners:
      chair -= prisoners
  else:
    chair = sweets - (prisoners - rest)
    if chair > prisoners:
      chair = chair % prisoners
      if chair == 0:
        chair = prisoners

  return chair
