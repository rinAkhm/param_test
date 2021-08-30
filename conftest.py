import pytest


@pytest.fixture()
def file_path(request):
    file_name = request.config.getini("log_file")
    return file_name


def pytest_addoption(parser):
    parser.addini('log_file', help='file', default='log.txt')
