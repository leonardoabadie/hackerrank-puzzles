<?php
function isFactor($a, $b, $x) {
    $divResultA = [];
    $divResultB = [];

    foreach ($a as $num) {
        // True if an element 'a' is a factor
        $divResultA[] = ($x % num)==0;
    };
    foreach ($b as $num) {
        // True if 'x' is a factor
        $divResultB[] = ($num % $x)==0;
    };

    if (!(in_array(false, $divResultA)) && !(in_array(false, $divResultB))) {
        return true;
    }

    return false;
}

function getTotalX($a, $b) {
    $betweenThem = 0;

    if (array_sum($a) <= array_sum($b)) {
        // max(a) ~ (min(b) + 1) => range of numbers between the two sets
        for ($x = max($a); $x <= min($b); $x++) {
            if (isFactor($a, $b, $x)) {
                $betweenThem++;
            }
        }
    }

    return $betweenThem;
}
?>