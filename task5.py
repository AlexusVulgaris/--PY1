from random import sample


def get_random_password() -> str:
    str_ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    list_password = sample(str_, 8)  # TODO написать функцию генерации случайных паролей
    password = ''.join(list_password)
    return password


print(get_random_password())
