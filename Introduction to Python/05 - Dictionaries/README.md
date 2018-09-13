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


