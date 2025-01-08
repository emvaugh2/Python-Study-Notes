

# Description for the Lovely Loveseat
lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
"""

# Price for the Lovely Loveseat
lovely_loveseat_price = 254.00

# Description for the Stylish Settee
stylish_settee_description = """
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
"""
# Price for the Stylish Settee
stylish_settee_price = 180.50

# Description for the Luxurious Lamp
luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
"""

# Price for the Luxurious Lamp
luxurious_lamp_price = 52.15

# Have to account for sales tax
sales_tax = .088

# Total for the customer for price 
customer_one_total = 0

# Total for the customer in terms of items
customer_one_itemization = ""

# Customer has decided to purchase a Lovely Loveseat
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

# Customer has decided to purchase a Luxurious Lamp
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

# Calculates the customer's sales tax
customer_one_tax = customer_one_total * sales_tax

# Adds the sales tax to the customer's total
customer_one_total += customer_one_tax

# Prints out the customer's itemization portion of receipt
print("Customer One Items:")
print(customer_one_itemization)

# Prints out the customer's total price portion of the receipt
print("Customer One Total:")
print(customer_one_total)
