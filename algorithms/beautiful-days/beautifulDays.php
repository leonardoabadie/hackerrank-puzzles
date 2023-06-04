<?php
function ($days, $k) {
  $beautifulDays = 0;
    
  foreach ($days as $day) {
    $reverseDay = int(strrev(strval($day)));
    if (($day - $reverseDay) % k == 0) {
      $beautifulDays++;
    }
  };

  return $beautifulDays;
}

function listDays($i, $j) {
  $d = array();
  for ($k = $i; $k <= $j, $k++) {
    $d[] = $k;
  };

  return $d;
}

function beautifulDays($i, $j, $k) {
  $days = listDays($i, $j);
  return filterBeautifulDays($days, $k);
}
?>
