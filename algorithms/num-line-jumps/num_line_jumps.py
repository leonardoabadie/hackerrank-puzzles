def canCatchUp(x1, x2):
  return True if(x1 == x2) else False

def aheadPosition(position, jump):
  return position + jump

def v1IsTheHighestJump(v1, v2):
  return True if (v1 > v2) else False

def areSamePosition(x1, v1, x2, v2):
  if (v1IsTheHighestJump(v1, v2)):
    while (x1 < x2):
      x1 = aheadPosition(x1, v1)
      x2 = aheadPosition(x2, v2)

      if (canCatchUp(x1, x2)):
        return "YES"

  return "NO"

def kangaroo(x1, v1, x2, v2):
  return areSamePosition(x1, v1, x2, v2)
