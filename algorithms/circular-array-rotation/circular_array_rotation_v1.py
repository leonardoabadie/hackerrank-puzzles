def circularArrayRotation(arr_to_rotate:list, rotation:int, index_to_return:list) -> list:
  queries = dict()
  n_queries = 0
  for index, n in enumerate(arr_to_rotate):
    final_index = index + rotation 
    if final_index >= len(arr_to_rotate):
      final_index %= len(arr_to_rotate)
    if final_index in index_to_return:
      queries[final_index] = n
      n_queries += index_to_return.count(final_index)
    if n_queries == len(index_to_return):
        break
    
  for i, querie in enumerate(index_to_return):
    index_to_return[i] = queries[querie]

  return index_to_return
