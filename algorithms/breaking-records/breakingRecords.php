<?php
function breakingRecords($score) {
  $lastMinScore = $lastMaxScore = $score[0];
  $minScore = $maxScore = 0;

  foreach ($score as $point) {
    if ($point > $lastMaxScore) {
      $lastMaxScore = $point;
      $maxScore++;
    }

    if ($point < $lastMinScore) {
      $lastMinScore = $point;
      $minScore++;
    }
  };

  $result = array($maxScore, $minScore);
  return $result;
}
?>
