def all_students(students):
    students_by_subject = {}

    for student in students:
        subject = student["subject"]

        if subject not in students_by_subject:
            students_by_subject[subject] = {
                "students_count": 0,
                "all_grades_count": 0,
                "grade_sum": 0
            }

        students_by_subject[subject]['students_count'] += 1
        students_by_subject[subject]["all_grades_count"] += len(student["grades"])

        for grade in student["grades"]:
            students_by_subject[subject]['grade_sum'] += grade

    for subject in students_by_subject:
        grade_sum = students_by_subject[subject]["grade_sum"]
        all_grades_count = students_by_subject[subject]["all_grades_count"]
        students_by_subject[subject]["avg_grade"] = round(grade_sum / all_grades_count, 2)

    return students_by_subject


if __name__ == "__main__":
    students = [
        {"name": "Иван", "subject": "Математика", "grades": [5, 4, 5]},
        {"name": "Петр", "subject": "Математика", "grades": [3, 4]},
        {"name": "Анна", "subject": "Физика", "grades": [5, 5, 5]}
    ]
    print(all_students(students))
    # from datetime import datetime
    #
    # def all_movies(movies):
    #     movies_by_genre = {}  # ← словарь для группировки
    #
    #     # ШАГ 1: Группируем данные по жанрам
    #     for movie in movies:  # ← для каждого фильма
    #         genre = movie["genre"]  # ← получаем жанр
    #
    #         # Если жанра ещё нет — создаём запись
    #         if genre not in movies_by_genre:
    #             movies_by_genre[genre] = {
    #                 "movies_count": 0,  # количество фильмов
    #                 "total_reviews": 0,  # количество отзывов
    #                 "score_sum": 0  # сумма всех оценок
    #             }
    #
    #         # Обновляем счётчики для этого жанра
    #         movies_by_genre[genre]["movies_count"] += 1  # ← добавляем фильм
    #         movies_by_genre[genre]["total_reviews"] += len(movie["reviews"])  # ← добавляем отзывы
    #
    #         # Проходим по всем отзывам фильма
    #         for review in movie["reviews"]:  # ← для каждого отзыва
    #             movies_by_genre[genre]["score_sum"] += review["score"]  # ← прибавляем оценку
    #
    #     # ШАГ 2: Считаем средние оценки
    #     for genre in movies_by_genre:  # ← для каждого жанра
    #         total_reviews = movies_by_genre[genre]["total_reviews"]
    #         score_sum = movies_by_genre[genre]["score_sum"]
    #         movies_by_genre[genre]["avg_score"] = round(score_sum / total_reviews, 1)
    #
    #     # ШАГ 3: Возвращаем результат
    #     return movies_by_genre
    #
    #
    # # Тестирование
    # if __name__ == "__main__":
    #     movies = [
    #         {"title": "Дюна", "genre": "Фантастика",
    #          "reviews": [{"user": "Аня", "score": 9}, {"user": "Боря", "score": 7}]},
    #         {"title": "Интерстеллар", "genre": "Фантастика", "reviews": [{"user": "Вика", "score": 10}]},
    #         {"title": "Зеленая миля", "genre": "Драма",
    #          "reviews": [{"user": "Аня", "score": 10}, {"user": "Боря", "score": 10}]}
    #     ]
    #
    #     print(all_movies(movies))
    #
    # print(all_movies(movies))
    # def filter_books(books, category=None):
    #     if category:
    #         category_filter = [book for book in books if book["author"] == category]
    #     else:
    #         category_filter = books
    #     sorted_books = (sorted(category_filter, key=lambda x: x["year"], reverse=False))
    #     return sorted_books
    #
    #
    # if __name__ == "__main__":
    #     books = [
    #         {"title": "Война и мир", "author": "Толстой", "year": 1869, "rating": 4.8},
    #         {"title": "Анна Каренина", "author": "Толстой", "year": 1877, "rating": 4.7},
    #         {"title": "1984", "author": "Оруэлл", "year": 1949, "rating": 4.6}
    #     ]
    #
    #     print(filter_books(books,"Толстой"))
    # def filter_department(departmens, category=None):
    #     if category:
    #         _testfilter_category = [department for department in departments if department["department"] == category]
    #     else:
    #         _testfilter_category = departments
    #     sorted_department = (sorted(_testfilter_category, key=lambda x: x["salary"], reverse=True))
    #
    #     return sorted_department
    #
    #
    # if __name__ == "__main__":
    #     departments = [
    #         {"name": "Иван", "department": "IT", "salary": 150000},
    #         {"name": "Петр", "department": "HR", "salary": 80000},
    #         {"name": "Анна", "department": "IT", "salary": 200000}
    #     ]
    #
    #     print(filter_department(departments, "IT"))

    #
    # def filter_student(students, category=None):
    #     if category:
    #         _testfilter_student = [student for student in students if student["group"] == category]
    #     else:
    #         _testfilter_student = students
    #
    #     sorted_students = (sorted(_testfilter_student, key=lambda x: x["group"], reverse=True))
    #     return sorted_students
    #
    #
    # if __name__ == '__main__':
    #     students = [
    #         {"name": "Аня", "group": "ИТ-101", "avg_grade": 4.5},
    #         {"name": "Боря", "group": "ИТ-101", "avg_grade": 3.8},
    #         {"name": "Вика", "group": "ЭК-202", "avg_grade": 4.9}
    #     ]
    #
    # print(filter_student(students,"ИТ-101"))
    # def filter_product(products, category=None):
    #     if category:
    #         filter_products = [product for product in products if product["category"] == category()]
    #     else:
    #         filter_products = products
    #
    #     sorted_products = sorted(filter_products, ket=lambda x: x["price"], reverse=True)
    #     return sorted_products

    # word_1 = [2, 3, 5, 7, 11]
    # word_2 = [-5, -7, -9, -13]
    # word_3 = [1, 2]
    # word_4 = [4]
    #
    #
    # def word(numbers_list):
    #     max_product = 0
    #     for i in range(len(numbers_list)):
    #
    #         for j in range(i + 1, len(numbers_list)):
    #             product = numbers_list[i] * numbers_list[j]
    #
    #             if product > max_product:
    #                 max_product = product
    #
    #     return max_product
    #
    #
    # print(word(word_1))
    # print(word(word_2))
    # print(word(word_3))
    # print(word(word_4))
    # def text_tx(strings):
    #     result = []
    #     for string in strings:
    #         if len(string) > 0 and string[0] == string == [-1]:
    #             result.append(string)
    #         elif len(string) == 0:
    #             result.append(string)
    #     return result
    #
    #
    # print('hello', 'world', 'apple', 'pear', 'banana', 'pop')
    # print('', 'madam', 'racecar', 'noon', 'level', '')
    # print([[]])
    # import os
    # from os import scandir
    #
    #
    # def get_directory(path=None, recursive=False):
    #     file_count = 0
    #     folder_count = 0
    #
    #     if path is None:
    #         path = os.getcwd()
    #     with os.scandir(path) as entries:
    #
    #         for entry in entries:
    #
    #             if entry.is_file():
    #                 file_count += 1
    #
    #
    #
    #             elif entry.is_dir() and recursive:
    #                 sub_result = get_directory(entry.path, recursive)
    #                 file_count += sub_result["files"]
    #                 folder_count += sub_result["folders"] +1
    #             else:
    #                 folder_count += 1
    #     return {"files": file_count, "folders": folder_count}
    #
    #
    # print(get_directory())
    # class Product:
    #
    #     def __init__(self, name, price, quantity):
    #         if price < 0:
    #             raise ValueError("цена товара не может быть отрицательной")
    #         self.name = name
    #         self.price = price
    #         self.quantity = quantity
    #

    #
    # class Category:
    #     def average_discount(self):
    #         try:
    #             total_discount = sum(product.discount for product in self.products)
    #             return total_discount / len(self.products)
    #         except ZeroDivisionError:
    #             return 0
    # from abc import ABC, abstractmethod
    #
    #
    # class BaseProduct(ABC):
    #     def __init__(self, *args, **kwargs):
    #         super().__init__()
    #
    #     @abstractmethod
    #     def __str__(self):
    #         pass
    #
    #     @abstractmethod
    #     def get_info(self):
    #         pass
    #
    #
    # class PrintInitMixin:
    #     def __init__(self, *args, **kwargs):
    #         print(f"{self.__class__.__name__}{args}")
    #
    #         super().__init__(*args, **kwargs)
    #
    #

    # class Product(PrintInitMixin, BaseProduct):
    #     def __init__(self, name, description, price, quantity, *args, **kwargs):
    #         super().__init__(name, description, price, quantity, *args, **kwargs)
    #         self.name = name
    #         self.description = description
    #         self.price = price
    #         self.quantity = quantity
    #
    #     def __add__(self, other):
    #         if type(self) != type(other):
    #             raise TypeError("ошибка")
    #
    #         else:
    #
    #             return self.price * self.quantity + other.price * other.quantity
    #
    #     def __str__(self):
    #         return (f"{self.name},{self.price}")
    #
    #     def get_info(self):
    #         return (f"{self.name}{self.description},{self.price},{self.quantity}")
    #
    #
    # class Category:
    #     def __init__(self, name, description):
    #         self.name = name
    #         self.description = description
    #         self.product = []
    #
    #     def add_product(self, product):
    #         if not isinstance(product, Product):
    #             raise TypeError("ошибка")
    #         else:
    #             self.product.append(product)
    #
    #
    # class PaperBook(Product):
    #
    #     def __init__(self, name, description, price, quantity,
    #                  author, pages, binding_type, weight, ):
    #         super().__init__(name, description, price, quantity,
    #                          author, pages, binding_type, weight)
    #         self.author = author
    #         self.pages = pages
    #         self.binding_type = binding_type
    #         self.weight = weight
    #
    #
    # class Ebook(Product):
    #
    #     def __init__(self, name, description, price, quantity,
    #                  author, file_format, file_size_mb, language):
    #         super().__init__(name, description, price, quantity,
    #                          author, file_format, file_size_mb, language)
    #         self.author = author
    #         self.file_format = file_format
    #         self.file_size_mb = file_size_mb
    #         self.language = language
    #
    #
    # paper_book = PaperBook(
    #     name="Война и мир",
    #     description="Роман Толстого",
    #     price=500,
    #     quantity=10,
    #     author="Толстой",
    #     pages=1200,
    #     binding_type="твёрдый",
    #     weight=800
    # )
    #
    # ebook = Ebook(
    #     name="Война и мир",
    #     description="Никита Назарова",
    #     price=1000,
    #     quantity=15,
    #     author="Толстой",
    #     file_format="EPUB",
    #     file_size_mb=5.2,
    #     language="ENG"
    # )
    #
