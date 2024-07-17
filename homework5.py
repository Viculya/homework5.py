immutable_var=1,2,3,True,'5'
print('Immutable',type(immutable_var),immutable_var)
#immutable_var[1]=5 #элементы типа tuple (кортежи) рассматриваются как неизменяемые последовательности данных. Это означает, что после создания кортежа нельзя изменить его элементы, добавить новые или удалить существующие.Данный подход был выбран разработчиками языка для обеспечения надежности программ и предотвращения неожиданных изменений данных. Кортежи, в отличие от списков, используются там, где необходимо сохранить данные в неизменяемой форме, например, в качестве ключей в словарях или элементов в множествах.
#Изменение кортежей нарушит эту надежность и может привести к ошибкам в программе. Поэтому если вам нужна структура данных, которую можно изменять, рекомендуется использовать списки вместо кортежей в Python.
mutable_list=[1,3,'6',False]
mutable_list[1]=8
print('Mutable list:',mutable_list)