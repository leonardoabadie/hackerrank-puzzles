def shift_values_array(arr):
  for i in range(1, len(arr)):
    arr[i - 1] = arr[i]
  
  arr[len(arr)-1] = 0
  
  return arr
