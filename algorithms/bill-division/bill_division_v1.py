from functools import reduce

def bonAppetit(bill, base_index, ana_payment):
  half_price = int()

  for i, item in enumerate(bill):
    if i != base_index:
      half_price += item

  result = ana_payment - (half_price // 2)
  if result == 0:
    print("Bon Appetit")
  else:
    print(result)

