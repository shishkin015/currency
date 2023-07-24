import json
import os
from datetime import datetime

import requests

# Присваиваем в переменную ключ переменного окружения
API_KEY = os.environ.get('VARIABLE_NAME')

# Импортируем в .json файл полученные данные
CURRENCY_RATES_FILE = 'currency_rates.json'


def main():
    while True:
        currency = input('Введите название валюты (USD или EUR): ').upper()
        if currency not in ('USD', 'EUR'):
            print('Неверный ввод. Попробуйте еще раз.')
            continue

        rate = get_currency_rate(currency)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        print(f'Курс {currency} к рублю {rate}')
        data = {'currency': currency, 'rate': rate, 'timestamp': timestamp}
        save_to_json(data)

        choice = input('Выберите действие: (1 - продолжить, 2 - выход)')
        if choice == '1':
            continue
        elif choice == '2':
            break
        else:
            print('Неверный ввод. Попробуйте еще раз.')


def get_currency_rate(base: str) -> float:
    """Получает крс от API и возвращает его в виде float"""

    url = f"https://api.apilayer.com/exchangerates_data/latest"
    response = requests.get(url, headers={'apikey': API_KEY}, params={'base': base})
    rete = response.json()['rates']['RUB']
    return rete


def save_to_json(data: dict) -> None:
    """Сохраняет данные в файл json"""

    with open(CURRENCY_RATES_FILE, 'a') as f:
        if os.stat(CURRENCY_RATES_FILE).st_size == 0:
            json.dump([data], f)
        else:
            with open(CURRENCY_RATES_FILE) as f:
                data_list = json.load(f)
                data_list.append(data)
            with open(CURRENCY_RATES_FILE, 'w') as f:
                json.dump(data_list, f)


if __name__ == "__main__":
    main()