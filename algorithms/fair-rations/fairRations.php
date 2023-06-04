<?php
  function fairRations($B) {
    $n = 0;
    for ($i = 0; $i < count($B); $i++) {
      if ($B[$i] % 2 <> 0 && !($i == count($B) - 1))  {
        $B[$i]++;
        $B[$i + 1]++;
        $n += 2;
      }
    }
    
    $j = count($B) - 1;
    
    for ($i = 0; $i < count($B); $i++) {
      if ($i > $j) {
        break;
      }
      if ($B[$i] % 2 <> 0 || $B[$j] % 2 <> 0) {
        return "NO";
      }
            
      $j--;
    }

    return strval($n);
  }
?>