# Books Scraper

## Цель
Парсер для сбора данных о книгах с сайта [Books to Scrape](http://books.toscrape.com):
название, цена, рейтинг, наличие, описание и характеристики из таблицы Product Information.

## Структура
- `scraper.py` — функции `get_book_data` и `scrape_books`
- `tests/` — тесты на pytest
- `artifacts/books_data.txt` — результат парсинга
- `notebooks/` — ноутбук с решением домашнего задания

## Запуск
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Сбор всех книг:
```python
from scraper import scrape_books
books = scrape_books(is_save=True)
```

Запуск тестов:
```bash
pytest -v
```

## Библиотеки
- requests
- beautifulsoup4
- schedule
- pytest