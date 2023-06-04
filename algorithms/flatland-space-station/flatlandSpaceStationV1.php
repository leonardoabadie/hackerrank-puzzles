<?php
function flatlandSpaceStation($n, $c) {
  if ($n == count($c)) {
      return 0;
  }

  $noSpaceStation = [];
  $prevNearestSpaceStation = min($c);
  $maxD = 0;

  for ($i = 0; $i < $n; $i++) {
    if (!(in_array($i, $c))) {
      array_push($noSpaceStation, $i);
      continue;
    }

    foreach ($noSpaceStation as $city) {
      $tmp = [abs($city - $prevNearestSpaceStation), abs($city - $i)];
      $nearestDistance = min($tmp);
      
      if ($nearestDistance > $maxD) {
        $maxD = $nearestDistance;
      }
    };

    $prevNearestSpaceStation = $i;
    $noSpaceStation = [];
  }

  return $maxD;
}
