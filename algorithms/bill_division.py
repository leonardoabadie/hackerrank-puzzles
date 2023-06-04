from functools import reduce
# My solution 1:
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

# My solution 2:
def bonAppetit(bill, base_index, ana_payment):
    portion = (reduce(lambda item_x, item_y: item_x + item_y, bill) - bill[base_index]) // 2
    refund = ana_payment - portion
    print("Bon Appetit") if (refund == 0) else print(refund)
