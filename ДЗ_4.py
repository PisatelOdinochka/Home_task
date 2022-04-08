# Задача 2

""" Написать функцию currency_rates(), принимающую в качестве аргумента код валюты 
(например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю. 
Использовать библиотеку requests. В качестве API можно использовать 
http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос 
к API в обычном браузере, посмотреть содержимое ответа. Можно ли, используя только методы 
класса str, решить поставленную задачу? Функция должна возвращать результат числового типа, 
например float. Подумайте: есть ли смысл для работы с денежными величинами использовать вместо 
float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве аргумента передали 
код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того, 
в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро. """


# from requests import get, utils

# response = get('http://www.cbr.ru/scripts/XML_daily.asp')

# encodings = utils.get_encoding_from_headers(response.headers)

# content = response.content.decode(encoding=encodings)

# val = content.split('</Name>')

# valute = []

# names = ['AUD', 'AZN', 'GBP', 'AMD', 'BYN', 'BGN', 'BRL', 'HUF', 'HKD', 'DKK', 'USD', 'EUR', 'INR', 'KZT', 'CAD', 
# 'KGS', 'CNY', 'MDL', 'NOK', 'PLN', 'RON', 'XDR', 'SGD', 'TJS', 'TRY', 'TMT', 'UZS', 'UAH', 'CZK', 'SEK', 'CHF', 
# 'ZAR', 'KRW', 'JPY']


# for i in val:
#     if i.startswith('<Value>'):
#         valute.append(i[7:14])


# def currency_rates(*args):
#     valute_names = {}
#     for t in range(len(args)):
#         valute_names[args[t]] = valute[t]
#     return valute_names
# print(currency_rates(*names))

"""К сожалению, я смог сделать только так, чтобы выводился курс всех валют :(  """


# Задача 3
'''Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату, которая передаётся в ответе сервера. 
Дата должна быть в виде объекта date. Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?'''


# from requests import get, utils
# from datetime import datetime

# response = get('http://www.cbr.ru/scripts/XML_daily.asp')

# encodings = utils.get_encoding_from_headers(response.headers)

# content = response.content.decode(encoding=encodings)

# date = content.split('<ValCurs ')

# val = content.split('</Name>')

# valute = []

# valute_date = []

# names = ['AUD', 'AZN', 'GBP', 'AMD', 'BYN', 'BGN', 'BRL', 'HUF', 'HKD', 'DKK', 'USD', 'EUR', 'INR', 'KZT', 'CAD', 
# 'KGS', 'CNY', 'MDL', 'NOK', 'PLN', 'RON', 'XDR', 'SGD', 'TJS', 'TRY', 'TMT', 'UZS', 'UAH', 'CZK', 'SEK', 'CHF', 
# 'ZAR', 'KRW', 'JPY']


# for i in val:
#     if i.startswith('<Value>'):
#         valute.append(i[7:14])

# for t in date:
#     if t.startswith('Date'):
#          valute_date.append(t[6:16])
    
# valute_date = ''.join(valute_date)

# date_obj = datetime.strptime(valute_date, '%d.%m.%Y').date()


# def currency_rates(*args):
#     valute_names = {}
#     print(date_obj)
#     for arg in range(len(args)):
#         valute_names[args[arg]] = valute[arg]
#     return valute_names


# print(currency_rates(*names))


# Задача 4

"""Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания. 
Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates(). 
Убедиться, что ничего лишнего не происходит."""

import utils

print(utils.currency_rates(*names))

"""Почему-то пишет 'NameError: name 'names' is not defined' """
