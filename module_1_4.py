#Организуйте_программу
from os import replace

my_string= input("В каком городе вы живете? ")

#Работа_с_методами_строк
print(("В каком городе вы живете?".replace("живете", "")).upper())
print(("В каком городе вы живете?".replace("каком", "")).lower())
print("В каком городе вы живете?".replace(" ", ""))
print(my_string[0])
print(str(my_string[-1]))


