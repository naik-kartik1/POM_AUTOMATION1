import pytest

@pytest.fixture(scope='class')
def test_setup(request):
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("http://localhost:8081/login")
    driver.implicitly_wait(30)
    request.cls.driver = driver