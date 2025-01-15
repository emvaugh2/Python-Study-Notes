# Python-Study-Notes


**I'll fill in a description later on. Just sit down and watch me do my thang.**

## 01.16.2025

**Today's Topics**

* Learning Python 3 (Modules)

Python allows us to package code into files called modules. They're often called libraries or packages. A package is really a directory that holds a collection of modules. 

To use a module in a file, it usually follows the syntax: `from module_name import object_name`.

A namespace isolates the functions, classes, and variables defined in the module from the code in the file doing the importing. Your local namespace, meanwhile, is where your code is run.

You can give your module an aliase if you want to change the name of it for your own convenience. For example, `import module_name as name_you_pick_for_the_module`.

You can import you own functions in your own librarys. Lets say you have a script called `library.py` and you have a function in it called `def duel_masters(cards)`. Say you open up another Python script and you want to use that function. At the top of your new script, you can do `from library import duel_masters` and then you can use that function in your new script. 


Project - Time Traveler's Toolkit


## 01.15.2025

**Today's Topics**

* Learning Python 3 (Strings)


We'll finish up strings today. I want to get through the Coding Challenge for Strings (so I'm skipping to the end for a bit but I want to make sure all these methods don't escape me before I get to it) and I have to finish the "Project". So we'll focus on that and if we have more time, we'll move to the next chapter (Modules). 

I went through both the Strings and Strings (Advanced) section of the Python Coding Challenges. These were way easier than I thought they would be. The Flow / Loop ones were by far the hardest which is weird because I have the most experience with those. 

Project - Thread Shed

I already know this is going to be a nightmare. I feel like I had to do multiple unnecessary loops to break apart these values. I have a new-found respect for Power BI and data cleaners. I can only image what they go through now. We basically had to take a huge string that was stored in a weird format (Name, Sale Amount, thread color and date) and clean it up so we can get each customer name in one list, the total sales, and the number of thread colors sold for that date. For insight, there were about 30 entries and all of this was stored in one long string. The string was internally separated by commas and each value was separated by `;,;` notation. So we had to remove that notation, break each input into one list, remove the leading and trailing whitespaces, and take each entry and put that into the proper list. We had to convert all the sales into a floating decimal by removing the dollar sign and converting it from a string to a decimal. We then totaled that up. The project also required us to see how many of each color thread we sold. There were about 7 colors and half the entries had more than one color (up to 3). We had to separate these values into two different lists and then the multi-color list was split into internal, separated lists and then all the colorss were split into indidivual elements. We then added both of those lists together and created a function to get the total amount of each color in the list. 

We then made a loop and used the `.format()` method to print out a list of how many of each color were sold for that day. 

Phew. 


## 01.14.2025

**Today's Topics**

* Learning Python 3 (Strings)

Alright there are two sections for this for a total of 3 hours and 40 minutes of material. So it's going to take a while to get through this. 

A string can also be thought of as a list of characters. Each character is an index in your string. You reference each letter just like you do a list with the `[]` brackets. 

If you use `len.()` to found the length of a string, this also takes into account the spaces in the string. So be aware of this. 

Immutable - unable to change it once it is created. Strings are immutable (which is funny because lists are mutable). So strings are a special class of list. You can not change them. 

Just like in Linux, you have the escape character `\`. So for example, whenever you end off a single or double quotation, you conclude that string. You can't do `string_word = "I need to quote"this saying here""` because those extra double quotes are going to end the variable and cause that weird variable in the middle. It's a syntax error. If you want to include those double (or single) quotes in the variable without Python assuming you want to end the variable, you use the escape character. The escape character tells Python "Treat this like a normal character, not a syntax character". Therefore, if you want the escape character in front of the double quote `\"`, Python will just read the double quota as a character just like S or p or `.`. Just keep this in mind. 

Strings have a special syntax command called `in`. This checks if one string is a part of another string. You can do `letter in word` and it will return a boolean answer of True or False. This works on letters and entire words in strings. Or entire strings in strings. 

