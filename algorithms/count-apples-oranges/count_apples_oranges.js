function countApplesAndOranges(s, t, a, b, apples, oranges) {
  let land_apples = apples.filter(function(apple) {
    return a + apple >= s && a + apple<= t; 
  });

  let land_oranges = oranges.filter(function(orange) {
    return b + orange >= s && b + orange <= t; 
  });
}

