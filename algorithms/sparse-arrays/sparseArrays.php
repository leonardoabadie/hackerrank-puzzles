<?php
function matchingStrings($strings, $queries) {
  $result = array();

  foreach($queries as $query) {
    array_push($result, substr_count($strings, $query));
  }

  return $result;
}
?>
