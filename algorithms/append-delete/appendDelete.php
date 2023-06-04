<?php
function stringComparison($originalStr, $desiredStr, $steps) {
  $firstStr = $originalStr;
  $secondStr = $desiredStr;
  
  if strlen($firstStr) < strlen($secondStr) {
    $firstStr = $desiredStr;
    $secondStr = $originalStr;
  }

  $finalIndex = strlen($secondStr) -1;
  $i = 0;
    
  while (true) {
    if ($i == $finalIndex) && ($firstStr[$i] == $secondStr[$i]) {
      $i++;
      break;
    }
    if ($firstStr[$i] != $secondStr[$i]) {
      break;
    }

    $i++;
  }

  $charToDelete = strlen($firstStr) - $i;
  $charToAdd = strlen($secondStr) - $i;
  $steps -= $charToDelete;

  if ($steps > $charToAdd) {
    while ($steps > $charToAdd) {
      $steps--;
    } 
  }

  if (!($steps - $charToAdd == 0)) {
    return "No";
  }
    
  return "Yes";
}

function appendAndDelete($s, $t, $k) {
  if (strcmp($s, $t) == 0) {
    return "Yes";
  }

  return stringComparison($s, $t, $k);
}
?>
