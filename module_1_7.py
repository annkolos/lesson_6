immutable_var=1,'string',True
print(immutable_var)
#immutable_var[1]=2
#print(immutable_var)
#'tuple' object does not support item assignment - объект "кортеж" не поддерживает изменяемые элементы

mutable_list=[1,'string',True]
print(mutable_list)
mutable_list[2]=False
print(mutable_list)