def get_count_char(str_):
    dict_ = {}
    s_t_r = str_.lower()
    for i in s_t_r:
        if i in dict_ and i.isalpha():
            dict_[i] += 1
        else:
            dict_[i] = 1
    return dict_


def get_dict_perc(dct):
    summa = sum(dct.values())
    for i in dct:
        dct[i] = dct[i] / summa * 100
    return dct


# TODO посчитать количество каждой буквы в строке в аргументе str_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_dict_perc(dict_))


print(get_count_char(main_str))
