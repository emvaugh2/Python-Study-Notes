# What's the weight of the package?

weight = 41.5 # Weight is in pounds (lbs)

# How do you want to ship your package?
# Options are ground_shipping, ground_shipping_premium, and drone_shipping

shipping_option = "ground_shipping"

# Defines the total price value
total = 0

# Calculates the price based on Ground Shipping and weight
if shipping_option == "ground_shipping":
  if weight <= 2: # Weight is less than 2lbs
    total = 1.5 * weight + 20
  elif 2 < weight <= 6: # Weight is betwen 2lbs and 6lbs
    total = 3 * weight + 20
  elif 6 < weight <= 10: # Weight is betwen 6lbs and 10lbs
    total = 4 * weight + 20
  else: # Weight is over 10lbs
    total = 4.75 * weight + 20 

# Calculates the price based on Ground Shipping Premium
if shipping_option == "ground_shipping_premium":
  total = 125

# Calculates the price based on Drone Shipping and weight
if shipping_option == "drone_shipping":
  if weight <= 2: # Weight is less than 2lbs
    total = 4.5 * weight
  elif 2 < weight <= 6: # Weight is betwen 2lbs and 6lbs
    total = 9 * weight
  elif 6 < weight <= 10: # Weight is betwen 6lbs and 10lbs
    total = 12 * weight
  else: # Weight is over 10lbs
    total = 14.25 * weight 

# Prints the calculated total
print(total)