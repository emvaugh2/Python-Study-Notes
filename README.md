# Python-Study-Notes


**Greetings and welcome to my public study notes for Python! It seems like a programming language is definitely needed when applying for cloud engineer roles so I'm using this space to strengthen my skills. I already have some background in MATLAB. I've completed the beginner's course in Codecademy and I'm going to be periodically working through Automate the Boring Stuff with Python. Stay tuned!**

## 02.01.2025

**Today's Topics**

* Automate the Boring Stuff with Python (Chapter 6)

Chapter 6 - Manipulating Strings

Just came across string interpolation and f-strings and this is a game changer! I never liked having to use the quotes and the `.format()` just seemed a little more tedious than it needed to be. We're definitely using f-strings from now on and I'll make sure I understand the string interpolation because I see that everywhere. Just never knew how to read it. 

>>> name = 'Al'
>>> age = 4000
>>> f'My name is {name}. Next year I will be {age + 1}.''

The above is an example of f-string format. 

`.isupper()` and `.islower()` methods return Boolean values if a value in that string is uppercase or lowercase, respectively. Just in case you ever need this. There are more than just these two as well so be on the look out for the `.is<fill_in_the_blank>` methods. 

You have the `startswith()` and `endswith()` operators as well that return Boolean values if you compare two strings. This is pretty straightforward. 

You can use the `.rjust()`, `.ljust()`, and `center()` methods on a string followed by an integer value to put that integer number of spaces (or whatever character you choose) to the right, left, and both (for center, the text will be in the middle) of the text. That's pretty cool too. 

There's an `.rstrip()` and `.lstrip()` versions of the `.strip()` command. 



## 01.31.2025

**Today's Topics**

* Automate the Boring Stuff with Python (Chapter 5)

Chapter 5 - Dictionaries and Structuring Data

Dictionaries are not ordered. You don't have an integer index. The index is the key. 

You can use the `in` and `not in` operators on dictionaries as well. 

Use the `.get(<key>, <default_value>)` to get the value of whatever key in your dictionary. If the key doesn't exist, it will create the key and give it your default value. 

Import the `pprint` (pretty print) module to display your dictionaries in a more readable format. This would've been so helpful. `pprint()` and `pformat()`. 


## 01.30.2025

**Today's Topics**

* Automate the Boring Stuff with Python (Chapter 4)

Chapter 4 - Lists

Python will give you an IndexError error message if you use an index that exceeds the number of values in your list value.

Remember the `in` and `not in` operators for lists. You can do `<item> in [<list-or-list-name]` and Python will return True or False. 

Another way to write a for loop with the index and range() function is to use the `enumerate()` function. For example,

`supplies = ['pens', 'staplers', 'flamethrowers', 'binders']`

`for index, item in enumerate(supplies):`
    `print('Index ' + str(index) + ' in supplies is: ' + item)`

You know the syntax `var += 1`? Well there are other operator versions of that as well. You know the `var -= 1` option already but there is a multiplication, division, and remainder version to. Just in case you need it. 

To sort a list in the reverse way, use `<list_name>.sort(reverse=True)`. 

There's also a `.reverse()` list method that reverses the items in a list. This is not the same thing as sort but I guess you can sort the list and then reverse it too. 

These list methods act on lists "in place". They don't return a value. They just modify the list. So don't try to assign these method syntax commands to another variable. They'll just act on the list and you can recall that list. 

Remember, tuples are immutable just like strings. You cant modify them after you've created them unlike a list. 

" If you need an ordered sequence of values that never changes, use a tuple. A second benefit of using tuples instead of lists is that, because they are immutable and their contents don’t change, Python can implement some optimizations that make code using tuples slightly faster than code using lists."

You can also use the `list()` and `tuple()` commands to convert a value into a list or a tuple.


## 01.29.2025

**Today's Topics**

* Automate the Boring Stuff with Python (Chapter 3)

Chapter 3 - Functions

The value `None` represents the absence of a value. This is the same thing as null or undefined. None if the return value of the function `print()`. `print()` displays text on the screen but technically it doesn't return a value. Be mindful of this. So `print()` will display your text and then after that, it will (invisibly) return None unless you run a script. Then you may see this. 

`print()` automatically passes the newline character to your string. That's why your next output will be on the next line. `print()` actually has two optional arguments named `end` and `sep` where you can actually tell the print function NOT to add the newline character into it. It would look like `print('Hello', end='')`. 

You can pass multiple strings to `print()` as well. You can do `print('cats', 'dogs', 'mice')` and it will display `cats dogs mice`. Notice how it's spaced out? You can use the the `sep` argument that we mentioned earlier to separate these strings by whatever delimiter you want. For example, `print('cats', 'dogs', 'mice', sep=',')` would evaluate to `cats,dogs,mice`. 

