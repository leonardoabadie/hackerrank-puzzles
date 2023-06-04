<?php
function countApplesAndOranges($s, $t, $a, $b, $apples, $oranges) {
  $landApple = 0;
  $landOrange = 0;

  foreach ($apples as $apple) {
    if (($a + $apple >= $s) && ($a + $apple <= t)) {
      $landApple++;
    }
  };

  foreach ($oranges as $orange) {
    if (($b + $orange >= $s) && ($b + $orange <= $t)) {
      $landOrange++;
    }
  };

  echo "$landApple\n$landOrange";
}
?>
