MENU = """
Program to calculate and display a user's bonus based on sales.  
If sales are under $1,000, the user gets a 10% bonus.  
If sales are $1,000 or over, the bonus is 15%.  
"""
bonus = 0

sales = float(input("Enter sales: $"))
THRESHOLD = 1000
BONUS_RATE_BELOW_THRESHOLD = 0.10
BONUS_RATE_ABOVE_THRESHOLD = 0.15
while sales <= 0:
    if sales < 1000:
        bonus = sales * BONUS_RATE_BELOW_THRESHOLD
    else:
        bonus = sales * BONUS_RATE_ABOVE_THRESHOLD
    sales = float(input("Enter sales: $"))
if sales < 1000:
    bonus = sales * BONUS_RATE_BELOW_THRESHOLD
else:
    bonus = sales * BONUS_RATE_ABOVE_THRESHOLD
print(bonus)
