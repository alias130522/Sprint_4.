import pytest

from main import BooksCollector
class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_default_value_books_genre_empty_dictionary(self):
        assert BooksCollector().books_genre == {}
    def test_default_value_favorites_empty_list(self):
        assert BooksCollector().favorites == []
    def test_default_value_list_genre(self):
        assert BooksCollector().genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
    def test_default_value_list_genre_age_rating(self):
        assert BooksCollector().genre_age_rating == ['Ужасы', 'Детективы']


    @pytest.mark.parametrize("name",["Книга с количеством символов 31", "Книга о фильме с количеством символов 40", "К"])
    def test_add_new_book_valid_number_characters(self, name, dictionary_with_names_books_and_genres):
        dictionary_with_names_books_and_genres.add_new_book(name)
        assert dictionary_with_names_books_and_genres.get_book_genre(name) == ''
    @pytest.mark.parametrize('name', ['', 'Книга о фильме е с количеством символов 41', 'Книга о фильме ее с количеством символов 42'])
    def test_add_new_book_not_valid_number_characters(self, dictionary_with_names_books_and_genres, name):
        dictionary_with_names_books_and_genres.add_new_book(name)
        assert not dictionary_with_names_books_and_genres.get_book_genre(name)
    def test_add_new_book_name_of_which_already_in_books_genre(self, dictionary_with_names_books_and_genres):
        assert dictionary_with_names_books_and_genres.add_new_book('Моана') is None


    def test_set_book_genre_valid_values(self, dictionary_with_names_books_and_genres, completed_dictionary):
        assert dictionary_with_names_books_and_genres.get_books_genre() == completed_dictionary
    def test_set_book_genre_if_name_not_in_book_genre(self, dictionary_with_names_books_and_genres):
        assert dictionary_with_names_books_and_genres.set_book_genre('Фредди', 'Ужасы') is None
    def test_set_book_genre_if_genre_not_in_list_genre(self, dictionary_with_names_books_and_genres):
        dictionary_with_names_books_and_genres.add_new_book('Чтиво')
        dictionary_with_names_books_and_genres.set_book_genre('Чтиво', 'Романтика')
        assert dictionary_with_names_books_and_genres.get_book_genre('Чтиво') != 'Романтика'



    def test_get_book_genre_true(self, dictionary_with_names_books_and_genres):
        actual_genre = dictionary_with_names_books_and_genres.get_book_genre('Моана')
        assert 'Фантастика' == actual_genre
    def test_get_book_genre_if_name_not_book_genre(self, dictionary_with_names_books_and_genres):
        assert dictionary_with_names_books_and_genres.get_book_genre('Маугли') is None



    def test_get_books_with_specific_genre_true(self, dictionary_with_names_books_and_genres):
        list_book_genre = dictionary_with_names_books_and_genres.get_books_with_specific_genre('Мультфильмы')
        assert  list_book_genre == ['Алладин']
    def test_get_books_with_specific_genre_not_list_genre(self, dictionary_with_names_books_and_genres):
        list_book_genre = dictionary_with_names_books_and_genres.get_books_with_specific_genre('Романтика')
        assert list_book_genre == []


    def test_get_books_genre_if_dictionary_full(self,dictionary_with_names_books_and_genres, completed_dictionary):
        dictionary = dictionary_with_names_books_and_genres.get_books_genre()
        assert dictionary == completed_dictionary
    def test_get_books_genre_if_dictionary_empty(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == {}


    def test_get_books_for_children_true(self, dictionary_with_names_books_and_genres):
        list_books_for_children = dictionary_with_names_books_and_genres.get_books_for_children()
        assert list_books_for_children == ['Моана', 'Алладин', 'Много шума из ничего']


    def test_add_book_in_favorites_true(self, dictionary_with_names_books_and_genres):
        dictionary_with_names_books_and_genres.add_book_in_favorites('Фредди')
        assert ['Фредди'] == dictionary_with_names_books_and_genres.get_list_of_favorites_books()
    def test_add_book_in_favorites_if_book_genre_null(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Моана')
        assert [] == collector.get_list_of_favorites_books()
    def test_add_book_in_favorites_by_name_alredy_in_list_favorites(self, dictionary_with_names_books_and_genres):
        dictionary_with_names_books_and_genres.add_book_in_favorites('Фредди')
        dictionary_with_names_books_and_genres.add_book_in_favorites('Фредди')
        assert len(dictionary_with_names_books_and_genres.get_list_of_favorites_books()) != 2


    def test_delete_book_from_favorites_true(self):
        collector = BooksCollector()
        collector.add_new_book('Фредди')
        collector.add_book_in_favorites('Фредди')
        collector.delete_book_from_favorites('Фредди')
        assert collector.get_list_of_favorites_books() == []
    def test_delete_book_from_favorites_if_name_not_list_favorites(self):
        collector = BooksCollector()
        assert collector.delete_book_from_favorites('Радость и Печаль') is None


    def test_get_list_of_favorites_books_if_list_favorites_full_true(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []
    def test_get_list_of_favorites_books_if_list_favorites_has_values_true(self):
        collector = BooksCollector()
        collector.add_new_book('Фредди')
        collector.add_book_in_favorites('Фредди')
        list_favorites = collector.get_list_of_favorites_books()
        assert list_favorites == ['Фредди']