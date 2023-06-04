def get_money_spent(keyboard_prices:list, usb_drive_prices:list, badget:int) -> int:
  money_spent = max(keyboards_prices) + max(usb_drive_prices)
  
  return money_spent (if money_spent <= badget) else -1
