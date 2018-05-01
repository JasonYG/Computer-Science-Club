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

In programming, you'll often want to compare the value of a variable to a number or letter.
