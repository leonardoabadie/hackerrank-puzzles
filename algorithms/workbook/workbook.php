<?php
function workbook($n, $k, $arr) {
  $result = 0;
  $page = 1;

  foreach($arr as $e) {
    $tmp = 1;      
    
    for ($i = 1; $i <= $e; $i++) {     
      if ($tmp > $k) {
        $page++;
        $tmp = 1;
      }
      if ($i == $page) {
        $result++;
      }

      $tmp++; 
    }
    
    $page++;
  }
  
  return $result;
}
?>
