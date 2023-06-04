<?php
function circularArrayRotation ($arrToRotate, $rotation, $indexToReturn) {
  $queries = [];
  $queriesNum = 0;

  for ($i = 0; $i < count($arrToRotate); $i++) {
    $finalIndex = $index + $rotation;

    if ($finalIndex >= count($arrToRotate)) {
      $finalIndex %= count($arrToRotate);
    }

    if (in_array($finalIndex, $indexToReturn)) {
      $queries[$finalIndex] = $n;
      $indexOccurrence = array_filter($indexToReturn, function($index) {
        return $index == $finalIndex
      });
      $queriesNum += count($indexOccurrence);
    }

    if ($queriesNum == count($indexToReturn)) {
      break;
    }
  }

  for ($i = 0; $i < count($indexToReturn); $i++) {
    $querie = $indexToReturn[$i];
    $indexToReturn[$i] = $queries[$querie];
  }
    
  return $indexToReturn;
}
?>