Parameters and variables that are assigned in a called function are said to exist in that function’s local scope. Variables that are assigned outside all functions are said to exist in the global scope. Think of this in terms of class and instance variables. You would define a global variable in like, the beginning of your script/program. You would define a local variable within your function. The function doesn't remember any of them.

To make a variable global within a function, use the `global <variable_name>` syntax. 

You can handle errors (that red ouput on the screen when you mess up) using the `try` and `except` clauses. The code that could potentially have an error is put in an `try` clause. The program execution moves to the start of a following `except` clause if an error happens. Review the below code:

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

Wow that is so cool!!!

## 01.28.2025

**Today's Topics**

* Automate the Boring Stuff with Python (Chapter 2)

Chapter 2 - Flow Control

Remember, <, >, <=, and >= evaluate down to Boolean values. 

if statements only executes it's clause (clause = block of indented code) if the statement is True. Otherwise, it will skip the clause if the condition is False. 

"When there is a chain of elif statements, only one or none of the clauses will be executed. Once one of the statements’ conditions is found to be True, the rest of the elif clauses are automatically skipped."

`break` statements will exit out of a while loop no matter what part of the clause (block) it's located in. Use this as a way to exit infinite loops. 

When the program reaches a continue statement, the program execution jumps straight back to the beginning of the start of the loop and reevaluates the loop's condition. Think about it like when a loop reaches the end of the loop and starts back at the beginning. The `continue` statement would be the equivalent of reaching the end of a loop. 

You can make a program terminate before it reaches the end of the script. You need to import the `sys` module first and use the `sys.exit()` function. 



## 01.27.2025

**Today's Topics**

* Automate the Boring Stuff with Python (Chapter 1 - 2)

Alright! Last segment of Python before I'm done learning the basics of coding. We're moving onto projects after this. Lets get started. 

Chapter 1 - Python Basics

This is exactly what it says. Everything here was very straight forward. No need to say anything else.

Chapter 2 - Flow Control



## 01.26.2025

**Today's Topics**

* Learning Python 3 (Classes)

Alright now for the last part. We can use functions within the class to define our own methods for the class. So just make your function and give it a name. This will be the method that you use to call your function. Think of an attribute (data) as like a stationary value and think of a method as an action. Usually you'll pass an additional argument to the method but you call on the method the same way you call on the attribute. I'm too tired to show you how to do that right now though. 

Last but not least (maybe least), you can use the `hasattr()` and `getattr()` functions outside of your class to see if an object has that particular attribute or to get the value of that attribute, respectively. Please look at the syntax for this. I don't remember what is was. 


## 01.25.2025

**Today's Topics**

* Learning Python 3 (Classes)

Okay lets go over to instance variables. So instance variables are specific to that particular object. Say we have the attributes health, speed, and defense as instance attributes. We may to define that at the beginning when we're creating our object. Before we get into instance variables, lets talk about the constructor "function" or "method" called the `__init__` function. We can use this as a way to construct all of our objects so they have all the same parameters (such as health, speed, and defense even if they are different values. You will always pass the argument `self` to this function but you can add additional parameters afterwards. It would look something like `def __init___(self, health, speed, offense)` and then you would refer to each parameters below as `self.health = health`, `self.speed = speed`, and `self.defense = defense`. It's weird, I know. But that's just the syntax and that's how you have to refer to each variable in the rest of the class. 

## 01.24.2025

**Today's Topics**

* Learning Python 3 (Classes)

Back to classes. So previously, I said we need to create an instance of a class. This is like in containers where you create the image and build that from scratch. Then you actually have to create an instance of the container image that you create that will run. This is the same thing as an object. The object is that particular instance of the class that you create. 

Now why is this important? This is important because each object can have different properties depending on what you assign it. Now didn't we create the classes so each instance we create can be similar? Yes we did. But think of the class as a character design and each object as a different character in a Tekken game. We want each character to have arms, legs and do combos but each character will do their combos differently. The kicks and punches can be the equivalent of what we call an object's attribute or data. 

Now, we have class variables and instance variables. Class variables (usually defined outside of the methods or constructor) will be present for each object that we create. It will be the same (unless we change it). For example, we can have the class variable `Game = "Tekken Character"` as the class variable for each object that we create. So say we have a class called Tekken (`class Tekken():`) and then we give it the above class variable `Game = "Tekken Character"`. Say we have an object called Jin so it would be `Jin = Tekken()`. If we called on the attribute using `Jin.Game`, it should return `"Tekken Character"`. 


## 01.23.2025

**Today's Topics**

* Learning Python 3 (Classes)

So after talking to Chat GPT and going back over the Classes section of the coding course, I think I have a better understanding of what classes do. So classes are basically like you constructing your own libraries or modules. Packages. Whatever you want to call it. So such as `datetime` and `random` are libaries of code with their on object types and built-in methods, so are classes that you define. 

