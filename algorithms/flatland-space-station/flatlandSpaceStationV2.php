<?php
function flatlandSpaceStation($n, $c) {
  if ($n == count($c)) {
      return 0;
  }

  sort($c);
  $maxD = min($c);
  $tmp = 0;

  foreach ($c as $spaceStation) {
    $middleCity = intdiv(($spaceStation + $tmp), 2);
    $distance = min($middleCity - $tmp, $spaceStation - $middleCity);
    
    if ($distance > $maxD) {
      $maxD = $spaceStation;
    }
    
    $tmp = $spaceStation;
  };

  if (($n - 1) - $spaceStation > $maxD) {
    $maxD = ($n - 1) - $spaceStation;
  }

  return $maxD;
}
?>
