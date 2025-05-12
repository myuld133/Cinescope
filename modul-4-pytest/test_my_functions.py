# test_my_functions.py
def add(a, b):
    return a + b

class TestMyFunctions:

    def test_add_positive_numbers(self):
        assert add(2, 3) == 5


    def test_add_negative_numbers(self):
        assert add(-1, -4) == -5


    def test_add_positive_and_negative(self):
        assert add(5, -2) == 3


    def test_add_string(self):
        assert add("test", "string") == "test string"  # тест который должен упасть
