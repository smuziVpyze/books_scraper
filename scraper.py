import requests
from bs4 import BeautifulSoup


def get_book_data(book_url: str) -> dict:
    """
    Собирает данные о книге с ее страницы
    args:
        book_url (str): ссылка на страницу книги
    returns:
        book (dict): словарь с полной информацией о книге
    """

    # НАЧАЛО РЕШЕНИЯ
    resp = requests.get(book_url)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'html.parser')

    book = {}

    book['title'] = soup.find('h1').text
    book['price'] = soup.find('p', class_='price_color').text
    book['rating'] = soup.find('p', class_='star-rating')['class'][1]
    book['available'] = soup.find('p', class_='instock availability').text.strip()

    description = soup.find('div', id='product_description', class_='sub-header')
    if description:
        book['description'] = description.find_next('p').text
    else:
        book['description'] = ''

    table_inf = soup.find('table', class_='table table-striped').find_all('tr')
    info = {}
    for row in table_inf:
        info[row.find('th').text] = row.find('td').text
    book['product_info'] = info

    return book
    # КОНЕЦ РЕШЕНИЯ


def scrape_books(is_save: bool = False) -> list:
    """
    Собирает данные о всех книгах с каталога books.toscrape.com/catalogue
    Проходит по всем страницам каталога, вытаскивает ссылки на книги и для каждой вызывает get_book_data

    Args:
        is_save (bool): если True, результат сохраняется в файл books_data.txt в текуще папке

    Returns:
        list: список словарей с данными по каждой книге
    """

    # НАЧАЛО РЕШЕНИЯ
    books = []
    page = 1

    while True:
        page_url = f'http://books.toscrape.com/catalogue/page-{page}.html'
        resp = requests.get(page_url)

        if resp.status_code != 200:
            break

        soup = BeautifulSoup(resp.content, 'html.parser')

        for article in soup.find_all('article', class_='product_pod'):
            link = article.find('h3').find('a')['href']
            book_url = 'http://books.toscrape.com/catalogue/' + link
            books.append(get_book_data(book_url))

        page += 1

    if is_save:
        with open('books_data.txt', 'w', encoding='utf-8') as file:
            for book in books:
                file.write(str(book) + '\n')

    return books
    # КОНЕЦ РЕШЕНИЯ