def calculate_tip(bill_amount, tipPercentage):
   # Tu código aquí 👈
   tip_value = round(bill_amount*tipPercentage/100,2)
   return tip_value

print(calculate_tip(100,10))
print(calculate_tip(1524.33,25))