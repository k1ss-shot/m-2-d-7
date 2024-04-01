# my_list = [1, 2, 3 ,4]

# # new_list  = list(filter(lambda x: (x%2 == 0 ), my_list))

# # new_list = list(map(lambda x: x*2, my_list))

# from functools import reduce

# product = reduce((lambda x,y: x*y),my_list)

# print(product)



cities = ['MOSKOW', 'BISHKEK', 'ALMATY', 'BERLIN']

# def make_to_lower(city_name):
#     return city_name.lower()

cities_lower = list(map(lambda city_name: city_name.lower(), cities))

print(cities_lower)