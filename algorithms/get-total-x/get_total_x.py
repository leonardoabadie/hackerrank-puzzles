def isFactor(a,b,x):
  div_result_a = []
  div_result_b = []

  for num_a in a:
    # True if an element a is a factor
    div_result_a.append(x%num_a==0)
  for num_b in b:
    # True if x is a factor
    div_result_b.append(num_b%x==0)

  return True if((False not in div_result_a) and (False not in div_result_b)) else False

def getTotalX(a,b):
  between_them = int()

  if (sum(a) <= sum(b)):
    # max(a) -- (min(b)+1) ~> range of numbers between two sets
    for x in range(max(a), (min(b)+1)):
      if isFactor(a,b,x):
        between_them +=1

  return between_them
