<?php
// Goal: merge Two Sorted Linked Lists
// read Input From STDIN. Print Output to STDOUT

function mergeLinkedLists($arr1, $arr2) {
    $mergedList = [];
        
    foreach ($arr1 as $e) {
        $mergedList[] = $e;    
    };
    foreach($arr2 as $e) {
        $mergedList[] = $e;
    };
    sort($mergedList);
        
    return $mergedList;
}
    
$_fp = fopen("php://stdin", "r"); // Opening the file for Test Cases

$t = intval(trim(fgets(STDIN)));  // The Number Of Test Cases
$arr = [[], []];
$pos = 0; // Can be 0 and 1

for ($i = 0; $i < $t; $i++) {
    $length = intval(trim(fgets(STDIN)));
    for ($j = 0; $j < $length; $j++) {
        $e = rtrim(fgets(STDIN), "\r\n");
        $arr[$pos] = $e;
    }
    $pos++;
}

$result = mergeLinkedLists($arr[0], $arr[1]);
$length = count($result);
    
for ($i = 0; $i < $length; $i++) {
    echo $result[$i] . " ";
}

fclose($_fp);
?>