Python comes with built-in string methods that give you the power to perform complicated tasks on strings very quickly and efficiently. They have the format: `string_name.string_method(arguments)`. For example, `'Hello world'.lower()` will yield `'hello world'`. The first three will be `.lower()`, `.upper()`, and `.title()`. These will make the entire string lowercase, uppercase, or capitalize the first letter in every word of the string. 

String methods create new strings. They do not change the original string. 

You can use `.split()` to take every word in a string and create a list with each element in the list being each word in the string. So if you have `random_string = "I go to school."` and split it up, you'll get `random_list = random_string.split() = ["I", "go", "to", "school."]`. The delimiter is automatically spaces unless specified otherwise. The delimiter can be anything such as a space, comma, colon, or even a letter or another string. Think of `.split()` as removing whatever that delimiter is. So if the delimiter is `"n"`, it will split the strings at the n's and also remove the n's. 

We also have escape sequences just like the escape character. So with the character, we wanted to make sure we stayed in our string no matter if we put some additional quotation marks in our string. An escape sequence is still in the same vein as the `.split()` method though. It allows us to split the string up at specific places such as a newline or a horizontal tab. `\n` is for a newline and `\t` is for a horizontal tab. So if you do `random_string.split('\n')`, then the output would be the string that you have separated (or split) at each line break. Same thing for the tab. 

We'll use `.join()` to put strings together with a given delimiter. The syntax is backwards compared to the `.split()` syntax. You have `'delimiter'.join(list_you_want_to_join)`. You can use commas as the delimiter to get comma-separated values (CSV). You can also use escape sequences as the delimiter which is how you can break these different values into different lins. 

You can use `.strip()` (STRIP, not SPLIT) to get rid of leading and trailing spaces in a value. It won't get rid of the spaces in the middle of the string element. Just all the ones before and after it. You can do this with different characters too such as "!" and the such. 

I'm going to forget all of this syntax. It's a lot. I'm going to have to review this. 

Now we have the `.replace()` method which takes two arguments and replaces each instance of the first argument with the second argument. It replaces them. The syntax is `string_name.replace(substring_being_replaced, new_substring)`. You can also do this with spaces and commas and stuff. The world is yours. Don't limit your solutions. 

Now you have the `.find()` string method. This will take a string and will find the first index that the value you're looking for starts on. Whether you supply the method a letter, series of letters, or a whole word, it will find the first index value of when that argument is found. Yes, it counts indices from 0 all the way up to whatever so this can be a very large number. Syntax is `print('smooth'.find('t'))     # => '4'`

Now you have the `.format()` method. This is like an easier way to concatenate strings or whatever. Add strings together. Usually we use the formm `"I like " + str(favorite_cake) + " with " + str(favorite_ice_cream).` which can make things hard to read (not legible) and just clunky. We can use the `.format()` method to tell the code where to automatically add these values into a line. The syntax is 

def favorite_song_statement(song, artist):
  return "My favorite song is {} by {}.".format(song, artist)

print(favorite_song_statement("Smooth", "Santana"))
(which will spit out) "My favorite song is Smooth by Santana."

So wherever you put the curly brackets, that's where those arguments will go. You can kind of picture it a little better when reading your code. You can pass as many arguments as you want to the function as long as you have the same amount of curly brackets. 

You can take it a step further by using this syntax:

def favorite_song_statement(song, artist):
  return "My favorite song is {song} by {artist}.".format(artist=Santana, song=Smooth)

So you can specify exactly what should pop up where. It doesn't even have to be in order as you can see from above. I actually like this even better. Might do this instead of doing that + concatenate bull jive. 

Lord this exercise at the end is a little difficult to think through hahahaaa. I'm glad I have instructions although I have to come up with the code myself. This makes me appreciate Power BI or whatever people are using to scrub data even more. I see how crazy this can get doing this by hand.  

Project - Thread Shed

I already know this is going to be a nightmare. 



## 01.13.2025

**Today's Topics**

* Learning Python 3 (Python Code Challenge)

Okay I finished up the second half of this. The Loop coding challenges gave me the most run for my money but it was only about 3 of them that gave me some problems. Or at least it took me a second to work through them. All of the function coding challenges were easy. The list coding challenges gave me a few index errors (which were my fault because I kept forgetting 0 is an index when computing the `range()` function) but overall I was pretty good. Lets move onto strings. 


