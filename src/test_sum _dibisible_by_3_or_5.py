import pytest
from src import is_palindrome


@pytest.mark.parametrize(
    "text, expected", [("madam", True),
                       ("racecar", True),
                       ("hello", False),
                       ("A man a plan a canal Panama", True),
                       ("12321", True),
                       ("python", False),
                       ("Was it a car or a cat I saw", True),
                       ("No 'x' in Nixon", True),

                       ])
def test_palidndrone(text, expected):
    assert is_palindrome(text) == expected

# import pytest
# from src import group_by_length
#
#
# @pytest.mark.parametrize("words, expected", [
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
# def test_group_by_length(words, expected):
#     result = group_by_length(words)
#     assert result == expected
# import pytest
# from src import convert_temperature
#
#
# def test_convert        ():
#     result = convert_temperature(100, "C", "F")
#     assert result == 212
# def test_num2():
# def test_num3():

# import pytest
# from src import check_phone
#
#
# def test_password():
#     assert check_phone("+7-9777256547") == True

# import  pytest
# from src import sum_divisible_by_3_or_5
#
# def norm_test():
#     assert sum_divisible_by_3_or_5([3,5,6])==14
#
# def test_empty_list():
#     assert  sum_divisible_by_3_or_5([])== 0
#
# def test_all_divisible():
#     assert sum_divisible_by_3_or_5([9,10,15])==34
#
# def test_none():
#     assert sum_divisible_by_3_or_5([1,2,4,7])==0
#
# def sum_divisible():
#     assert sum_divisible_by_3_or_5([3,5,6,9,10,15])==49
#
# def test_sum_divisible_by_3_or_5_with_negative_numbers():
#     assert sum_divisible_by_3_or_5([-1,-2,-3,-4,-5,-6,-7,-8,-9,-10])==-33
