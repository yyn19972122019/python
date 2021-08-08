import pytest
from selenium import webdriver
@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    yield driver
if __name__ == '__main__':
    1