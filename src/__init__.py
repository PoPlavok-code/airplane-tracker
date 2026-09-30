

# def where_the_person_is(arr, target):
#     left, right = 0, len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#         return - 1
# import pytest
#
#
# def is_palindrome(text):
#     text = text.replace(" ", "").replace("'", "").lower()
#     return text == text[::-1]
# import pytest
#
#
# def is_anagram(str1,str2):
#     str1 = str1.replace(" ","").lower()
#     str2 = str2.replace(" ","").lower()
#     return  sorted(str1) == sorted((str2))
# @pytest.mark.parametrize("str1,str2,expected",[
#    ("listen", "silent", True),
#         ("anagram", "nagaram", True),
#         ("rail safety", "fairy tales", True),
#         ("A gentleman", "Elegant man", True),
#         ("hello", "world", False),
#         ("python", "java", False),
#         ("test", "best", False),
#         ("anagram", "manga", False),
#         ("Listen", "Silent", True),
#         ("Dormitory", "Dirty room", True),
#         ("The eyes", "They see", True),
#         ("School master", "The classroom", True),
#     ]
# )
# def test_is_anagram(str1, str2, expected):
#     assert is_anagram(str1, str2) == expected


# import pytest
#
#
# def reverse_matrix(matrix):
#     """Отражает матрицу по горизонтали (переворачивает строки)"""
#     rows = len(matrix)
#
#     result = []
#     for i in range(rows):
#         result.append(matrix[rows - 1 - i])
#
#     return result
#
#
# # ===== ФИКСТУРЫ =====
#
# @pytest.fixture
# def matrix3x3():
#     return [
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]
#     ]
#
#
# @pytest.fixture
# def matrix3x4():
#     return [
#         [3, 5, 6, 7],
#         [4, 5, 6, 7],
#         [3, 5, 6, 7]
#     ]
#
#
# @pytest.fixture
# def matrix4x5():
#     return [
#         [1, 2, 3, 5, 5],
#         [2, 5, 5, 6, 7],
#         [3, 4, 5, 6, 7],
#         [1, 3, 5, 54, 5]
#     ]
#
#
# @pytest.fixture
# def single_row():
#     return [
#         [1, 2, 5]
#     ]
#
#
# # ===== ПАРАМЕТРИЗОВАННЫЙ ТЕСТ =====
#
# @pytest.mark.parametrize(
#     "matrix_fixture, expected",
#     [
#         ("matrix3x3", [[7, 8, 9], [4, 5, 6], [1, 2, 3]]),
#         ("matrix3x4", [[3, 5, 6, 7], [4, 5, 6, 7], [3, 5, 6, 7]]),
#         ("matrix4x5", [
#             [1, 3, 5, 54, 5],
#             [3, 4, 5, 6, 7],
#             [2, 5, 5, 6, 7],
#             [1, 2, 3, 5, 5]
#         ]),
#         ("single_row", [[1, 2, 5]]),  # одна строка не меняется
#     ]
# )
# def test_reverse_matrix(matrix_fixture, expected, request):
#     matrix = request.getfixturevalue(matrix_fixture)
#     assert reverse_matrix(matrix) == expected
# import pytest
#
#
# @pytest.mark.parametrize("words", "exepected", [
#     (["a", "bb", "ccc", "dd"],
#      {1: ["a"], 2: ["bb", "dd"], 3: ["ccc"]}),
#
#     (["кот", "дом", "автомобиль", "лес"],
#      {3: ["кот", "дом", "лес"], 10: ["автомобиль"]}),
#
#     ([], {}),
#
#     (["x", "y", "z"], {1: ["x", "y", "z"]})
# ])
# def group_by_length(words):
#     result_lenght = {}
#
#     for char in words:
#         lenght = len(char)
#         if lenght not in result_lenght:
#             result_lenght[lenght] = [char]
#         else:
#             result_lenght[lenght] += [char]
#     return result_lenght

# import pytest
#
#
# @pytest.mark.parametrize("coll", "exepected",
#                          [([1, 1, 2, 2, 3], {1: 2, 2: 2, 3: 1})  # → {1: 2, 2: 2, 3: 1}
#                               (['a', 'b', 'a', 'a'], {"a": 3, "b": 1})  # → {'a': 3, 'b': 1}
#                               ([], {})  # → {}
#                               ([5, 5, 5, 5], {5: 4})  # → {5: 4}
#                               ([1, 2, 3], {1: 1, 2: 1, 3: 1})  # → {1: 1, 2: 1, 3: 1}
#
#                           ])
# def count_frequencies(coll):
#
#     result = {}
#
# for char in coll:
#     if char not in result :
#
#         result[char] = 1
#     else:
#         pass
#     result[char] += 1

