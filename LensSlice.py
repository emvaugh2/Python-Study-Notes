# Your code below:


# Creates the kinds of pizza we sell
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

print(toppings)

# Tells us the price of each kind of pizza
prices = [2, 6, 1, 3, 2, 7, 2]
print(prices)

# Counts the number of times "2" appears in the list prices. 
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# Calculates the number of types of pizzas. 
num_pizzas = len(toppings)
print(num_pizzas)

# This will print We sell [num_pizzas] different kinds of pizza!, where [num_pizzas] represents the value of our variable num_pizzas.
print("Well sell",num_pizzas,"different kinds of pizza!")

# Makes a new 2D list of pizza and prices with the prices value coming first. 
pizza_and_prices =[[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
print(pizza_and_prices)

# Sorts the pizza_and_prices list in numerical order. 
pizza_and_prices.sort()
print(pizza_and_prices)

# Stores the first element in the new table 
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)

# Stores the last element in the new table 
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)

# Deletes lasts value in our list
pizza_and_prices.pop()
print(pizza_and_prices)

# Inserts our new pizza slice in the proper price place. 
pizza_and_prices.insert(4,[2.5, "peppers"])
print(pizza_and_prices)

# Takes the first three elements of our list and stores it in a variable
three_cheapest = pizza_and_prices[0:3]
print(three_cheapest)


