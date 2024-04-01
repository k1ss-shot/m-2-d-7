# my_list = [1, 2, 3 ,4]

# # new_list  = list(filter(lambda x: (x%2 == 0 ), my_list))

# # new_list = list(map(lambda x: x*2, my_list))

from functools import reduce

# product = reduce((lambda x,y: x*y),my_list)

# print(product)



# cities = ['MOSKOW', 'BISHKEK', 'ALMATY', 'BERLIN']

# # def make_to_lower(city_name):
# #     return city_name.lower()

# cities_lower = list(map(lambda city_name: city_name.lower(), cities))

# print(cities_lower)

# number_list = [4, 3, 6 ,8, 9]

# number_list = list(filter(lambda x: x%2 == 0, number_list))

# number_list = list(map(lambda x: pow(x,3), number_list))

# print(number_list)


# numbers = [21, 32, 2, 122, 32]

# numbers = list(filter(lambda x: x%2 != 0, numbers))
# numbers = reduce(lambda x, y: x + y, numbers)

# print(numbers)

from random import randint

# def generate_random_numbers():
#     result = []
    
#     for n in range(20):
#         number = randint(1,101)
#         result.append(number)
#     return result

# numbers = [randint(1, 101) for n in range(20)]
# print(numbers)


# numbers = list(map(lambda x: x * 2, numbers))

# print(numbers)



'''
task 6
'''

# numbers = [randint(1, 100) for n in range(20)]

# print(numbers)

# numbers = reduce(lambda x, y: x + y**2, numbers)

# print(numbers)


# strings = ['apple', 'banana', 'cherry', 'grape', 'watermelon']

# print(list(filter(lambda x: len(x) > 5, strings)))


number = [1, 2, 3, 4, 5, -2, -23, -32 , 0]

# number = reduce(lambda x, y: x * y, number)

# print(number)

# print(list(filter(lambda x: x > 0, number)))

print(list(map(lambda x: str(x), number)))
