<?php
function dynamicArray($n, $queries) {
    $lastAnswer = 0;
    $arr = [];
    $result = [];
    // Creating an $arr of $n empty arrays
    for ($i = 0; $i < $n; $i++) {
        array_push($arr, []);
    }

    // Performing the queries
    foreach ($queries as $q) {
        $queryType = $q[0];
        $x = $q[1];
        $y = $q[2];
        $idx = (($x ^ $lastAnswer) % $y);

        if ($queryType === "1") {
            array_push($arr[$idx], $y);
        } else {
            $lastAnswer = $arr[$idx][$y % count($arr[$idx])];
            array_push($result, $lastAnswer);
        }
    };

    return $result;
}
?>