## 01.12.2025

**Today's Topics**

* Learning Python 3 (Python Code Challenge)

I'm not really taking notes on this. I'm just going through the challenges. This is actually taking longer than the prescribed time that they said on Codecademy but that's okay. I've only struggled with 2 of the 20 so far. I've only gotten 1 wrong. 

Nothing today.





## 01.11.2025

**Today's Topics**

* Learning Python 3 (Functions)

A functin is a convenient way to group our code into reusable blocks. A function contains a sequence of steps that can be performed repeatedly throughout a program without having to repeat the code. 

def function_name():
  <define function tasks here>

The `def` keyword indicates the beginning of a function. It's also called the function header. It's followed by the name of the function (function_name). The parentheses can hold input values. In this example, we have no parameters. We also need a colon `:` at the end of our function name. Then we can put statements after the function to make up our function. 

The process of executing the code inside the body of a function is known as calling it. To call a function in Python, type out its name followed by the parentheses. You can only call a function AFTER it has been defined in your code. 

Difference between parameter and argument: The parameter is what you define when you create the function. It's literally a variable in the defintion of a function. So `def travel(destination):` is the start of a function and `destination` is the parameter. An argument is the actual value you pass to the function when you're using the function. It would be real value of the `destination` parameter. So when you call a function `travel("Japan")`, you're passing the argument `"Japan"` to the function. The parameter takes on the argument value. 

All values calculated in your function will not leave your function. Once you call it, your function does its thing but it won't give you any values. If you want your function to spit out a value that you can assign to a variable, you'll have to include `return <insert value or variable you want>` at the end of the function. That way, you can low key create a variable and make it equal to your function. Your function will run and the return value will be given to the variable. Then you can print it and see. This is called a returned function value. 

You can return multiple values by separating them by commas. For example, `return budget, expense, credit_card_balance`. You can store those values by listing out three variable names like `money, debt, CC = flight()` where flight is the function that will return budget, expense, and credit_card_balance values. Money will take on the value of budget, debt will take on the value of expense, and CC will take on the value of credit_card_balance. I feel like you can also create an empty list and store them there. Maybe you can also do the `.append` method too. 


Also, there are different ways to define arguments in your function. You can make them have a default value. You can tell your function exactly which variables you want to assign a value to so the position of the argument doesn't matter when you're passing arguments to it. There are positional arguments, keyword arguments, and default arguments. 

There are built-in functions and user defined functions. 

The `map()` function allows you to use a function over multiple iterables (so values in a list). Say you have a list of numbers called `numbers` and a function called `double` which just doubles the number. The function returns the value as well. You can iterate over the list of numbers by doing `doubled_numbers = map(double, numbers)`. You can use this for built-in functions too. 

Lambda functions are quick functions we can spin up without having to go through the normal syntax. The syntax for a lambda function is `lambda <parameter>: <expression>, <argument`. For example, if we have an expression that squares a number so `x ** 2` which is the equivalent of x^2. That would be our expression. Our parameter would be x because that's the variable we are using in our expression. The argument would be the value we feed to the variable (lets say 4). So the lambda function would like like `lambda x: x ** 2, 4` which would return a value of 16 since 4^2 is 16. Your argument can be a list as well. 

You can use `map()` functions and lambda functions together. Just put the lambda function into the map function. Now I don't know what type of object the `map()` function returns but I'm noticing they're encasing the `map()` function in a `list()` function (so `list(map())` ) so this leads me to assume that you need to convert your `map()` output to a list. Just like with the `zip()` function zip object. Yes I just came across this sentence: "The `map()` function in Python returns a map object, which is an iterator." I'm not entirely sure what an iterator is but I was right about the map object. 

