def designerPdfViewer(h:list, word:str) -> int:
  alphabetic = list("abcdefghijklmnopqrstuvwxyz")
  heights = list()
  for letter in word:
    i = alphabetic.index(letter)
    heights.append(h[i])

  highlighted_area = max(heights) * 1 * len(word)

  return highlighted_area 