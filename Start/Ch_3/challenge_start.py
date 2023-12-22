# Example file for Advanced Python: Language Features by Joe Marini
# Programming challenge for comprehensions

import string
import pprint


test_str = "2 apples, 9 oranges?, 4 pears, Mike's 1 egg, Jane's 2 kiwis, $50!"

# print the data
str_data = {
    "Length": (len(test_str)),
    "Digits": (len([d for d in test_str if str(d).isnumeric()])),
    "Punctuation Count": (len([p for p in test_str if p in string.punctuation])),
    "Unique Letters" : (ul := "".join({c for c in test_str if c.isalpha()})),
    "Unique Count" : (len(ul))
}
pprint.pp(str_data)
