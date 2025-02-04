# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vF0dQawF4fbJH70mw77OOl-CEwjVplYy
"""

### Ans 1 .

players = [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]
sorted_players = sorted(players, key=lambda x: x[1], reverse=True)
print(sorted_players)

### Ans 2.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)

### Ans 3.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
string_tuple = tuple(map(lambda x: str(x), numbers))
print(string_tuple)

### Ans 4.

from functools import reduce
numbers = list(range(1, 26))
product = reduce(lambda x, y: x * y, numbers)
print(product)

### Ans 5.

numbers = [2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
divisible_by_2_and_3 = list(filter(lambda x: x % 2 == 0 and x % 3 == 0, numbers))
print(divisible_by_2_and_3)

### Ans 6.

words = ['python', 'php', 'aba', 'radar', 'level']
palindromes = list(filter(lambda x: x == x[::-1], words))
print(palindromes)

