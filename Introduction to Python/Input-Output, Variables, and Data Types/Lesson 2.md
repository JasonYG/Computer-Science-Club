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
Analyzing this code bit by bit, 
