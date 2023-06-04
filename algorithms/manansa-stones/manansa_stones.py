def stones(n, a, b):
  comb = list(combinations_with_replacement([a, b], n - 1))  
  if (a == b) :
    return [sum(comb[0])]
  
  possibleValues = [sum(i) for i in comb]
  possibleValues.sort()
  
  return possibleValues
