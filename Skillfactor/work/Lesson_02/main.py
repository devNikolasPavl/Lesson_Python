import requests

# главная функция с основным кодом программы
def main():
    url = input('URL для поиска:\t')        # здесь записываете url сайта, на котором будете искать директории

    links = []

    # загружаем все ссылки из файла
    with open('checks.txt', 'rt') as f:
        links = f.readlines()

    # если ссылок нет, то мы завершаем работу программы
    if len(links) == 0:
        print('Нет ссылок для проверки')
        return

    for link in links:
        # убираем знак переноса строки в конце каждой ссылки
        link = link.replace('\n', '')
        full_link = ''.join((url, link))    # формируем полную ссылку, по которой будут отправлять запросы

        response = requests.get(full_link)
        # получаем ответ от запроса, скорость запроса будет зависить от скорости вашего интернета

        if response.status_code != 404:
            print(f'{full_link} - существует')  # выводим ссылки, которые нам удалось найти

if __name__ == '__main__':
    main()