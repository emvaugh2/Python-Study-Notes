# Import the necessary modules
import datetime as dt
from decimal import Decimal
import random
import custom_module

# This uses the datetime module to get the current date and time. These are some type of objects apparently. We can't just treat them as strings. 
current_date = dt.date.today()
current_time = dt.datetime.now().time()

# Just prints the values to make sure the function is working properly. 
# print(current_date)
# print(current_time)

# This is how we calculate the base cost and the cost multiplier. Apparently the base cost is arbitrary. 
base_cost = Decimal('100.00')
cost_multi = abs(int(2025 - random.randint(2025, 3001)))

# Just prints the variables to make sure we're getting something. 
# print(base_cost)
# print(cost_multi)
# print(type(current_date))

# This calculates the final cost. 
final_cost = base_cost * Decimal(cost_multi)

# print(final_cost)

# Uses the random function to generate the target year. 
target_year = random.randint(2025, 3001)

# Going to create a list of destinations and then select one of them

dst = ["Paris", "Center of Earth", "Edge of Andromeda", "Heaven", "Hell", "My Grandmother's House"]
final_dst = random.choice(dst)

# print(final_dst)

# Calls the function and prints it. 
print(custom_module.generate_time_travel_message(target_year, final_dst, final_cost))








