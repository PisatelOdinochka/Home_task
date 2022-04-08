from requests import get, utils
from datetime import datetime

response = get('http://www.cbr.ru/scripts/XML_daily.asp')

encodings = utils.get_encoding_from_headers(response.headers)

content = response.content.decode(encoding=encodings)

date = content.split('<ValCurs ')

val = content.split('</Name>')

valute = []

valute_date = []

names = ['AUD', 'AZN', 'GBP', 'AMD', 'BYN', 'BGN', 'BRL', 'HUF', 'HKD', 'DKK', 'USD', 'EUR', 'INR', 'KZT', 'CAD',
'KGS', 'CNY', 'MDL', 'NOK', 'PLN', 'RON', 'XDR', 'SGD', 'TJS', 'TRY', 'TMT', 'UZS', 'UAH', 'CZK', 'SEK', 'CHF',
'ZAR', 'KRW', 'JPY']


for i in val:
    if i.startswith('<Value>'):
        valute.append(i[7:14])

for t in date:
    if t.startswith('Date'):
         valute_date.append(t[6:16])

valute_date = ''.join(valute_date)

date_obj = datetime.strptime(valute_date, '%d.%m.%Y').date()


def currency_rates(*args):
    valute_names = {}
    print('Date: ' + str(date_obj))
    for arg in range(len(args)):
        valute_names[args[arg]] = valute[arg]
    return valute_names
