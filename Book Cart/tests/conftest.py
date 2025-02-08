import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    print(f"Creating {browser} driver.")

    if browser == "firefox":
        my_driver = webdriver.Firefox()
    elif browser == "chrome":
        my_driver = webdriver.Chrome()
    elif browser == "safari":
        my_driver = webdriver.Safari()
    elif browser == "edge":
        my_driver = webdriver.Edge()
    else:
        raise TypeError(f"Expected 'firefox', 'chrome', 'safari' or 'edge' but got {browser}")

    my_driver.maximize_window()

    yield my_driver

    print(f"\nClosing {browser} driver.")
    # my_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="firefox", help="browser to execute tests (chrome, firefox)"
    )
