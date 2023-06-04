<?php
function angryProfessor($k, $a) {
  $count = 0;
  foreach($a as $i) {
    if ($i <= 0) {
      $count += 1;
    }
  }

  if ($k <= $count) {
    return "NO";
  }

  return "YES";
}
?>
