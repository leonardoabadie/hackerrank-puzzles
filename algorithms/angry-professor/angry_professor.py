def angryProfessor(k:int, a:list) -> str:
  return "YES" if k > len([n for n in a if n <= 0]) else "NO"