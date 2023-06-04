<?php
// Goal: insert a Node at the Tail of a Linked List

$_fp = fopen("php://stdin", "r");

$node_count = intval(trim(fgets(STDIN)));

for ($i = 0; $i < $node_count; $i++) {
    $node = rtrim(fgets(STDIN), "\r\n");
    echo $node, "\n";
}

fclose($_fp);
?>
