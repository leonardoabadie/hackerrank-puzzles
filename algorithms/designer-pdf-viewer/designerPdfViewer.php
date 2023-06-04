<?php
function designerPdfViewer($h, $word) {
  $alphabetic = "abcdefghijklmnopqrstuvwxyz";
  $heights = [];

  foreach ($word as $letter) {
    $i = strpos($alphabetic, $letter);
    $heights[] = $h[$i];
  }
  $highlightedArea = max($heights) * count($word);

  return $highlightedArea;
}
?>