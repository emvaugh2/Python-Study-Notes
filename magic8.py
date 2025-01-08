# Imports the package for the .randint() command for generating random numbers
import random

# Name of the person asking the 8-ball a question
name = "Edward"

# Question the user will be asking
question = "Will I ever become a cloud engineer?"

# The 8-ball's answer
answer = ""

# Generates a random integer number from 1 to 9
random_number = random.randint(1,9)

# Case statement to give a different answer for each randomly generated integer regardless of the answer that was chose

match random_number:
  case 1:
    answer = "Yes - definitely"
  case 2:
    answer = "It is decidedly so"
  case 3:
    answer = "Without a doubt"
  case 4:
    answer = "Reply hazy, try again"
  case 5:
    answer = "Ask again later"
  case 6:
    answer = "Better not tell you now"
  case 7:
    answer = "My sources say no"
  case 8:
    answer = "Outlook not so good"
  case 9:
    answer = "Very doubtful"
  case default:
    answer = "Error"

print(name + " ask: " + question)
print("Magic 8-Ball's answer:",answer)
