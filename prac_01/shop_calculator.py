DISCOUNT_RATE = 0.1
total_price = 0
number_of_items = int(input('Number of items:'))
for i in range(0, number_of_items):
    price = float(input('Price of item:'))
    while price <= 0:
        print('invalid price')
        price = float(input('Price of item:'))
    total_price += price
if total_price >= 100:
    total_price = total_price-total_price*DISCOUNT_RATE
print(f"Total price for {number_of_items} items is ${total_price:.2f} ")

