# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint

list_dict = []
for i in range(0, 16):
    dict_ = {'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)}
    list_dict.append(dict_)

pprint(list_dict)