An interator is an object that enables you to iterate through a collection of items, like a list, one element at a time. A map object does not immediately compute or store all the results. Instead, it computes each result on demand, making it memory-efficient. Lets break this down. In a normal `for` loop that you want to iterate over, you may have already created a list or two. Actually, you have to create these variables upfront to feed to your loop. So say you have a list of numbers called `numbers = [1, 2, 3, 4]`. You feed this to your loop to get your desired result (say x squared so `x ** 2`). You already created the list of numbers. Your device has to store all of these values first which uses up memory. With a function like `map()`, you pass these values to your function or lambda function if you're using that but the computer does it one by one and it does it at the time of you calling the `map()` function. It's less taxing on your resources because you don't have to pre-store the list and you can do each iteration one-by-one as they come. 

Project - Getting Ready for Physics Class

We basically had to create a bunch of functions to compute Fahrenheit to Celsius, Celsius to Fahrenheigh, force, energy, and work. Now I loved this because this was like a very basic version of what I did in college. All of the equations were nostalgic. I didn't use any lambda functions here. Just normal functions which I also learned you don't have to assign a variable to your `return` statement. You can just put the operation there. We also used out energy function within our work function so it was nice to see a nested function. 


## 01.10.2025

**Today's Topics**

* Learning Python 3 (Loops)

Pretty familiar with these as well. But lets see what I can learn. 

Anatomy of a Python `for` loop:

for <temporary variable> in <collection>:
  <action>

The temporary variable is arbitrary and doesn't need to be defined beforehand. Think of this as `i` in MATLAB but it can be anything. It can be ingredient, game, horse, n, whatever you want it to be. I'm used to `i` being predefined as well. I guess it will just continue to run through the list no matter what you put. 

More from Chat GPT, the temporary variable is only used in the loop. It won't have any value after the loop is done. The loop iterates for however long you specify it to. If you iterate over a list of 5 values, the loop will iterate 5 times. If you give it a range from 0 - 9 using the range command, it will iterate 9 (or 10?) times. The temporary variable will take on each iteration value of the list you provide. So if your arbitrarily named temp variable is `acc` and you have a list named `acceleration`, for the first iteration, `acc = acceleration[0]`. For the second iteration, it will be `acc = acceleration[1]`. And so forth and so on. You don't even always need a temp variable but that's how it works in iterations. The temp variable values are directly tied to the <collection> values. Whether that's a list, range, string, whatever. Each value in the collection is tied to the first, second, third, etc values of the temp variable. The temp variable takes on those values. 

Anatomy of a Python `while` loop:

while <conditional statement>:
  <action>

`break` statements are for loops (both for and while). They do not apply to if statements although they can be used in if statements to break the for or while loop that incases that statement. 

`continue` statements makes the loop start back from the beginning of the loop code but it moves to the next iteration. So if a condition is met into the loop and you hit continue, the loop won't read any of the code after the continue statement. It will start back from the top at the next iteration. 

I think nested loops are just loops inside of other loops. I'll ask Chat GPT. 

List comprehensions are actually pretty cool. It's like writing a quick, mini loop into your list to do computations. Definitely revisit this. For example, `grades = [90, 80, 62, 76, 74, 89, 48, 57`. You can add 10 to all of these grades by doing `scaled_grades = [10 + score for score in grades]`. You can also use `if-else` statements within these list comprehensions right along with the for loops too. Very nice. I'll paste some examples in a second. 

`This is without the list comprehesion. It doubles all the negative numbers in the list and puts them in a new list.`

numbers = [2, -1, 79, 33, -45]
only_negative_doubled = []

for num in numbers:
  if num < 0: 
    only_negative_doubled.append(num * 2)

print(only_negative_doubled) 

`This is with the list comprehension`

numbers = [2, -1, 79, 33, -45]
negative_doubled = [num * 2 for num in numbers if num < 0]
print(negative_doubled)

`This takes it a step further.`

numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 if num < 0 else num * 3 for num in numbers ]
print(doubled)



Project - Carly's Clippers

Okay I want to first say that I'm proud of myself for working through all these loops. I haven't written any real loops since college and while I brushed up on this again back in 2020, it's been a while. I'm not familiar with list comprehensions too and I think I did a hell of a job. But that's all this project was based on. We had to do a list of list manipulation using for loops and if statements mixed with list comprehensions. The last one gave me some trouble but maybe it's because I haven't eaten today (it's 6pm). But I had to create a new list by taking all the values from a price list that were under $30 and print each haircut that was associated with that under $30 price using a list comprehension. Not very difficult but I didn't truly know how to go about it. There was a hint in the description so I used that and just wrote the code until it made sense to me. I got the right answer. You can check out my code in this repo under the file `CarlysClippers.py`. 




