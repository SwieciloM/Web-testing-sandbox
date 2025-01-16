from selenium import webdriver
import pytest


# @pytest.fixture(params=["firefox", "edge"])
@pytest.fixture(params=["firefox"])
def driver(request):
    # browser = request.config.getoption("--browser")
    browser = request.param
    print(f"Creating {browser} driver")

    if browser == "firefox":
        my_driver = webdriver.Firefox()
    elif browser == "edge":
        my_driver = webdriver.Edge()
    else:
        raise TypeError(f"Expected 'firefox' or 'edge' but got {browser}")

    my_driver.maximize_window()
    my_driver.implicitly_wait(1)

    yield my_driver

    print(f"\nClosing {browser} driver")
    # my_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="firefox", help="browser to execute tests (chrome, firefox)"
    )
