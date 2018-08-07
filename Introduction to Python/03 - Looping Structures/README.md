Looping Structures
---
When you're programming, you'll often encounter situations where you want a section of code to run repeatedly. Rather than copy-pasting code over and over, we use _looping structures_.

While Loop
---
The _while loop_ is one way to repeat a block of code. While _some_condition_ is true, we want to run a block of code:

```Python
while some_condition:
  #run some code
```

This snippet of code outlines how we make a while loop in Python. We use the keyword `while`, followed by a condition `some_condition`, then a colon proceeded by an indented block of code. 

The while loop is not unlike an _if statement_. It follows a similar syntax, but instead, we can run some code **while** a condition is true. Python checks a condition — if it evaluates to `True`, then the indented block of code is executed. Once the last line of code in the indented block is evaluated, Python returns to the beginning of the while loop — is the condition still `True`? If so, then we run the indented block of code again. If not, then we skip everything inside the while loop. This process repeats over and over until the condition is `False`. It's possible for the condition to **never** be `False`: in which case you've created an infinite loop and you'll be stuck.

There are multiple ways to use a while loop. One of which way is to use a 'counter' variable as the condition.

```Python
counter = 0
while counter < 10:
  print(counter)
  counter += 1
```

In this example, we create a variable called 'counter', and we want everything inside the while loop to run while 'counter' is less than 10. 

The '+=' operator is used to increment counter by 1. It's the same as if we wrote `counter = counter + 1`. But that doesn't make sense! 'counter' is clearly not equal to itself plus one!

But we have to remember that the equal sign is an _assignment operator_, not an _equality operator_. If we wrote `counter == counter + 1`, then that would evaluate to `False`; however, we are **assigning** a new value to 'counter' — the value of itself plus one.

In the example above, the variable 'counter' starts at the value 0. The while loop would then check the condition. Since 'counter' is 0, which is less than 10, we run the indented block of code. We print out the value of 'counter', 0, then assign a new value to 'counter'. We would be looking at the statement `counter = counter + 1`. Python first evaluates everything on the right side of the equals sign. 'counter' + 1 is 0 + 1, which evaluates to 1. 1 is then assigned to the 'counter' variable — in essence, we've incremented counter by 1.

Note that the '+=' operator is just a quicker way to write out `counter = counter + 1`. You could do the same with '-=' (`counter = counter - 1`), '*=' (`counter = counter * 1`), and '/=' (`counter = counter / 1`).

Another way to use the while loop is with a `while True` statement. Take a look at this example:

```Python
while True:
  favourite_snake = input('What is your favourite kind of snake? ')
  if favourite_snake == 'Python':
    break
```

We are repeatedly asking the user for their `favourite_snake`. If they don't answer with 'Python', then we keep on asking them for their `favourite_snake`. 


