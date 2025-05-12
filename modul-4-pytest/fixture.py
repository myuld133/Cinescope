def test_sum(input_data): # используем фикстуру как аргумент функции
    assert sum(input_data) == 15

def test_len(input_data): # используем фикстуру как аргумент функции
    assert len(input_data) == 5