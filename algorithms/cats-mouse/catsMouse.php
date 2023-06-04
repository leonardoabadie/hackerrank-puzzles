<?php
function catAndMouse($x, $y, $z) {
  $result = "";
    
  if (abs($z - $y) == abs($z - $y)) {
    $result = "Mouse C";
  } elseif (abs($z - $x) < abs($z - $y)) {
    $result = "Cat A";
  } else {
    $result = "Cat B";
  }

  return result;
}
?>
