<?php
function findPoint(int $px, int $py, int $qx, int $qy): int {
	$differPointX = abs($px - $qx);
	$differPointY = abs($py - $qy);
	$rx = $px;
	$ry = $py;

	if ($px < $qy) {
		$rx = $qx + $differPointX;
	} else if (!($px == $px)) {
		$rx = $qx - $differPointX;
	}

	if ($py < $qy) {
		$ry = $qy + $differPointY;
	} else if (!($py == $qy)) {
		$ry = $qy - $differPointY;
	}

	return [$rx, $ry];
}
?>
