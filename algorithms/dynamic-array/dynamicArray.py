def dynamicArray(n, queries):
  lastAnswer = 0
  arr = [[] for x in range(0, n)]
  result = []

  for q in queries:
    queryType = q[0]
    x = q[1]
    y = q[2]
    idx = ((x ^ lastAnswer) % n)
        
    if (int(queryType) == 1):
      arr[idx].append(y)
    else:
      lastAnswer = arr[idx][y % len(arr[idx])]
      result.append(lastAnswer)
            
  return result