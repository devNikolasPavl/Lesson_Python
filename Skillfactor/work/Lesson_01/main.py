import requests

def main():
    url = 'https://www.litres.ru/'

    links = []

    with open('check.txt', 'rt') as f:
        links = f.readlines()

    if len(links) == 0:
        print('Нету ссылок для проверки')

    for link in links:
        link = link.replace('\n', '')
        full_link = ''.join((url, link))

        response = requests.get(full_link)

        if response.status_code != 404:
            print(f'{full_link} - существует')

if __name__ == '__main__':
    main()