import pytest

from scraper import get_book_data

BOOK_URL = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'


@pytest.fixture
def book():
    """Данные о книге для всех тестов."""
    return get_book_data(BOOK_URL)


def test_book_data_is_dict_with_keys(book):
    """Проверяет, что функция возвращает словарь с нужными ключами."""
    assert type(book) == dict
    for key in ['title', 'price', 'rating', 'available',
                'description', 'product_info']:
        assert key in book


def test_book_title(book):
    """Проверяет название книги."""
    assert book['title'] == 'A Light in the Attic'


def test_book_price(book):
    """Проверяет цену книги."""
    assert book['price'] == '£51.77'


def test_book_rating(book):
    """Проверяет рейтинг книги."""
    assert book['rating'] == 'Three'