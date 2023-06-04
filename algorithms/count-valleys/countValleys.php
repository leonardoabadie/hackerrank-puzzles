<?php
function countValleys($steps, $path) {
  $seaLevel = $crossedValleys = $count = $prevCount = 0;

  foreach ($path as $step) {
    $prevCount = $count;

    if ($step === "U") {
      $count++;
    } else {
      $count--;
    }

    if ($count == $seaLevel && !($prevCount > $seaLevel)) {
      $crossedValleys++;
    }
  }

  return crossedValleys;
}
?>
