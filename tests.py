from main import BooksCollector
import pytest


books_with_genres = [
    ['Паутина', 'Детективы'],
    ['Прелести культуры', 'Комедии'],
    ['Сами Боги', 'Фантастика'],
    ['Винни-Пух', 'Мультфильмы'],
    ['Темная башня', 'Ужасы'],
]

favorite_books = [
    'Мгла',
    'Война м мир'
]

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_add_repeated_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')

        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('book_name, book_genre', books_with_genres)
    def test_set_book_genre_add_genre_to_book(self, book_name, book_genre):
        collector = BooksCollector()

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)

        assert collector.get_books_genre().get(book_name) == book_genre
        
    def test_set_book_genre_add_not_exists_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Грозовой перевал')
        collector.set_book_genre('Грозовой перевал', 'Драмы')

        assert collector.get_books_genre().get('Грозовой перевал') == ''

    @pytest.mark.parametrize('book_name, book_genre', books_with_genres)
    def test_get_book_genre_return_exists_book_genre(self, book_name, book_genre):
        collector = BooksCollector()

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)

        assert collector.get_book_genre(book_name) == book_genre

    def test_get_books_with_specific_genre_two_books_with_same_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Паутина')
        collector.set_book_genre('Паутина', 'Детективы')
        collector.add_new_book('Винни-Пух')
        collector.set_book_genre('Винни-Пух', 'Мультфильмы')
        collector.add_new_book('Нежданный гость')
        collector.set_book_genre('Нежданный гость', 'Детективы')
        books_with_specific_genre = collector.get_books_with_specific_genre('Детективы')

        assert len(books_with_specific_genre) == 2 \
               and 'Нежданный гость' in books_with_specific_genre \
               and 'Паутина' in books_with_specific_genre

    def test_get_books_genre_equals_to_added(self):
        collector = BooksCollector()

        for book_name, book_genre in books_with_genres:
            collector.add_new_book(book_name)
            collector.set_book_genre(book_name, book_genre)

        books_genre = collector.get_books_genre()
        
        for book_name, book_genre in books_with_genres:
            assert book_name in books_genre and books_genre.get(book_name) == book_genre

    def test_get_books_for_children_filter_one_book(self):
        collector = BooksCollector()

        collector.add_new_book('Паутина')
        collector.set_book_genre('Паутина', 'Детективы')
        collector.add_new_book('Винни-Пух')
        collector.set_book_genre('Винни-Пух', 'Мультфильмы')
        collector.add_new_book('Темная башня')
        collector.set_book_genre('Темная башня', 'Ужасы')
        books_for_children = collector.get_books_for_children()
        
        assert len(books_for_children) == 1 and 'Винни-Пух' in books_for_children

    def test_add_book_in_favorites_add_favorite_books(self):
        collector = BooksCollector()

        for book_name in favorite_books:
            collector.add_new_book(book_name)
            collector.add_book_in_favorites(book_name)

        favorites_books_from_collection = collector.get_list_of_favorites_books()
        quantity = 0

        for book_name in favorite_books:
            if book_name in favorites_books_from_collection:
                quantity += 1

        assert quantity == len(favorite_books)

    def test_add_book_in_favorites_add_not_exists_book(self):
        collector = BooksCollector()

        collector.add_book_in_favorites("Мгла")
        favorites_books_from_collection = collector.get_list_of_favorites_books()

        assert len(favorites_books_from_collection) == 0

    def test_delete_book_from_favorites_delete_one_book(self):
        collector = BooksCollector()

        for book_name in favorite_books:
            collector.add_new_book(book_name)
            collector.add_book_in_favorites(book_name)

        book_to_delete = favorite_books[0]
        collector.delete_book_from_favorites(book_to_delete)
        favorites_books_from_collection = collector.get_list_of_favorites_books()

        assert len(favorites_books_from_collection) == len(favorite_books) - 1 \
               and book_to_delete not in favorites_books_from_collection

    def test_get_list_of_favorites_books_add_favorite_books(self):
        collector = BooksCollector()

        for book_name in favorite_books:
            collector.add_new_book(book_name)
            collector.add_book_in_favorites(book_name)

        assert collector.get_list_of_favorites_books() == favorite_books
