from datetime import datetime
import requests
import json
import os

VARIABLE_NAME = os.environ.get('VARIABLE_NAME')

def main():
    while True:
        currency = input('Введите название валюты (USD или EUR): ').upper()
        if currency not in ('USD', 'EUR'):
            print('Неверный ввод. Попробуйте еще раз.')
            continue

        rate = get_currency_rate(currency)
        timestamp = datetime.now()

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


def get_currency_rate(base: str) -> None:
    """Получает крс от API и возвращает его в виде float"""
    url = f"https://api.apilayer.com/exchangerates_data/latest"

    response = requests.get(url, headers={'apikey': VARIABLE_NAME}, params={'base': base})
    print(response.json())


def save_to_json(data):
    pass

if __name__ == "__main__":
    get_currency_rate('USD')

    # main()