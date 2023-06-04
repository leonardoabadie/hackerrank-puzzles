def pickingNumbers(arr):
  all_num_arr = set()
  for num in arr:
    all_num_arr.add(num)

  longest_subarr_len = int() # 0

  for num in all_num_arr:
    length = arr.count(num)

    if (num + 1 in all_num_arr) or (num - 1 in all_num_arr):
       x = arr.count(num + 1) if (num + 1) in all_num_arr else arr.count(num - 1)
       length += x
           
    if length > longest_subarr_len:
      longest_subarr_len = length

  return longest_subarr_len
