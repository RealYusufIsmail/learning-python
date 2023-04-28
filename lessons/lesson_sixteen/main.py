# dictionary comprehension = creates dictionaries using expressions
# Dictionaries are used to store data values in key:value pairs and are ordered.

# dictionary= {key : expression for (key, value) in iterable}
# dictionary= {key : expression for (key, value) in iterable if conditional}
# dictionary= {key : (if/else) for (key, value) in iterable}
# dictionary= {key : function(value)  for (key, value) in iterable}

# cities_in_uk_and_temp_C = {
#    'Preston': 10,
#    'Blackburn': 9,
#    'Manchester': 5
# }

# will change to Fahrenheit using dictionary comprehension

# cities_in_uk_and_temp_F = {
#    key: round((value * 1.8) + 32) for (key, value) in cities_in_uk_and_temp_C.items()
# }

# print(cities_in_uk_and_temp_F)

# make sure to use : not commas
# weathers = {
#    'Preston': "raining",
#    'London': "snowing",
#    'BlackBurn': "raining"
# }

# Only get if they are raining
# raining_weather = {
#    key: value for (key, value) in weathers.items() if value == "raining"
# }

# print(raining_weather)

# cars = {
#    "bwm": 5,
#    "lambo": 8,
#    "tesla": 10
# }

# cars_rated = {
#    key: ("TOP_TIER" if value > 5 else "OKAY") for (key, value) in cars.items()
# }

# print(cars_rated)

cars = {
    "bwm": 5,
    "lambo": 8,
    "tesla": 10
}


def check_tier(value: int):
    return "TOP_TIER" if value > 5 else "OKAY"


cars_rated = {
    key: check_tier(value) for (key, value) in cars.items()
}

print(cars_rated)