Lists
---
In the previous lessons, we have looked at variables that contain one piece of information: a name, a number, or perhaps a favourite_snake. But what if we need to deal with multiple pieces of related data?

Say, for example, that we wanted to store the prices of 5 apples. With what we have learned so far, we may do something that looks like this:

```Python
price_of_apple_1 = 5
price_of_apple_2 = 3
price_of_apple_3 = 6
price_of_apple_4 = 7
price_of_apple_5 = 10
```

As you can tell, it gets pretty inefficient to store the prices of the apples in separate variables. What if we needed the price of 10 apples? 50? 1000? The sun would explode before you finish typing out the information manually.

In this case, it would be wise for us to use a data structure called a **list**. In a Python list, we can store multiple pieces of data of any type. We could store any combination of ints, strings, floats, etc.

```Python
my_list = []
```

To create a list, we just initialize a variable like any other, except we use square brackets to indicate that we want a list.

```Python
price_of_apples = [5, 3, 6, 7, 10]
```

To initialize the list with information, we just have different values separated by commas. 

Each value in the list is called an **element**, or an item. In this case, the prices of the apples `5, 3, 6, 7, 10` would be the **elements** of the list.

We refer to each element in the list its **index**. Each element is assigned an index starting from 0, counting up.

### price_of_apples
|Index| 0 | 1 | 2 | 3 | 4  |
|---|---|---|---|---|----|
|Element| 5 | 3 | 6 | 7 | 10 |

The 0th element of price_of_apples would be `5`, the 1st element of price_of_apples would be `3`, and so on.

To access the elements, we have to use the name of the list, followed by the index in square brackets.

```Python
print(price_of_apples[4]) #prints 10
```

We can also print out an entire list if we want.

```Python
print(price_of_apples)
```

Looping Techniques
---
We often use a for loop to access all the elements in a list. 

```Python
for i in range(0, len(price_of_apples), 1):
  print(price_of_apples[i])
```

In the example above, we used the `len()` function to get the length of the list `price_of_apples`. In this case, `len(price_of_apples)` would give us 5, which works out perfectly because the for loop iterates from 0, to the upperbound-1. The iterator `i` would represent the indices of the elements in the list, from 0 to 4.

Another way to access the elements in a list is to use a for-in loop.

```Python
for i in price_of_apples:
  print(i)
```

In this example, the iterator `i` is iterates through every element in the list. It starts from the 0th element, and goes to the (length of the list-1) element. In this case, `i` starts with the value 5, then 3, then 6, and so on.

The two examples above do the same thing, but in different ways. There will be a time and place for both methods.

List Methods
---
Speaking of methods, the Python `list` has many built-in functions that we can use. These functions are called **methods** because they belong only to the `list` class. You can tell a function apart from a method with the 'dot-notation' (i.e. there is a dot before the function).

```Python
some_list.some_method()
```

One useful method is the `append()` method, which adds an item to the **end** of the list.

```Python
some_list = [1, 2]
some_list.append(3)
print(some_list)
```

Some other useful list methods include:

| Method | Description |
| ------ | ----------- |
| `.insert(i, x)` | Inserts the item _x_ at the _ith_ index. `.insert(0, x)` would add the item _x_ to the beginning of the list, for example |
| `.remove(x)` | Removes the first element in the list that is equal to _x_ |
| `.sort()` | Sorts the items of the list |
| `.reverse()` | Reverses the items of the list |

The methods listed here, as well as many more, can be found at [this website](https://docs.python.org/3/tutorial/datastructures.html).

Exercises
---
1. Write a program that returns the highest number in a list.
2. Write a programt that returns the sum of the numbers in a list.
3. Ask the user for all the letters in his/her name. Store these letters in a list, then look up a way to `.join` the letters to print his/her name.
