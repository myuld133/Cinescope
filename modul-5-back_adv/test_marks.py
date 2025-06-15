import pytest

# Пропускает тест без условий
@pytest.mark.skip(reason="Временно отключён")
def test_example():
    assert 1 + 1 == 2

# Пропускает тест, если условие истинно.
skip_test = True
@pytest.mark.skipif(skip_test, reason="Тест отключён вручную")
def test_skipif_demo():
    assert True

# Обозначает, что тест ожидаемо должен упасть
@pytest.mark.xfail(reason="Функция ещё не реализована")
def test_future_feature():
    assert 1 == 2

# Пример - неожиданное прохождение (XPASS)
@pytest.mark.xfail(reason="Баг в системе")
def test_fixed_bug():
    assert 2 + 2 == 4

# Позволяет подключить фикстуру без явного указания её в аргументах функции.
# вариант 1

@pytest.fixture
def setup_data():
    print("Setup99")
    return 3

@pytest.mark.usefixtures("setup_data")
def test_with_usefixtures():
    print(setup_data)
    assert True

# вариант 2
@pytest.fixture
def setup_data2():
    print("Setup")

def test_with_fixture(setup_data2):
    assert True

@pytest.mark.smoke
def test_addition():
    assert 1 + 1 == 2

@pytest.mark.regression
def test_subtraction():
    assert 5 - 3 == 2

@pytest.mark.api
def test_multiplication():
    assert 2 * 3 == 6

@pytest.mark.slow
def test_division():
    assert 10 / 2 == 5