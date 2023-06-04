<?php
function gregCalendarLeapYear($y) {
  $dd = 13;

  if ($y % 4 == 0 && $y % 100 != 0):
    $dd = 12;
  elseif ($y % 400 == 0):
    $dd = 12;
  endif;

  return $dd;
}

function julianCalendarLeapYear($y) {
  if ($y % 4 == 0):
    return 12;
  endif;
    
  return 13;
}

function dayOfProgrammer($year) {
  $dd = 26;

  if (!($year == 1918)):
    if ($year > 1918):
      $dd = gregCalendarLeapYear($year);
    else:
      $dd = julianCalendarLeapYear($year);
    endif;
  endif;

  return "$dd.09.$year";
}
?>
