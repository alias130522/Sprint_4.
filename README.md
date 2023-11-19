# qa_python

Файл tests.py - проверки:
1  test_default_value_books_genre_empty_dictionary - Проверка значения по умолчанию на пустой словарь books_genre
2  test_default_value_favorites_empty_list - Проверка значения по умолчанию на пустой список favorites
3  test_default_value_list_genre - Проверка значения по умолчанию на список жанров genre
4  test_default_value_list_genre_age_rating - Проверка значения по умолчанию на список жанров по возрасту genre_age_rating

5  test_add_new_book_valid_number_characters - Проверяем добавление новой книги с валидным кол-вом значений
6  test_add_new_book_not_valid_number_characters - Проверяем добавление книги с НЕ валидным кол-вом значений
7  test_add_new_book_name_of_which_already_in_books_genre - Проверка добавления новой книги название которой уже есть в словаре books_genre

8  test_set_book_genre_valid_values - Проверяем установку книге жанра с валидными значениями
9  test_set_book_genre_if_name_not_in_book_genre - Проверяем добавление книги жанра, если имени книги нет в book_genre
10 test_set_book_genre_if_genre_not_in_list_genre - Проверяем добавление книги жанра, если его (название жанра) нет в списке genre

11 test_get_book_genre_true - Проверка получения жанра книги по ее имени, если она находится в списке book_genre
12 test_get_book_genre_if_name_not_book_genre - Проверка получения жанра книги по ее имени, если указанного имени НЕТ в списке book_genre

13 test_get_books_with_specific_genre_true - Проверяем получение списка книг по определённому жанру
14 test_get_books_with_specific_genre_not_list_genre - Проверяем получение списка книг по жанру, которого нет в списке genre

15 test_get_books_genre_if_dictionary_full - Проверка получения словаря books_genre, если в нём есть значения
16 test_get_books_genre_if_dictionary_empty - Проверка получения словаря books_genre, когда словарь пустой

17 test_get_books_for_children_true - Проверка возврата книг, подходящих детям

18 test_add_book_in_favorites_true - Проверка добавляем книгу в Избранное по имени
19 test_add_book_in_favorites_if_book_genre_null - Проверка добавления книги в список favorites, если её имени нет в словаре book_genre, он пустой
20 test_add_book_in_favorites_by_name_alredy_in_list_favorites - Проверка добавления книги в список favorites, если её имя уже есть в словаре book_genre

21 test_delete_book_from_favorites_true - Проверка удаления книги из списка favorites
22 test_delete_book_from_favorites_if_name_not_list_favorites - Проверка удаления книги из списка favorites, если таокй книги нет в favorites

23 test_get_list_of_favorites_books_if_list_favorites_full_true - Проверка получения списка favorites
24 test_get_list_of_favorites_books_if_list_favorites_has_values_true - Проверка получения списка favorites с внесёнными значениями