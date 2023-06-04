function canCatchUp(x1, x2) {
  if (x1 == x2) {
    return true;
  }
  
  return false;
}

function aheadPosition(position, jump) {
  return position + jump;
}


function v1IsTheHighestJump(v1, v2) {
  if (v1 > v2) {
    return true;
  }
  
  return false;
}

function areSamePosition(x1, v1, x2, v2) {
  if (v1IsTheHighestJump(v1, v2)) {
    while (x1 < x2) {
      x1 = aheadPosition(x1, v1);
      x2 = aheadPosition(x2, v2);

      if (canCatchUp(x1, x2)) {
          return "YES";
      }
    }
  }

  return "NO";
}

function kangaroo(x1, v1, x2, v2) { 
  let same_position = areSamePosition(x1, v1, x2, v2);    
  return same_position;
}

