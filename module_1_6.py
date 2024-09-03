my_dict={'Ivan': 1991, 'Dim': 1981, 'Marin':1961}
print(my_dict)
print(my_dict['Ivan'])
print(my_dict.get(2001, "Такого ключа нет"))

my_dict.update({'Mash': 1994,
                'Marv': 2020})
print(my_dict)
del my_dict ['Dim']
print(my_dict)

my_set= {'Cocktail','Book', 1,2.5,3,1,2}
print(my_set)
my_set.update({"Anton",
                   "Box"})
print(my_set.discard(2))
print(my_set)