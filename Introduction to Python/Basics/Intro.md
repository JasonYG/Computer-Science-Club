Python Programming Language
---
We will be using the programming language Python, version 3.6.x, in our club. Python is often used to introduce programming to beginners due to it's simple syntax. Here is a list of pros and cons of learning the language:

### Pros
* Easy to learn, basic syntax (meaning that its code is intuitive. It's almost like reading English)
* Higher level language, meaning that there's less for the programmer to worry about
* Useful to beginners and professionals
	* used in many fields like data science

### Cons
* Some things inaccessible on python
* Slower than compiled languages like c++
* Less useful in fields like web development

Installing Python
---
As mentioned earlier, we will be using Python 3 in this club. We won't be using any IDE (integrated development environment) or external libraries that don't come from the official Python distribution.

Please download Python from [this](https://www.python.org/downloads/) link.

After going through the installation process, open up Python's built-in IDLE (integrated development and learning environment). Get used to this, as it'll be your new home for the duration of this club.

It should look a little something like this:

![Python IDLE](https://www.w3resource.com/w3r_images/python-shell.png)

Except, obviously, the version may be different.

This "Python Shell" is where you can type in Python code. After typing in a line of code, press enter and the shell will _interpret_ the text as Python code and spit out an output.

Try typing in regular old English into the intepreter and see what happens.

It should, if you did it right (wrong?), the Python Shell should have thrown an error: a "SyntaxError". This means that the code you typed in was incorrect, i.e. not proper Python. It's similar to having grammar mistakes in language: "Mesa likest theg cheses". Hard to understand? The same thing happens when you type in code that isn't proper Python into the interpreter. 

This is just one of the many errors you'll encounter in your Python career. Trust me there'll be a lot of them.

Starting Your First Project
---
Although useful (not really), the Python shell isn't helpful when you want to write larger-scale projects (i.e. longer than one line of code). To start a new Python project, click File > New File. 

To run your project, press 'F5' on your keyboard. Note that you'll always have to save your project before running it.

Tradionally, your first line of code as a programmer has always been "hello world". Try running this line of code:

```python
print(Hello world!)
```
Oh no! The interpreter (should) threw an error!

This is because the text, 'Hello world!', was not wrapped in quotation marks. The **'print' function** requires an input type, a **string**, to work properly. As you'll learn later on, a **string** is a _data type_ that takes in characters, or words. We'll learn more about data types in future lessons.

To fix this problem, simply surround 'Hello world' with quotation marks. Python treats single quotation marks and double quotation marks the same way. Just make sure that the open and close quotations are the same.

The proper format would be the following:

```python
print("Hello world!")
```

or

```python
print('Hello world!')
```

but not

```python
print("Hello world!')
```

Try running the above code in your Python project.

The Print Function
---
Here is a brief explanation of the Python 'print' function. Feel free to skip this section if you'd like, as we'll be talking about this stuff more in depth in later lessons.

The print magic that we used in the previous code is known as a **print function**. Functions, in all programming languages, take in some input value and spit out some output value. In this case, the print function took a **string** as its _argument_, or input value, and output the string to the Python shell.

For now, that's all we need to know. Later on, we'll be going over other **built-in functions** to Python (functions that come with the standard language) and even how to create your own functions.

Exercises
---
In every lesson, there will be an exercise section to help practice the concepts learned. Here is a list of easy exercises to try that accompass this lesson:

1. Print "I love compsci club!" to the console
2. Follow my github account (just kidding)
