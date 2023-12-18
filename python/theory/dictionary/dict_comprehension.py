# Dictionary Comprehension
# allows to create a nw dictionry from the values in a list,
# or in a dictionary, or any other iterable

import random
# Create a dictionary based on values of existing list
# Syntax: new_dict = {new_key:new_value f0r item in list}
city_names = ['Paris', 'London', 'Rome', 'Berlin', 'Madrid']
city_temps = {city:random.randint(20,30) for city in city_names}
print(city_temps)

# Create a dictionary based on the values from existing dictionary
# Syntax: new_dict = {new_key:new_value for (key,value) in dict.items()}
new_dict = {city:temp for (city,temp) in city_temps.items()}
print(new_dict)

# use if condition
# Syntax: new_dict = {new_key:new_value for (key,value) in dict.items() if condition}
above_25 = {city:temp for (city,temp) in city_temps.items() if temp > 25}
print(above_25)