import re
import pytest


def log(file_name: str, text: str):
    with open(file_name, 'a', encoding='utf-8') as file:
        try:
            file.write(text + '\n')
        finally:
            file.close()


def check_to_valid_email(email: str) -> bool:
    return bool(re.search(r'^[\w\.\+\-]+\@[ \w]+\.[a-z]{2,3}$', email['email']))


@pytest.mark.parametrize("data", [
    {'email': 'test@test.ru', "expected": True},
    {'email': 'w@w.com', 'expected': True},
    {'email': '123QWE@mmm.mmm', 'expected': True}
])
def test_valid_email(data: dict, file_path: str):
    temp = check_to_valid_email(data)
    if temp is True:
        log(file_path, f'Результат {temp}: почта {data["email"]} валидная')
        assert temp == data['expected']


@pytest.mark.parametrize("data", [
    {'email': 'test@test.', 'expected': False},
    {'email': 'w@', 'expected': False},
    {'email': '@tt', 'expected': False}
])
def test_invalid_email(data: dict, file_path: str):
    temp = check_to_valid_email(data)
    if temp is False:
        log(file_path, f'Результат {temp}: почта {data["email"]} невалидная')
        assert temp == data['expected']
