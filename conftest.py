import pytest

from main import BooksCollector

@pytest.fixture
def dictionary_with_names_books_and_genres():
    dictionary = BooksCollector()
    dictionary.add_new_book('Моана')
    dictionary.set_book_genre('Моана', 'Фантастика')
    dictionary.add_new_book('Фредди')
    dictionary.set_book_genre('Фредди', 'Ужасы')
    dictionary.add_new_book('Пуаро')
    dictionary.set_book_genre('Пуаро', 'Детективы')
    dictionary.add_new_book('Алладин')
    dictionary.set_book_genre('Алладин', 'Мультфильмы')
    dictionary.add_new_book('Много шума из ничего')
    dictionary.set_book_genre('Много шума из ничего', 'Комедии')
    return dictionary

@pytest.fixture
def completed_dictionary():
    completed_dictionary = {'Моана': 'Фантастика',
                            'Фредди': 'Ужасы',
                            'Пуаро': 'Детективы',
                            'Алладин':'Мультфильмы',
                            'Много шума из ничего': 'Комедии'}
    return completed_dictionary