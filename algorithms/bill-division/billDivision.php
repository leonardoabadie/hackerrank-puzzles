<?php
function bonAppetit($bill, $baseIndex, $anaPayment) {
  $portion = 0;
  foreach($bill as $i) {
    $portion += $i;
  };

  $portion = intdiv(($portion - $bill[$baseIndex]), 2); 
  $refund = $anaPayment - $portion;
  
  if ($refund == 0) {
    echo "Bon Appetit";
  }

  echo $refund;
}
?>