__________________________
## 01.09.2025

**Today's Topics**

* Learning Python 3 (Lists)

Lists are the same thing as arrays in MATLAB. You can put any type of value in a list and mix and match value types. Just separate everything with a comma. 

When we do stuff like `random.randint()`, that `.randint()` portion is called a method. A method is a built-in functionality that we can use to create, manipulate and even delete our data. There are general types of methods. One is the `.append()` method which adds onto the end of a object or list. 

We can add lists together (1 list plus another list) but we can't just add a value of any type to a list. It must be a list plus a list. Or you'll need to append the new value type onto the list. You can also use brackets `[]` to add it to the list as well. 

The location of an element/value in a list is called its `index`. Remember, the first index value is 0. You can access an index value by doing `<list-name>[<index-#>]`. For example, `kings[3]` will give you the 4th value in the `kings` list. 

Wow. So you can use negative numbers to access the elements at the end of the list. So if you do `kings[-1]`, it will get you the last element in the list. If you do `kings[-2]`, it will get you the second-to-last element in a list. And so fourth and so on. 

You can also reassign values in a list by just taking the list name and index and then assign it a new value. 

`.remove()` is another method that's popular. It will remove that index from the list and shrink the list down as well. If there are duplicate occurs of whatever you're removing, it will only remove the first occurrence. 

