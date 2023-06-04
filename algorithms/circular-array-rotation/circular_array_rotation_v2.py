def consult(index_to_return, queries, i, n):
  pos = 0
  while not pos == -1:
    try:
      pos = queries.index(i, pos)
      index_to_return[pos] = n
      pos += 1
    except ValueError:
      pos = -1
  
  return index_to_return

def circularArrayRotation(arr_to_rotate, rotation, queries) -> list:
  index_to_return = queries[:]
  queries_count = 0
  for index, num in enumerate(arr_to_rotate):
    final_index = index + rotation
    
    if final_index >= len(arr_to_rotate):
      final_index %= len(arr_to_rotate)

    if final_index in queries:
      index_to_return = consult(index_to_return, queries, final_index, num)
      queries_count += queries.count(final_index)

    if queries_count == len(index_to_return):
      break

  return index_to_return

