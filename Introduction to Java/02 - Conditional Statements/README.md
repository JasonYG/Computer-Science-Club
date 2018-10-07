Conditional Statements
---
When you are creating a program, you will often run into situations where you want some code to run in certain _conditions_ but not others.

For example, let's say that we wanted to call a user old **only if** they were older than 18. In this case, we would only want to print out "You are old" if our condition, the user's age being over 18, was True.

To do this, we would use a **conditional statement**, or an _if statement_.

To better understand this concept, take a look at this flowchart:

![conditional flowchart](http://www.openbookproject.net/books/bpp4awd/_images/flowchart_if_only.png)

We only want some code to run when our condition is met.

Python If Statements
---
In Python, the general syntax for _if statements_ is as follows:

```Python
if some_condition:
  #run some code
```

In order for _some code_ to run, our condition, _some_condition_, must evaluate to True. 

Remember the boolean data type that we learned about from before? It comes back when we look at these conditions. 

In the example code above, _some_condition_ would be a boolean value that must be true for _some code_ to run.

In programming, you'll often want to compare the value of a variable to some other value. In the example we talked about before, we would want to compare the user's age to see if he or she is older than 18.

To do this in Python, we use **comparison operators**. Think back to the operators we use in math: 
* x is bigger than y; x > y
* x is bigger than or equal to y; x >= y
* x is smaller than y; x < y
* x is smaller than or equal to y; x <= y
* x is equal to y; x == y
Note that in the last case, we used TWO equal signs (==). This is because one equal signs is an **assignment** operator, used for when we assign a value to a variable (think back to the last lesson). The double equal signs is an **equality** operator, and checks if two values are equal to one another.

Take a look at this implementation of the example we talked about previously:

```Python
age = int(input("How old are you? "))
if age > 18:
  print("You are old")
```

If the user were to input a number that was greater than 18, then the program would print out "You are old". But what if we wanted it to print out "You are young" if the user was under 18? To do this, we would add an else statement:

```Python
age = int(input("How old are you? "))
if age > 18:
  print("You are old")
else:
  print("You are young")
```

To better understand how the if-else statement works, take a look at this flowchart:

![if-else flowchart](http://www.openbookproject.net/books/bpp4awd/_images/flowchart_if_else.png)

If the condition is true, if the user is over 18 years old, then we run one statement: "You are old". Otherwise, it would print out "You are young".

Elif Statements
---
Let's say that, after checking the first condition, we wanted to check a second condition. In this case, we would use an **else if** statement, or in Python, an **elif** statements. 

For example, if the user was older than 30 years old, we might want to print out "You are ancient". Let's try implementing this on top of the code we had already written. Can you see the problem in this code?

```Python
age = int(input("How old are you? "))
if age > 18:
  print("You are old")
if age > 30:
  print("You are ancient")
```

To resolve this problem, we have to use an **elif statement**. Here is a flowchart that illustrates how it works:

![elif flowchart](http://www.openbookproject.net/books/bpp4awd/_images/flowchart_chained_conditional.png)

First the program would check one condition. Then, if that condition was not met, then it would check the second condition, and so on. If that condition was met, however, every other **linked** condition (all the elif statements after) would be skipped.

Take a look at this snippet of code:

```Python
age = int(input("How old are you? "))
if age > 70:
  print("You are more than twice as old as Python")
elif age > 30:
  print("You are ancient")
elif age > 18:
  print("You are old")
else:
  print("Your skills with the computer are commendable")
```

In this example, the program would check the user's age in the order that the conditional statements are in. 

1. Is the user older than 70? If yes, then print..., otherwise;
2. Is the user older than 30? If yes, then print..., otherwise;
3. Is the user older than 18? If yes, then print..., otherwise;
4. All the other statements were false, so then print...

Exercises
---
1. Create a mini calculator program. The user would input two numbers, and whether they wish to add, subtract, multiply or divide. Print out the resulting answer.
2. Ask the user to input in a number. If their number is a perfect square, then print out "Perfect square!"! Otherwise, print out "Not a perfect square". **Hint**: Google how to square root a number in Python, or write your own implementation if you dare.
3. Allow the user to input whatever they want. If the input is a number, for example, then print out "You just typed in a number". Try to include strings (words), and booleans (True/False).

All the flowcharts were taken from [this](http://www.openbookproject.net/books/bpp4awd/ch04.html) website.
