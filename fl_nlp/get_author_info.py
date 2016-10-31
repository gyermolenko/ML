import urllib.request
import csv
from lxml import html


def get_author_name_and_info(url):
    with urllib.request.urlopen(url) as response:
        page = response.read()

    tree = html.fromstring(page.decode('utf-8'))
    name = tree.xpath('.//h1')[0].text
    paragraphs = tree.xpath('.//table[@id="autor_info"]/tr/td/table[1]/tr/td/table[1]/tr/td/p[@class="abzac"]')
    info = '\n'.join(p.text_content() for p in paragraphs)

    return name, info


def main():
    BASE_URL = 'https://fantlab.ru/autor'
    author_ids = [
        1,    # Дэн Симмонс (Dan Simmons)
        2,    # Клайв Баркер (Clive Barker)
        3,    # Роджер Желязны (Roger Zelazny)
        13,   # Гарри Гаррисон (Harry Harrison)
        20,   # Роберт Шекли (Robert Sheckley)
        196,  # Ант Скаландис
    ]

    filename = 'authors_info.csv'
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f, delimiter='|')
        writer.writerow(('Name', 'Info'))
        for author_id in author_ids:
            url = BASE_URL + str(author_id)
            name, info = get_author_name_and_info(url)
            writer.writerow((name, info))


if __name__ == "__main__":
    main()
