def stringComparison(original_string:str, desired_string:str, steps:int) -> str:
  first_string, second_string = original_string, desired_string

  if len(first_string) < len(second_string):
    first_string, second_string = second_string, first_string

  final_index = len(second_string) - 1
  i = 0

  while True:
    if (i == final_index) and (first_string[i] == second_string[i]):
      i += 1
      break

    if (first_string[i] != second_string[i]):
      break

    i += 1
        
    char_to_delete, char_to_add = len(first_string) - i, len(second_string) - i
    steps -= char_to_delete

    if (steps > char_to_add):
      while (steps > char_to_add):
        steps -= 1
    
    remain_operations = steps - char_to_add

    return "Yes" if (remain_operations == 0) else "No"

def appendAndDelete(s:str, t:str, k:int):
  canBeConverted = "Yes"

  if not (s == t):
    canBeConverted = stringComparison(s,t,k)
        
  return canBeConverted  
