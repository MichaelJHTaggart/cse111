# You work for a retail store that wants to increase sales on Tuesday and Wednesday,
# which are the store’s slowest sales days. 
# On Tuesday and Wednesday, if a customer’s subtotal is $50 or greater, 
# the store will discount the customer’s subtotal by 10%.

# Get subtotal
subtotal = float(input("Please enter the subtotal. "))

# Get day of week
from datetime import datetime
current_datetime = datetime.now()
day_of_week_integer = current_datetime.weekday()
days_of_week_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_of_week_name = days_of_week_names[day_of_week_integer]

if subtotal > 50:
    # newSubtotal is discounted 10%
    discount_amount = subtotal * .10
    subtotal = subtotal - discount_amount

    # Finally add 6% sales tax
    sales_tax_amount = subtotal * .06
    subtotal = subtotal + sales_tax_amount

    # Return the final total.
    print(f"Because of our {day_of_week_name} SALE, You got 10% off your order! Your total is: ${subtotal:.2f}")
else :
    # Finally add 6% sales tax
    sales_tax_amount = subtotal * .06
    subtotal = subtotal - sales_tax_amount

    # Return the final total.
    print(f"Your total is: ${subtotal:.2f}")