# def merge_inventores(inv1, inv2):
#     merge = inv1.copy()
#
#     for item in inv2:
#         if item in merge:
#             merge[item] += inv2[item]
#         else:
#             merge[item] = inv2[item]
#     return merge
#
#
# import pytest
#
#
# @pytest.mark.parametrize("coll,expected"[
#
#
# ([1, 1, 2, 2, 3],[[1,2],[2,3],[3,1]]),  # → [[1, 2], [2, 2], [3, 1]]
# ([1, 2, 3, 4, 5],[[1,2][2,3][4,5]]),  # → [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1]]
# ([1, 1, 1, 1, 1],[[1,5]]),  # → [[1, 5]]
# ([]),  # → []
# (['a', 'a', 'b', 'b', 'a'],[["a",2],["b",2],["a",1]])  # → [['a', 2], ['b', 2], ['a', 1]])
# ])
#
# def my_run_length_encode(coll):
#     if not coll:
#         return []
#     count = 1
#     result==[]
#     for i in range(1, len(coll)):
#         if coll[i] == coll[i - 1]:
#             count +=1
#         else:
#             # result.append ([coll[i-1],count])
#             count = 1
#             result.append([coll[-1],count])
#
#         return result
# import pytest
#
#
# @pytest.mark.parametrize("coll, expected, expected_length", [
#     ([1, 1, 2, 2, 3], [1, 2, 3], 3),
#     ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 5),
#     ([1, 1, 1, 1, 1], [1], 1),
#     ([], [], 0),
#     ([1, 2, 2, 3, 3, 3, 2], [1, 2, 3, 2], 4), ])
# def my_compress(coll, expected, expected_length):
#     if not coll:
#         return []
#     result = [coll[0]]
#     for i in range(1, len(coll)):
#         if coll[i]!= coll[i-1]:
#             result.append(coll[i])
#     return result
# import pytest
#
#
# @pytest.mark.parametrize("coll, size, expected", [
#     ([1, 2, 3, 4, 5], 2, [[1, 2], [3, 4], [5]]),
#     ([1, 2, 3], 1, [[1], [2], [3]]),
#     ([1, 2, 3], 5, [[1, 2, 3]]),
#     ([], 3, []),
#     ([1, 2, 3, 4], 3, [[1, 2, 3], [4]]),
# ])
# def my_chunk(cool, size):
#     if not cool or size < 0:
#         return []
#     result = []
#
#     for i in range(0, len(cool), size):
#         result.append(coll[i:i + size])
#     return result
# @pytest.mark.parametrize("coll, start, end, expected",
#     [
#         ([], 0, None, []),  # Пустой список
#         ([1, 2, 3, 4, 5], 0, None, [1, 2, 3, 4, 5]),  # Все элементы
#         ([1, 2, 3, 4, 5], 2, None, [3, 4, 5]),  # Срез с началом
#         ([1, 2, 3, 4, 5], 1, 3, [2, 3]),  # Срез с началом и концом
#         ([1, 2, 3, 4, 5], -2, None, [4, 5]),  # Срез с отрицательным началом
#         ([1, 2, 3, 4, 5], -10, None, [1, 2, 3, 4, 5]),  # Срез с отрицательным началом за пределами длины
#         ([1, 2, 3, 4, 5], 0, 3, [1, 2, 3]),  # Срез с концом
#         ([1, 2, 3, 4, 5], 1, -1, [2, 3, 4]),  # Срез с отрицательным концом
#     ])
# def my_slice(coll, start=0, end=None):
#     """
#     Возвращает новый массив, содержащий копию части исходного массива.
#     :param coll: исходный список.
#     :param start: индекс, по которому начинается извлечение. Если индекс отрицательный,
#     start указывает смещение от конца списка. По умолчанию равен нулю.
#     :param end: индекс, по которому заканчивается извлечение (не включая элемент с индексом end).
#     Если индекс отрицательный, end указывает смещение от конца списка. По умолчанию равен длине исходного списка.
#     :return: массив элементов
#     """
#     length = len(coll)
#
#     if length == 0:
#         return []
#
#     normalized_end = length if end is None else end
#
#     normalized_start = start
#
#     if normalized_start < 0:
#         if normalized_start < -length:
#             normalized_start = 0
#         else:
#             normalized_start += length
#
#     return coll[normalized_start:normalized_end]

