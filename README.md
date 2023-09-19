# qa_python

Добавлены тесты: 
test_add_new_book_add_three_books — проверка добавления книг и что одна книга не добавляется дважды
test_add_new_book_add_incorrect_book_name_lengh — проверка добавления книг с некорретными значениями длины названия
test_set_book_genre_add_correct_genre — проверка добавления корректного жанра для книги
test_set_book_genre_add_incorrect_genre — проверка добавления некорректного жанра для книги
test_get_book_genre_correct_book_name — проверка получения жанра для существующей книги
test_get_books_with_specific_genre_correct_genre — проверка получения книг по заданному жанру
test_get_books_genre_get_list — проверка получения списка книг и их жанров
test_get_books_for_children_restricted_genre_not_included — проверка, что в списке книг для детей нет книг запрещенных жанров
test_add_book_to_favorites_added_book — проверка добавления книги в избранное и что одна книга не добавляется дважды
test_delete_book_from_favorites_deleted_book — проверка удаления книги из избранного, что два раза книга не удаляется
test_get_list_of_favorites_get_list — проверка получения списка избранных книг