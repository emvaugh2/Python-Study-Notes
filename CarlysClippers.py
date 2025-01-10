hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]


# Creates a variable for total_price
total_price = 0

# Loops through all the prices and adds them up
for price in prices:
  total_price += price

print(total_price)

# Takes the average of the total prices by taking the total price variable and dividing it by the amount of prices
average_price = total_price / len(prices)
print("Average Haircut Price: $" + str(average_price))

# Makes a comprehension list that cuts all prices by $5
new_prices = [price - 5 for price in prices]
print(new_prices)

# Creates a variable for total revenue
total_revenue = 0

# Takes the product of the hairstyle plus the amount of people who got the hairstyle last week and sums it for the total revenue. 
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]

print("Total Revenue: $" + str(total_revenue))

# Finds the daily average revenue
average_daily_revenue = total_revenue / 7

print(average_daily_revenue)

# Makes a comprehension list that collects all the haircuts that are under $30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]

print(cuts_under_30)