# import pytest
#
#
# @pytest.mark.parametrize("value, from_unit, to_unit,expected", [
#     (100, "C", "F", 212.0),  # C → F
#     (212, "F", "C", 100.0),  # F → C (исправлено!)
#     (0, "C", "K", 273.15),  # C → K
#     (373.15, "K", "C", 100.0),  # K → C
#     (100, "X", "C", None)
#
# ])
# def convert_temperature(value, from_unit, to_unit):
#     if from_unit == to_unit:
#         return value
#     elif from_unit == "C":
#         celsius = value
#
#     elif from_unit == "F":
#         celsius = (value - 32) * 5 / 9
#
#     elif from_unit == "K":
#         celsius = value - 273.15
#
#     if to_unit == "C":
#        return round (celsius,2)
#     elif to_unit == "F":
#         return round((celsius * 9 / 5) + 32,2)
#     elif to_unit == "K":
#         return round( celsius + 273.15,2)
#     else:
#         return  None
#

# C → F
# (celsius * 9/5) + 32
# C → K
# celsius + 273.15
# F → C
# (value - 32) * 5/9
# K → C
# value - 273.15

# def test_convert(value, from_unit, to_unit, expected):
#     assert convert_temperature(value, from_unit, to_unit) == expected

# import pytest
#
#
# @pytest.fixture
# def test_num1():
#     return {"numbers": [1, 2, 3, 4, 5, 6, 7, 8],"expected":4}
#

# @pytest.fixture
# def test_num2():
#     return {"numbers": [11, 12, 31, 43, 54]}
#
#
# @pytest.fixture
# def test_num3():
#     return {"numbers": [111, 12, 1331, 131]}
#
#
# def chech_numbers(numbers):
#     count = 0
#     for num in numbers:
#         if num % 2 == 0:
#             count += 1
#     return count
#
# def test_count1(test_num1):
#         result = chech_numbers(test_num1["numbers"])
#         assert result == test_num1["expected"]
# import pytest
#
#
# @pytest.fixture
# def test_data_1():
#     return {"numbers": [1, 2, 3, 2, 4, 5, 2], "target": 2, "expected": 3}
#
# @pytest.fixture
# def test_data_2():
#     return {"numbers": [1, 2, 3, 4, 5], "target": 7, "expected": 0}
#
# @pytest.fixture
# def test_data_3():
#     return {"numbers": [5, 5, 5, 5, 5], "target": 5, "expected": 5}
#
#
# def count_number_in_list(numbers, target):
#     count = 0
#     for num in numbers:
#         if num == target:  # ← num, а не numbers!
#             count += 1
#     return count  # ← Вне цикла!
#
#
# def test_count_1(test_data_1):
#     result = count_number_in_list(test_data_1["numbers"], test_data_1["target"])
#     assert result == test_data_1["expected"]
#
# def test_count_2(test_data_2):
#     result = count_number_in_list(test_data_2["numbers"], test_data_2["target"])
#     assert result == test_data_2["expected"]
#
# def test_count_3(test_data_3):
#     result = count_number_in_list(test_data_3["numbers"], test_data_3["target"])
#     assert result == test_data_3["expected"]
# def check_phone(phone):
#     if not phone:
#         return False
#     if not phone.startswith("+"):
#         return False
#     dash_index = phone.find("-")
#     if dash_index == -1:
#         return False
#     counter_code = phone[1:dash_index]
#     if not counter_code.isdigit():
#         return False
#     number = phone[dash_index + 1:]
#
#     if len(counter_code)<1 or len(counter_code)>3:
#         return False
#     if len(number)<7 or len(number)>10:
#         return False
#     if not number.isdigit():
#         return False
#     if len(phone) < 10 or len(phone) > 15:
#         return False
#     return True
#
#
# print(check_phone("+7-777256547"))      # True
# print(check_phone("+375-291234567"))    # True
# print(check_phone("+1-5551234"))        # True
# print(check_phone("8-1234567890"))      # False (нет +)
# print(check_phone("+71234567890"))      # False (нет дефиса)
# print(check_phone("+7-123"))            # False (короткий)
# print(check_phone("+7-abc1234567"))     # False (буквы)
# print(check_phone("+12345-1234567"))    # False (код > 3)
# def check_username(username):
#     if not username:
#         return False
#
#     # Проверка длины (от 3 до 16)
#     if len(username) < 3 or len(username) > 16:
#         return False
#
#     # Начинается с буквы
#     if not username[0].isalpha():
#         return False
#
#     # Только буквы и цифры
#     if not username.isalnum():
#         return False
#
#     # Проверка на две одинаковые буквы подряд
#     for i in range(len(username) - 1):
#         if username[i] == username[i + 1]:
#             return False
#
#     return True
# # def check_password(password):
#     if not password:
#         return False
#     if len(password) < 8:
#         return False
#     if password.islover():
#         return False
#     if not any(char.isdigit() for char in password):
#         return False
#     special_chars = "!@#$"
#     if not any(char in special_chars for char in password):
#         return False
#     return True