A 2-D list is a list that contains both numbers and strings. This is like a list in a list though. The format is `heights = [["Noelle", 61], ["Ava", 70], ["Sam", 67], ["Mia", 64]]`. If you want to access a piece of information in this heights list (for example, Ava's heigh), you would do `heights[1][1]` which denotes the second index `[1]` and the second index of that index (also `[1]`). 

Project 1 - Gradebook

We basically did a bunch of list manipulation. This was a very easy project. More of a lab than a project but this was really easy. Just think adding lists and entries. Then using indexing, append, and remove to change entries. I think the most complicated thing I did was add to separate lists together in the table format that they listed in the lab. I did this by making the new list empty and adding each entry by the index of the other two lists. I see they were trying to catch me up because the next tasks said "Print out the tables. Do they look like you thought they would?" I know if I would've just added the lists, it would've had the classes listed first and the grades listed second. You want to have the class and then grade for each class. So that was my way around that. My code will be in the `Gradebook.py` file in this repo. 


We have more methods to take note of. 

First one up is `.insert()`. You can use this as a method for any list variable that you have. It has two inputs: the index and the value you want to place at that index. For example, if you have `new_list.insert(2, "Edward") then the value Edward will be placed in the third spot on the list and the list will automatically shift over. So whatever was in the first and second index [0 and 1], they'll stay put. Whatever was in the 3rd index [2], that will be shifted to the 4th index [3]. 

Next is `.pop()`. You use this to remove an element from a list. This is slightly different than `.insert()` because 1.) if you don't specify an index inside the paratheses, it will just remove the last value in the list and 2.) this actually stores the value that was removed. So technically you can assign a variable to the `.pop()` command and the variable will store it. The only input you need for this command is the index number that you want to remove. So for example, you can do `new_list.pop(2)` and it will remove the 3rd value in the string. Also, you can do `third_value = new_list.pop(2)` to store that value if you wanted to. 

Next, the `range()` built in function. This isnt a method so you will not append it onto a list or something. `range()` will create a list of consecutive integers starting from 0 all the way to one number BEFORE the number you put in. So if you did `range(10)`, it will go from 0 to 0. This will create a list so you have to assign a variable to this output. I think you can also specify a starting value too so just keep your mind open to more possibilities. 

The `range()` function creates a range object so it's not a typical list. I'm not exactly sure what a range object is though. Oh apparently to use it like a list, we have to convert this range object into a list using the `list()` built-in function. Think of it like when you have to use the `str()` command to convert an integer into a string. 

Okay I was right. `range()` is flexible. You can have 2 inputs which will give your function the value you want to start at and then right before the number you want to end at. If you give it a third value, that number will be the distance between numbers in a list. For example if you have `range(1,10,2)` then your output would be [1, 3, 5, 7, 9]. 

Next, we have the `len()` built-in function which is short for length. This will tell you how long a list is. Just put your list inside the paratheses. 

Next, we have slicing which I'll show you how ot do that. Slicing is taking a portion of a list. That's it. Say we only want values 1 - 5 (so index 0 - 4). There's a way to take that from a list and store it into a new list. Lets say you have the original list which is `kings` and it's 10 values long. We only want 1 - 5. So we would do `kings[0:5]` which is weird because you would think this inclues the 5th index. This syntax says go from the 0 index all the way up to the 5th index but not including the 5th index. So that second number will always be one index number pass what you're looking to collect. 

You can do even more with it though. You can do `list_name[:n]` which you can insert whatever number you want for n. This will slice your list from the first index all the way up to the index you specified (so right before that index number). You can also do `list_name[-n:]` which will take the index you specified (so remember, negative numbers start from the end of the list) and slice the list from that number up to the end of the list. You can also do `list_name[:-n]` which is pretty similar to the first one just it stops at the number you listed (which counts backwards from the end of the list). 

Next, we have the `.count()` method. This will tell you the amount of occurrences in a list for whatever value you place in the paratheses. This method returns a value so you can store it in a variable if you want. You can also use this to see the occurrences in a 2-D list. Just put your value in the paratheses. 

Lastly, we have the `.sort()` method. We can use this to sort a list in numerical or alphabetical order. This method doesn't return a value. It just automatically modifies the list. Also, you can use `.sort(reverse=True)` to sort in reverse (so Z to A or 9 to 0). There's also a built-in function for `sorted()`. This will take a list that you have an do the same sorting but will assign it to a variable. For example, `sorted_cities = sorted(cities)` which sorts the values in the list `cities` and assigns to the new list `sorted_cities`. 

Project 2 - Len's Slice

This project was just incorporating everything we've done with lists with the methods and built-in functions. Nothing to really see here but you can see my code in the `LensSlicing.py` file in this repo. 


Tuples - a special type of list. They can't be modified after you create them. More memory efficient. You can create a tuple just like a list but you use the `()` instead of the `[]`. 

You can use the `zip()` command to pair two lists together, each index paired with the corresponding index from the other list. This creates a zip object. You can turn this zip object into a list by using `list()` where the input would be the zip output. This seems useful but it creates a tuple and not a list. I wonder if there's a list version of this. 


__________________________
## 01.08.2025

**Today's Topics**

* Learning Python 3 (Control Flow)

We know what flow control is. This should be a review and for you to hammer down how these loops and statements work in Python. Boolean statements are either true or false and they're verifiable. 

![Image](FlowControl1.png)

Relational operators - compare two values and returns `True` or `False`. So you have the equals operator `==` which will return `True` if both values are the same. Otherwise, `False`. The not equals operator `!=` will return `True` if the values are not equal to each other. Because that's a true statement. 

`True` and `False` are a special variable type called bool. Also, you can use the `type()` syntax to get the type of value for you input such as string, float, integer, bool, etc. 

Our `if` statements are in the format of

if <statement>:
  <action>

Where `if` kicks off the conditional statement and `:` is the "then". Say this every time you write these statements.

Okay remember we have more relational operators. We have `>`, `>=`, `<`, and `<=`. 

Now we have Boolean operators: `and`, `or`, and `not`. Lets start with the first one. The `and` will combine two Boolean expressions and resolve to `True` if both Boolean expressions are true. The `or` will evaluate as `True` as long as one of the expressions is true. If they are both `False`, then it will return `False`. Lastly, the `not` operator reverses the boolean value. So I would evaluate the expression first and whatever that expression is (True or False), take the opposite of that. 

Remember, if an `if` statement is `False`, it won't run. 

Switch-case statements and match-case statements are the same thing. But think of them as a cleaner way to write if-else statements with a bunch of elifs. Here's the syntax below:

match expression:  
    case value_1:  
        # code to execute when expression equals value_1  
    case value_2:  
        # code to execute when expression equals value_2  
    case value_3:  
        # code to execute when expression equals value_3  
    case value_4:  
        # code to execute when expression equals value_4  
    case value_N:  
        # code to execute when expression equals value_N  
    case default:  
        # code to execute when expression isn't equal to any of the values 

Only one case block is executed in the entire match block for any given value of expression. Once a case block is executed, the program’s control flow moves out of the match block.


You can use the `input()` syntax to prompt a user to give you an value for a variable. For example, `likes_snakes = input("Do you like snakes? ")` will ask the user Do you like snakes? And whatever the user responds as will be the input value for the variable `likes_snakes`. I'm not sure if the `input()` syntax stores everything as a string or not. I'll have to check. 


Project 3 - Magic 8-Ball

We created a script that would generate random answers like a Magic 8-Ball. We first had to import the `random` package for Python in order to use the `random.randint()` command. We used this to generate a number from 1 - 9 for each of the random answers the 8-Ball would give for the user's yes or no question. I used a match case statement for all 9 answer choices. I put the script in this repo. I would like to tailor the script to actually ask the user their name and question but I don't think these projects have an IDE. They just run the script. 

Project 4 - Sal's Shipping

This one was also pretty easy. I was able to solve it pretty much by myself besides something I overlooked with the pricing. But we had a company that had 3 different shipping methods that varied in price based on the weight. So we need to create 3 different if statements to choose the shipping method and how much that method would cost based on weight. Then it should print that shipping total. So you also had to predefine a weight and a variable for the total parameter. It was pretty straightforward. You can check out my code in the repo. 


In Python, there are many different ways of classifying errors, but here are some common ones:

SyntaxError: Error caused by not following the proper structure (syntax) of the language.
NameError: Errors reported when the interpreter detects a variable that is unknown.
TypeError: Errors thrown when an operation is applied to an object of an inappropriate type.



Project 1 - Block Letters

We basically created our first and last initials using ASCII art in block letters. It was pretty straight forward. I used a triple quotation to just put in my initials with a 5 x 7 chart. I'll paste the code here for reuse later. 

Project 2 - Receipts for Lovely Loveseats

This lab was easier than the first lab lol. They gave us all the instructions but really we just set description and price values for 3 different items in a furniture shop. I personally chose to use the `+=` operator to add the number and string values up on two separate variables. We also had a sales tax which we added to the customer's total. Then we printed everything out. So nothing crazy. A copy of the code will be in my repo. 

__________________________
## 01.07.2025

**Today's Topics**

* Learning Python 3 


Two common errors that we encounter while writing Python are SyntaxError and NameError.

SyntaxError means there is something wrong with the way your program is written — punctuation that does not belong, a command where it is not expected, or a missing parenthesis can all trigger a SyntaxError.

A NameError occurs when the Python interpreter sees a word it does not recognize. Code that contains something that looks like a variable but was never defined will throw a NameError.

A way to print out a string and then the value of your variable is to do `print("Here's my variable value ->", <variable-name>`. 

Python converts all ints to floats before performing division

You represent exponents by doing two asterisks. So 2 to the 4th power or 2^4 would be `2 ** 4` in Python. 

You can also use `%` to divide in Python but it will give you the remainder of the division operation. So `38 % 6` would yield `2` because 6 goes into 36 6 times and what's left over is 2. 

I created an if-else loop for this problem. Might of been overkill but I'm not exactly sure what they were looking for. 

String concatenation - combining two strings together. Use `str(#)` to make a number a string. Just insert your number or variable that is an integer. 

You can use the `=+` operator to update a currently existing value. You can also use this to add additional string values to a variable. I could see this being useful. 

You can create multi-line strings by using the triple `'` or `"` quotation marks. So you would have a variable and on the other side of the equal sign, put """ and then press enter. Paste your multi-line variable here and press enter again. Then, ende it with """ again. When you print the variable, it will print your paragraph. 
