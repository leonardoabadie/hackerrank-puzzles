<?php
function chocolateFeast($moneyToSpend, $barCost, $wrappersPerBar) {
	$newBars = intdiv($moneyToSpend, $barCost);
	$wrappers = $newBar;
	$chocolateEaten = $newBars;
	$remainWrappers = 0;

	while ($wrappers >= $wrappersPerBar) {
		$newBars = intdiv($wrappers, $wrappersPerBar);
		$remainWrappers = $wrappers - ($newBars * $wrappersPerBar);
		$wrappers = $newBars + $remainWrappers;
		$chocolateEaten += $newBars;
	}

  return $chocolateEaten;
}
?>