# def check_email():
#     if not email:
#         return False
#     if "@" not in email or "." not in email:
#         return False
#     at_index = email.find("@")
#     dot_index = emaik.find(".", at_index)
#     if at_index < 1 or dot_index < + 2 or dot_index == len(email) - 1:
#         return False
#     return True

# def sum_divisible_by_3_or_5(lst):
#     """
#     Функция принимает на вход список чисел и возвращает сумму всех элементов списка,
#     которые делятся на 3 или 5 без остатка.
#     """
#     result = 0
#     for num in lst:
#         if num % 3 == 0 or num % 5 == 0:
#             result += num
#     return result
# #
#
# def analyze_drivers(trips):
#     driver_by_trips = {}
#
#     for trip in trips:
#         driver = trip["driver"]
#         if driver not in driver_by_trips:
#             driver_by_trips[driver] = {
#                 "trips_count": 0,
#                 "total_distance": 0,
#                 "total_duration": 0,
#
#             }
#         driver_by_trips[driver]["trips_count"] += 1
#         driver_by_trips[driver]["total_distance"] += (trip["distance"])
#         driver_by_trips[driver]["total_duration"] += (trip["duration"])
#     for driver in driver_by_trips:
#         total_distance = driver_by_trips[driver]["total_distance"]
#         total_duration = driver_by_trips[driver]["total_duration"]
#         driver_by_trips[driver]["avg_speed"] = round(
#             (total_distance / total_duration) * 60, 1)
#
#         return driver_by_trips
#
#
# if __name__ == "__main__":
#     trips = [
#         {"driver": "Иван", "route": "Центр-Аэропорт", "distance": 30, "duration": 45},
#         {"driver": "Иван", "route": "Аэропорт-Центр", "distance": 32, "duration": 50},
#         {"driver": "Петр", "route": "Вокзал-Отель", "distance": 15, "duration": 20},
#         {"driver": "Петр", "route": "Отель-Вокзал", "distance": 15, "duration": 25},
#         {"driver": "Петр", "route": "Центр-Вокзал", "distance": 10, "duration": 15}
#     ]
#     print(analyze_drivers(trips))
# def analyze_departments(employees):
#     all_emploees = {}
#     for employee in employees:
#         department = employee["department"]
#         if department not in all_emploees:
#             all_emploees[department] = {
#                 "employees_count": 0,
#                 "total_tasks_count": 0,
#                 "avg_hours_per_task": 0,
#                 "hours_sum": 0,
#
#             }
#         all_emploees[department]["employees_count"] += 1
#         all_emploees[department]["total_tasks_count"] += len(employee["tasks"])
#         for hours in employee["tasks"]:
#             all_emploees[department]["hours_sum"] += hours
#     for department in all_emploees:
#         hours_sum = all_emploees[department]["hours_sum"]
#         total_tasks_count =all_emploees [department]["total_tasks_count"]
#         all_emploees[department]["avg_hours_per_task"] = round(hours_sum / total_tasks_count, 1)
#
#     return all_emploees
#
#
# if __name__ == "__main__":
#     employees = [
#         {"name": "Алексей", "department": "IT", "tasks": [8, 10, 8]},
#         {"name": "Мария", "department": "IT", "tasks": [9, 9]},
#         {"name": "Дмитрий", "department": "Бухгалтерия", "tasks": [7, 8, 7, 8]}
#     ]
#
#     print(analyze_departments(employees))
# def all_students(students):
#     students_by_subject = {}
#
#     for student in students:
#         subject = student["subject"]
#
#         if subject not in students_by_subject:
#             students_by_subject[subject] = {
#                 "students_count": 0,
#                 "all_grades_count": 0,
#                 "grade_sum": 0
#             }
#
#         students_by_subject[subject]['students_count'] += 1
#         students_by_subject[subject]["all_grades_count"] += len(student["grades"])
#
#         for grade in student["grades"]:
#             students_by_subject[subject]['grade_sum'] += grade
#
#     for subject in students_by_subject:
#         grade_sum = students_by_subject[subject]["grade_sum"]
#         all_grades_count = students_by_subject[subject]["all_grades_count"]
#         students_by_subject[subject]["avg_grade"] = round(grade_sum / all_grades_count, 2)
#
#     return students_by_subject
#
#
# if __name__ == "__main__":
#     students = [
#         {"name": "Иван", "subject": "Математика", "grades": [5, 4, 5]},
#         {"name": "Петр", "subject": "Математика", "grades": [3, 4]},
#         {"name": "Анна", "subject": "Физика", "grades": [5, 5, 5]}
#     ]
#     print(all_students(students))
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
