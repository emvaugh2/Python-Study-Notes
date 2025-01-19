letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Use the zip command to tie the above two lists together
letters_to_points = {key:value for key, value in zip(letters, points)}

# Checks to make sure the keys and values were paired properly. 
#print(letters_to_points)

# Adds a key that takes into account blank tiles
letters_to_points[" "] = 0
#print(letters_to_points)

# Defines a function that will add up the score for whatever word we pass to the function based on the values of points above. 
def score_word(word):
  point_total = 0
  for char in word:
    point_total += letters_to_points.get(char)
  return point_total

# Creates a variable called brownie_points for testing our function
brownie_points = "BROWNIE"

# Prints the point total for BROWNIE which should be 15 points. 
#print(score_word(brownie_points))

# Creates a new dictionary for our project
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

# Make sures our dictionary was made properly. 
#print(player_to_words)



# Makes our last task a function that could be called on at any time. 
def update_point_totals():
  player_to_points = {}

  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
      player_to_points[player] = player_points
  print(player_to_points)




print(update_point_totals())









