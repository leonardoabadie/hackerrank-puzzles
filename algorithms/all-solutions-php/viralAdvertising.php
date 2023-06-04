<?php
function viralAdvertising($theDayToReport) {
    $cumulativeLikes 0;
    $shared = 5;
    for ($day = 1; $day <= $theDayToReport, $day++) {
        $whoLiked = intdiv($shared, 2);
        $cumulativeLikes += $whoLiked;
        $shared = $whoLiked * 3;
    }
    return $cumulativeLikes;
}
?>