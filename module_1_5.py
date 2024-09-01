
immutable_var=1,2,3,3.5,"Start"
print(immutable_var)
#immutable_var[0]=300  не поддерживает обращение по элементам

mutable_list=[1,2,3,3.5,"Start"]
print(mutable_list[-1])
mutable_list[-1]= "Stop"
print(mutable_list)