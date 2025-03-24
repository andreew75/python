# Костромин Андрей Львович


import re

date_input = input("Введите дату в формате dd-mm-YYYY: ").strip()

pattern = r'^(0[1-9]|[12][0-9]|3[01])'  # День: 01-31
pattern += r'-(0[1-9]|1[0-2])'  # Месяц: 01-12
pattern += r'-(19\d{2}|20(?:[0-1]\d|2[0-5]))$'  # Год: 1900-2025

date = re.findall(pattern, date_input)
if date:
    print(date)
else:
    print("Неверный формат или значения вне диапазона")
