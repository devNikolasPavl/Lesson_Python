name = 'ada lovelace'

# функция изменяет первые буквы в словах нижнего регистра на верхний
print(name.title())

name = 'Ada Lovelace'

# меняет все буквы на верхний регистр
print(name.upper())
# меняет все буквы на нижний регистр
print(name.lower())

# Использование переменных в строках
first_name = 'ada'
last_name = 'lovelace'

full_name = f'{first_name} {last_name}'
print(full_name)

print(f'Hello, {full_name.title()}!')

full_name = f'{first_name.title()} {last_name.title()}'
print(full_name)