So a class is simply a schematic or bliueprint or diagram for whatever type of object you want to create. You can call these objects whatever you want to but they will belong to the same class. So just like a `zip()` object is a zip object, so will whatever class you create. 

Why do we need classes? Well it helps making multiple of a certain type of object or blueprint easy to replicate. You may want to treat that particular object differently then you treat the other code that you're writing. Each chunk of code can be written differently and behave the way you want it to behave. So with classes, you can define it using `class <Class-Name>:` which will create the class that you want. This is the beginning of everything. Now that you've done that, you actually have to create an instance of the class. I'll cover that in the next day's topic. 

## 01.22.2025

**Today's Topics**

* Learning Python 3 (Classes)

`__init__()` is a double underscore method. It's used to initialize a new created object. It's called every time the class is instantiated. 

Methods that are used to prepare an object being instantiated are called constructors. 


## 01.21.2025

**Today's Topics**

* Learning Python 3 (Classes)

Last chapter! Lets do it. 

You can determine an object's type by using the `type()` command. Really you should do `print(type(<insert_variable>))`. 

You can define your own class type. A class is a template for a data type. It describes the kinds of information that class will hold and how a programmer will interact with that data. 

A class must be instantiated after it has been defined. You have to create an instance of the class. Instantiating a class looks a lot like calling a function. 

A class instance is also called an object. The pattern of defining classes and creating objects to represent the responsibilities of a program is known as Object Oriented Programming (OOP). When you use the `type()` syntax on a class object, you'll get the output `__main__.<class-name>` and the `__main__` part means "this current file that we're running". So basically "within this script". 

When we want the same data to be available to every instance of a class, we use a class variable. We define this in the indented part of the class definition. THESE ARE NOT THE SAME but think of it like a tag. A group tag. Each object will have this tag. In the example, they denoted the class variable (or tag) of `title = "Rockstar"`. Say we have a class named `class Musician:` and it has that title in the indented space. If we do `drummer = Musician()`, the drummer will be a part of the class object of Musician AND if you do print(drummer.title), guess what the result will be? It will be "Rockstar". So this isn't a tag but for now, think of it like one. Think of it as an attribute!

OOOOOOHHHH I think this is clicking. So now we're going over methods. Remeber methods were just extensions of commands we already knew? And packages we imported that had additional methods? I think defining a class is the same thing as like, creating your own library in a since. And with that being said, we've already went over different types of objects like zip objects, random objects, stuff like that? I think that's what they mean by Object Oriented Programming. You can create your own objects that behave the way you want them to behave and your own libraries. 

So we're creating a method inside of our class. We're basically defining the method the same way we define a function. The first argument of this method function will always be `self`. Say you have a class named Dog and it has a method called time_explanation (think of this like a custom function inside the class). If you assign a variable to this class `pipi_pitbull = Dog()` and you want to use that method (in our case, this method is just an explanation but it could be a computing function or something more useful), you would say `pipi_pitbull.time_explanation()` and it will deliver that information. 

It's weird having to create an instance of an object and then using that instance to call upon the object and it's methods. I guess this is the thing as importing a library and using an alias for the library. Trying to wrap my head around it. 

And we've finally made it to constructors and the `__init__()` method. I'm going to pause it here because my brain is fried from doing so much work at work today. Plus, I truly want to know how this works because this was a part of the HTTP method when doing the Cloud Resume Challenge. 



## 01.20.2025

**Today's Topics**

* Learning Python 3 (Files)

Project - Hacking the Fender

Okay I had to completely rely on the syntax from these lessons in order to make it through this project. I didn't take the best notes so I forgot how to iterate through these dictionary objects. I'm actually not even too strong on dictionaries to begin with, let alone manipulating files like dictionaries. Also, the instructions were not very explicitly stated so I had to really make sure I ran the code correctly myself which is 1 thing I don't like about Codecademy. I think they need to have an IDE or whatever so we can just run parts of our code just to see what they do. Just because I don't get an output error doesn't mean I'm getting the output I wanted. Anyway, the project was pretty much taking a compromised password file, exporting that information into another file, writing a message in JSON, and then replacing the corrupted file with the signature of another hacker to throw off the original hacker. We did all of this through file manipulation. For more code, please check out the `HackingTheFender.py` file in this repo. 




## 01.19.2025

**Today's Topics**

* Learning Python 3 (Files)

You can think of each file as an individual container of related information. A `.py` file is also a file. 

There are some methods for modifying files. You have `.readlines()`, `.readline()`, `.write()`, etc. 

We'll go over syntax later but Python has a build in context manager that lets Python know when to open and close files. Without it, we would have to manually close the file after our block indent section. That's why our `with open()` syntax looks like a loop or something. This is the context manager at work. 

CSV files are just plain text files. Remember, CSV stands for command separated values. 

