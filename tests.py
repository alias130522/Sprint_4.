import pytest

from main import BooksCollector
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_default_value_books_genre_empty_dictionary(self):  # Проверка значения по умолчанию на пустой словарь books_genre
        assert BooksCollector().books_genre == {}
    def test_default_value_favorites_empty_list(self):  # Проверка значения по умолчанию на пустой список favorites
        assert BooksCollector().favorites == []
    def test_default_value_list_genre(self):  # Проверка значения по умолчанию на список жанров genre
        assert BooksCollector().genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
    def test_default_value_list_genre_age_rating(self):  # Проверка значения по умолчанию на список жанров по возрасту genre_age_rating
        assert BooksCollector().genre_age_rating == ['Ужасы', 'Детективы']


    @pytest.mark.parametrize("name",["Книга с количеством символов 31", "Книга о фильме с количеством символов 40", "К"])
    def test_add_new_book_valid_number_characters(self, name):  # Проверяем добавление новой книги с валидным кол-вом значений
        collector = BooksCollector()
        collector.add_new_book(name)
        assert  collector.books_genre[name] == ''
    @pytest.mark.parametrize('name', ['', 'Книга о фильме е с количеством символов 41', 'Книга о фильме ее с количеством символов 42'])
    def test_add_new_book_not_valid_number_characters(self, name):  # Проверяем добавление книги с НЕ валидным кол-вом значений
        collector = BooksCollector()
        collector.add_new_book(name)
        assert not collector.books_genre.get(name)
    def test_add_new_book_name_of_which_already_in_books_genre(self, ):  # Проверка добавления новой книги название которой уже есть в словаре books_genre
        collector = BooksCollector()
        collector.add_new_book('Радость и печаль')
        collector.set_book_genre('Радость и печаль', 'Ужасы')
        assert not collector.add_new_book('Радость и печаль')



    def test_set_book_genre_valid_values(self):  # Проверяем установку книге жанра с валидными значениями
        collector = BooksCollector()
        collector.add_new_book('Фредди')
        collector.set_book_genre('Фредди', 'Ужасы')
        assert collector.books_genre['Фредди'] == 'Ужасы'
    def test_set_book_genre_if_name_not_in_book_genre(self):  # Проверяем добавление книги жанра, если имени книги нет в book_genre
        collector = BooksCollector()
        assert collector.set_book_genre('Фредди', 'Ужасы') == None # Либо останется collector.book_genre == {}
    def test_set_book_genre_if_genre_not_in_list_genre(self):  # Проверяем добавление книги жанра, если его (название жанра) нет в списке genre
        collector = BooksCollector()
        collector.add_new_book('Чтиво')
        collector.set_book_genre('Чтиво', 'Романтика')
        assert collector.books_genre['Чтиво'] != 'Романтика'
        print(collector.books_genre)



    @pytest.mark.parametrize('name, genre',[('Убийство на рассвете', 'Детективы'), ('Моана', 'Мультфильмы'), ('Побег', 'Комедии')])
    def test_get_book_genre_true(self, name, genre):  # Проверка получения жанра книги по ее имени, если она находится в списке book_genre
        collector = BooksCollector()
        collector.add_new_book('Моана')
        collector.set_book_genre('Моана', 'Мультфильмы')
        actual_genre = collector.get_book_genre('Моана')
        assert 'Мультфильмы' == actual_genre
        print(collector.books_genre)
    @pytest.mark.parametrize('name, genre',[('Убийство на рассвете', 'Детективы'), ('Моана', 'Мультфильмы'), ('Побег', 'Комедии')])
    def test_get_book_genre_if_name_not_book_genre(self, name,genre):  # Проверка получения жанра книги по ее имени, если указанного имени НЕТ в списке book_genre
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre('Маугли') == None
        print(collector.books_genre)


    def test_get_books_with_specific_genre_true(self):  # Проверяем получение списка книг по определённому жанру
        collector = BooksCollector()
        collector.add_new_book('Моана')
        collector.set_book_genre('Моана', 'Мультфильмы')
        list_book_genre = collector.get_books_with_specific_genre('Мультфильмы')
        assert  list_book_genre == ['Моана']
    @pytest.mark.parametrize('name, genre',[('Убийство на рассвете', 'Детективы'), ('Моана', 'Мультфильмы'), ('Побег', 'Комедии')])
    def test_get_books_with_specific_genre_not_list_genre(self, name, genre):  # Проверяем получение списка книг по жанру, которого нет в списке genre
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        list_book_genre = collector.get_books_with_specific_genre('Романтика')
        assert  list_book_genre == []


    def test_get_books_genre_if_dictionary_full(self):  # Проверка получения словаря books_genre, если в нём есть значения
        collector = BooksCollector()
        collector.add_new_book('Моана')
        collector.set_book_genre('Моана', 'Мультфильмы')
        dictionary = collector.get_books_genre()
        assert dictionary == {'Моана': 'Мультфильмы'}
    def test_get_books_genre_if_dictionary_empty(self): #Проверка получения словаря books_genre, когда словарь пустой
        collector = BooksCollector()
        assert collector.get_books_genre() == {}


    def test_get_books_for_children_true(self): # Проверка возврата книг, подходящих детям
        collector = BooksCollector()
        collector.add_new_book('Моана')
        collector.set_book_genre('Моана', 'Мультфильмы')
        list_books_for_children = collector.get_books_for_children()
        assert list_books_for_children == ['Моана']


    def test_add_book_in_favorites_true(self):  # Проверка добавляем книгу в Избранное по имени
        collector = BooksCollector()
        collector.add_new_book('Фредди')
        collector.add_book_in_favorites('Фредди')
        assert ['Фредди'] == collector.favorites
    def test_add_book_in_favorites_(self):  # Проверка добавления книги в список favorites, если её имени нет в словаре book_genre, он пустой
        collector = BooksCollector()
        collector.add_book_in_favorites('Моана')
        assert [] == collector.favorites
    def test_add_book_in_favorites_by_name_alredy_in_list_favorites(self):  # Проверка добавления книги в список favorites, если её имя уже есть в словаре book_genre
        collector = BooksCollector()
        collector.add_new_book('Фредди')
        collector.add_book_in_favorites('Фредди')
        collector.add_book_in_favorites('Фредди')
        assert len(collector.favorites) != 2


    def test_delete_book_from_favorites_true(self): # Проверка удаления книги из списка favorites
        collector = BooksCollector()
        collector.add_new_book('Фредди')
        collector.add_book_in_favorites('Фредди')
        collector.delete_book_from_favorites('Фредди')
        assert collector.favorites == []
    def test_delete_book_from_favorites_if_name_not_list_favorites(self): # Проверка удаления книги из списка favorites, если таокй книги нет в favorites
        collector = BooksCollector()
        assert collector.delete_book_from_favorites('Радость и Печаль') == None


    def test_get_list_of_favorites_books_if_list_favorites_full_true(self): # Проверка получения списка favorites
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []
    def test_get_list_of_favorites_books_if_list_favorites_has_values_true(self): # Проверка получения списка favorites с внесёнными значениями
        collector = BooksCollector()
        collector.add_new_book('Фредди')
        collector.add_book_in_favorites('Фредди')
        list_favorites = collector.get_list_of_favorites_books()
        assert list_favorites == ['Фредди']