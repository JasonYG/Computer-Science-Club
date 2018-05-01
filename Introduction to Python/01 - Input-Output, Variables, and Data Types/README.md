Input/Output
---
Many computer programs you'll run into will need to ask the user for some sort of **input**; for example, "What's your name?", "What's your favourite animal?", "How much does the earth weigh in elephants rounded to the nearest hundredth of an elephant?". Luckily in Python, there's a simple way to allow for user input in your programs.

To do this, we'll need to make use of the **input()** function, which is similar to the print function. Try running this line of code in IDLE:

```Python
input()
```

Oh no! Nothing happened? 

![Broken input() function?](https://i.gyazo.com/29ef44e70f0d851f65b77e764224acd2.png)

Actually, something did happen. The program is waiting for the user's input! It just looks like nothing happened because we don't have any other code: only an input function.

![User input](https://i.gyazo.com/ffa747fca424c680d1674a07beef54d5.png)

We can see that I actually typed something into the program, and that it executed correctly! The three 'greater than' signs, ">>>", indicate that your program ran without any issues; but it doesn't mean that it did what you want.

To make our program slightly more responsive, we can actually specify what we would like to ask the user to input.

Take a look at this piece of code:

```Python
input("What is your name?")
```
Analyzing this code bit by bit, we can see that there is still the input function, _input()_, but the function has an _argument_, that is the words written inside the brackets: _"What is your name?"_

Similarly to the **print()** function, the input function may take in a **string** as an argument, but the string doesn't always have to be there. 

This function, **input()**, is pretty much all there is to Python input. Output in Python is just the print function (it prints, or _outputs_, something to the screen).

Variables
---
In programming, you'll often run into situations where you'll have to store data to be used later - to do this, we use **variables**. Like in math class, variables represent data that can change. Let's say that we wanted to print out the user's name after they inputted it into our program. What we would do is create a variable that stores the user's name, then print it to the screen.

To create variables in Python, all we have to do is use whatever variable name we want, and assign some data to it.

The general syntax goes:

```Python
name = "Fred"
```
_name_ would be what we call our variable - this can be anything we want it to be. I could've had the variable name be _soup_ or _asjkhdaksdhkl_, or anything, but I chose to use a descriptive name that lets others reading your code know what the variable is representing. It's important to use appropriate names for your variables, so that others who read your code know what's going on.

If we wanted the variable _name_ to store what the user inputted as their name, we can do this:

```Python
name = input("What is your name?")
```
Now, whenever we refer back to the variable _name_ in our program, it will contain the data that the user inputted. To see this, we could print _name_:

```Python
name = input("What is your name?")
print(name)
```

![Printing out the user's name](https://i.gyazo.com/b81d62c2350d21b760a0de392711effe.png)

Note that I do not have quotation marks surrounding _name_, because I want the program to print out the variable _name_, not the word "name". Try running print("name") and print(name).

If we wanted to output something else along with the user's name, what we can do is use **concatenation**. This means combining two strings together to form one longer string.

For example, if I wanted to print out "Hello Fred", what I would do is add "Hello " to the variable _name_. To do this, I would use the addition operator, +, to combine the strings together.

```Python
name = input("What is your name?")
print("Hello " + name)
```

![Printing Hello Fred](https://i.gyazo.com/c0f2cd847f0b04ee6614bd5137181283.png)

Data Types
---
Variables can store many different types of data. We've covered _strings_, but there are many other types as well.

Here is a table summarizing the common types of data:

| Data Type     | Description   |
| ------------- |---------------|
| **String**    | A string is a sequence of characters, and they often represent text and words, although numbers can be strings too. For example: "Python is a huge snake that has 7 wings and 32 teeth". We can recognize strings by the single or double quotation marks. |
| **Int**eger   | An integer is a number that has no decimal places. For example: 8 is an integer, but 8.0 is not.      |
| **Float**     | A float, or floating point, is a number that **does** contain decimal places. 8.0 would be a float because it contains a decimal place, even though it's a zero.       |
| **Bool**ean   | A boolean is a data type with only 2 possible values: **True** and **False**. These can come in handy for **conditional statements**, which will be discussed in a future lesson. |

Remember that when you're dealing with data types, you can only deal with one at a time. You can add two integers together, or two strings together, but you can't add a string and an integer. There are some exceptions, however, like when you add an integer and a float together.

In Python, there are built-in functions to force data to be of a certain type. The **str()**, **int()**, **float()**, and **bool()** functions force data to be strings, integers, floating point numbers, and booleans respectively. You can run into errors when using these functions. If, for example, you forced the string "Fred" to become an integer, Python would throw an error because "Fred" clearly is not a number. 

For more examples of code, refer to sample.py.

Exercises
---
1. Ask the user for their name. Greet the person by name in the console.
2. Print the user's age in 10 years, 20 years, 20000000 years, and dog years.
3. **Challenge**: Create a quadratic formula calculator, where the user inputs the 'a', 'b', and 'c' values of the equation, and the console would print the roots. 