Now, if we just did the `.read()` method on a CSV file, it will get all the values of the CSV file but the output would just be one long string (remember that store project we did? lets never have our output as just one string). So we can use the `.DictReader()` method to put our CSV values into a dictionary. You also have to first import your csv library using `import csv`. 

This also applies to JSON files. Thank God. 




## 01.18.2025

**Today's Topics**

* Learning Python 3 (Dictionaries)


Dictionary - unordered set of key:value pairs (sounds like a database). Uses the `{}` brackets. The format is `menu = {"avocado toast": 6, "insert_key": insert_value]`. 

The keys can also be numbers. The value can be any type. Even a list. Do not make a list or a dictionary the key. It doesn't work. You'll get a TypeError. You can make the value a list or dictionary though. 

You can create empty dictionaries just like lists. 

You can add a key:value pair to a dictionary after it was created. The syntax is `dictionary_name[key] = value`. 

If you want to add multiple values at once, you can use `dictionary_name.update({insert_all_key_value_pairs})` and the syntax is literally like you creating a new dictionary. So add them in there as the key:value pairs in a normal dictionary. 

You can overwite values as well. Just do the add a key:value pair syntax and put the new value that you want for that particular key. 

Okay so apparently that `zip()` function and the zip object can come into handy here. We have dict comprehensions (pause) just like we have list comprehensions. Remember with `zip()`, it can combine two lists together and pair them how we want. You can use this function with the dict comprehension to make a dictionary. First, make your two lists and use the zip function to pair them together. Give that zip object a variable name. Then the syntax id `dictionary_name = {key:value for key, value in zip_variable_name}`. That's the exact syntax. The only thing you're declaring is the dictionary name and the zip object variable. That key:value stuff doesn't change. 

Dictionaries have a built in method to allow you to search the dictionary for a key. Use the syntax `dictionary_name.get("key_name")`. I guess you can also declare what value you want a key to return if the key doesn't exist. The syntax is `dictionary_name.get("key_name", "value_value")`. 

You can use this same exact syntax to remove a value from the dictionary but instead of `.get()`, you would use `.pop()` which you're already familiar with. 

Hmm so apparently when you do the `.get()` and `.pop()` methods, it will return the value of the key and then either keep it or delete it, respectively. So it will call it first and then take the necessary action. 

You can use the `.list()` and `.keys()` to return values from a dictionary into a list. I think this acts on the keys only though. The `.keys()` method returns a dict_keys object so be aware. You cant modify this. 

Now to the values. There is a method for this as well called `.values()`. This also returns a dict_values object. Be aware. 

So you can use an if loop to iterate through the dict object (whether that's keys or values) in order to add that to a variable or a list. Or another dictionary. So just keep that in mind if you want to extract the values out of a dictionary. 

You can use the `.items()` method to get both the key and the value. The syntax for the loop for this is `for <arbitrary_key_name>, <arbitrary_value_name> in <dictionary_name>.items():` and then iterate through all of them. 


Project - Scrabble

This project was pretty straight forward. Just making sure we can zip lists together, create a dictionary out of them, and be able to call on the values by using the keys. We also made some loops to iterate through the dictionary as well. Very useful. Check out my code in the `Scrabble.py` file. 


## 01.17.2025

**Today's Topics**

* Learning Python 3 (Modules)


Project - Time Traveler's Toolkit

Okay guess we're finishing this today. Had a rough week. 

Okay so I didn't really like this lab because it wasn't very clear what they were asking for. The instructions were just vague. But we had to make a Python module with a function in it and then import that module (and function) with a few other modules to make a time traveler's message. It was smooth enough until the end I had to call the function from a different script and it was saying the function wasn't defined. I'm like I definitely defined it and imported the module. Apparently, you have to put the module name with a period before the function name in order to call it specifically. Or, you can call the specific function in the module at the beginning of your script in order for your file to know exactly where the function is. Just learned something new. You can check my code in the `Custom_Module.py` script and the `TimeTravelersToolkit.py` script. 

## 01.16.2025

**Today's Topics**

* Learning Python 3 (Modules)

Python allows us to package code into files called modules. They're often called libraries or packages. A package is really a directory that holds a collection of modules. 

To use a module in a file, it usually follows the syntax: `from module_name import object_name`.

A namespace isolates the functions, classes, and variables defined in the module from the code in the file doing the importing. Your local namespace, meanwhile, is where your code is run.

You can give your module an aliase if you want to change the name of it for your own convenience. For example, `import module_name as name_you_pick_for_the_module`.

You can import you own functions in your own librarys. Lets say you have a script called `library.py` and you have a function in it called `def duel_masters(cards)`. Say you open up another Python script and you want to use that function. At the top of your new script, you can do `from library import duel_masters` and then you can use that function in your new script. 


Project - Time Traveler's Toolkit

I'll finish this tomorrow


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
