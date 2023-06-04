def isDivisible(num_i,num_j, target_num): 
  return 1 if ((num_i + num_j) % target_num == 0) else 0

def divisibleSumPairs(len_array, target_num, array):
  divisible_pairs = int()   

  for i in range(len_array-1):        
    for j in range(i+1, len_array):
      divisible_pairs += isDivisible(array[i], array[j], target_num)