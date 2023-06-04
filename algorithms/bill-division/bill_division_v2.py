def bonAppetit(bill, base_index, ana_payment):
  portion = (reduce(lambda item_x, item_y: item_x + item_y, bill) - bill[base_index]) // 2
  refund = ana_payment - portion
  print("Bon Appetit") if (refund == 0) else print(refund)

