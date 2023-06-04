<?php
// Alternative Solution (2)

function flatlandSpaceStation($n, $c) {
    if ($n == count($c)) {
        return 0;
    }

    $noSpaceStation = [];
    $prevNearestSpaceStation = min($c);
    $maxD = 0;

    for ($i = 0; $i < $n; $i++) {
        if (!(in_array($i, $c))) {
            array_push($noSpaceStation, $i);
            continue;
        }

        foreach ($noSpaceStation as $city) {
            $tmp = [abs($city - $prevNearestSpaceStation), abs($city - $i)];
            $nearestDistance = min($tmp);
            if ($nearestDistance > $maxD) {
                $maxD = $nearestDistance;
            }
        };

        $prevNearestSpaceStation = $i;
        $noSpaceStation = [];
    }


    return $maxD;
}

// Alternative Solution (3)

function flatlandSpaceStation($n, $c) {
    if ($n == count($c)) {
        return 0;
    }

    $prevNearestSpaceStation = min($c);
    $maxD = 0;
    $start = True;

    for ($i = 0; $i < $n; $i++) {
        if (!(in_array($i, $c)) && $start) {
            if ($start) {
                $initialValue = $i;
                $start = False;
            }
            continue;
        }

        for ($j = $initialValue; $j < $i; $j++) {
            $nearestDistance = min(abs($city - $prevNearestSpaceStation), abs($city - $i));
            if ($nearestDistance > $maxD) {
                $maxD = $nearestDistance;
            }
        }

        $prevNearestSpaceStation = $i;
        $start = True;
    }

    return $maxD;
}

// Alternative Solution (4) inspired by ''

function flatlandSpaceStation($n, $c) {
    if ($n == count($c)) {
        return 0;
    }

    sort($c);
    $maxD = min($c);
    $tmp = 0;

    foreach ($c as $spaceStation) {
        $middleCity = intdiv(($spaceStation + $tmp), 2);
        $distance = min($middleCity - $tmp, $spaceStation - $middleCity);
        if ($distance > $maxD) {
            $maxD = $spaceStation;
        }
        $tmp = $spaceStation;
    };

    if (($n - 1) - $spaceStation > $maxD) {
        $maxD = ($n - 1) - $spaceStation;
    }

    return $maxD;
}
?>