Dictionaries
---
When we wanted to store multiple pieces of information, we used the list, a _data collection_ type. 

In Python, there's another _data collection_ type that is slightly more complicated, but more powerful at times.

The **dictionary** allows us to assign a _key_ to a _value_. With a list, we referred to an element by its index, but with a dictionary, we refer to an element by its key.

```Python
fruit_collection = {'apple':200, 'banana':50, 'oranges':25}
print(fruit_collection['apple'])
```

In this code example, we create a dictionary `fruit_collection` with keys `'apple'`, `'banana'`, and `'orange'`, and values `200`, `50`, and `25`.

Similarly to a list, we access elements with the square bracket syntax; however, with dictionaries we refer to elements with their key, rather than their index.


```Python
fruit_lengths = {'apples': [1, 4, 10, 17, 54], 'bananas': [2, 3, 1, 5, 7], 'oranges': [5, 2, 3, 10, 9]}
print(fruit_lengths['apples'][2])
```

Dictionaries, like lists, can have many things as values. You can have a list as a value, or even a dictionary! But, the key **cannot be a list or a dictionary**. 

Looping Techniques
---
To access all the keys of a dictionary, we can use a for-in loop, like how we did with the list.

```Python
example_dict = {'apple':  2, 'banana': 3, 'triangle': 4}
for key in example_dict:
  #Prints the keys of the example_dict
  print(key)
```

In this example, the iterator `key` is set to the different keys of `example_dict`. If this is confusing, refer back to the lesson on lists.

```Python
for key in example_dict:
  print(str(key) + ' : ' + str(example_dict[key]))
```

To navigate through the values of a dictionary, we can use the iterator with the square bracket notation, as shown above.

Another method of accessing the keys and values of the dictionary is to use _two_ iterators with the `items()` method.

```Python
for key, value in example_dict.items():
  #Does the same as the code excerpt above
  print(str(key) + " : " + str(value))
```

In this case, the first iterator `key` is set to the different keys of the dictionary, and the second iterator `value` is set to the different values of the dictionary.

Dictionary Methods
---
Like lists, dictionaries have many built-in functions, or methods, to make your life easier. Here is just a few:

| Method | Description |
| ------ | ----------- |
| `.clear()` | Clears the contents of the dictionary |
| `.items()` | Returns the contents of the dictionary as a (key, value) pair |
| `.keys()` | Returns the keys of the dictionary as a list  |
| `.values()` | Returns the values of the dictionary as a list |

The methods listed here, as well as many more, can be found at [this website](https://www.tutorialspoint.com/python/python_dictionary.htm).

Exercises
---
```Python
#TODO
```
