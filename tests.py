import pytest

from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_three_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('bookname', ['Что делать, если ваш кот хочет вас убить. Сборник', ''])
    def test_add_new_book_add_incorrect_book_name_lengh(self, bookname):
        collector = BooksCollector()
        collector.add_new_book(bookname)
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_add_correct_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби','Комедии')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Комедии'

    def test_set_book_genre_add_incorrect_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби','Комедия')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == ''

    def test_get_book_genre_correct_book_name(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Комедии')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Комедии'

    @pytest.fixture(scope="session")
    def all_books(self):
        collector = BooksCollector()
        collector.add_new_book('Фантастическая книга 1')
        collector.set_book_genre('Фантастическая книга 1', 'Фантастика')
        collector.add_new_book('Фантастическая книга 2')
        collector.set_book_genre('Фантастическая книга 2', 'Фантастика')
        collector.add_new_book('Ужасная книга 1')
        collector.set_book_genre('Ужасная книга 1', 'Ужасы')
        collector.add_new_book('Ужасная книга 2')
        collector.set_book_genre('Ужасная книга 2', 'Ужасы')
        collector.add_new_book('Детективная книга 1')
        collector.set_book_genre('Детективная книга 1', 'Детективы')
        collector.add_new_book('Детективная книга 2')
        collector.set_book_genre('Детективная книга 2', 'Детективы')
        collector.add_new_book('Детская книга 1')
        collector.set_book_genre('Детская книга 1', 'Мультфильмы')
        collector.add_new_book('Детская книга 2')
        collector.set_book_genre('Детская книга 2', 'Мультфильмы')
        collector.add_new_book('Смешная книга 1')
        collector.set_book_genre('Смешная книга 1', 'Комедии')
        collector.add_new_book('Смешная книга 2')
        collector.set_book_genre('Смешная книга 2', 'Комедии')
        return collector

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_get_books_with_specific_genre_correct_genre(self, all_books, genre):
        assert all_books.get_books_with_specific_genre(genre) == list(filter(lambda n: all_books.books_genre.get(n) == genre, all_books.books_genre))

    def test_get_books_genre_get_list(self, all_books):
        assert all_books.get_books_genre() == all_books.books_genre

    def test_get_books_for_children_restricted_genre_not_included(self, all_books):
        genres = []
        for i in all_books.get_books_for_children():
            if all_books.get_book_genre(i) not in genres:
                genres.append(all_books.get_book_genre(i))
        assert 'Ужасы' not in genres and 'Детективы' not in genres

    def test_add_book_to_favorites_added_book(self, all_books):
        all_books.add_book_in_favorites('Ужасная книга 1')
        all_books.add_book_in_favorites('Фантастическая книга 2')
        all_books.add_book_in_favorites('Фантастическая книга 2')
        all_books.add_book_in_favorites('Детская книга 2')
        assert len(all_books.get_list_of_favorites_books()) == 3

    def test_delete_book_from_favorites_deleted_book(self, all_books):
        all_books.delete_book_from_favorites('Детская книга 2')
        all_books.delete_book_from_favorites('Детская книга 2')
        assert len(all_books.get_list_of_favorites_books()) == 2

    def test_get_list_of_favorites_get_list(self, all_books):
        assert all_books.get_list_of_favorites_books() == all_books.favorites






