import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Set type of browser:chrome(default), firefox, edge"
    )


@pytest.fixture
def get_chrome_options():
    chrome_options = ChromeOptions()
    chrome_options.add_argument('chrome')    # use 'headless' if you don't need a browser UI / 'chrome' if UI need
    chrome_options.add_argument('--start-maximized')    # Starts the browser maximized, regardless of any previous settings
    # chrome_options.add_argument('--window-size=1920,1080')
    # chrome_options.add_experimental_option("detach", True)   # Keeps the browser open
    # chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    return chrome_options


@pytest.fixture
def get_firefox_options():
    firefox_options = FirefoxOptions()
    firefox_options.add_argument('firefox')
    firefox_options.add_argument('--start-maximized')
    firefox_options.add_argument('--window-size=1920,1080')
    return firefox_options


@pytest.fixture
def get_edge_options():
    edge_options = EdgeOptions()
    edge_options.add_argument('edge')
    edge_options.add_argument('--start-maximized')
    edge_options.add_argument('--window-size=1920,1080')
    return edge_options


@pytest.fixture
def get_webdriver(request, get_chrome_options, get_firefox_options, get_edge_options):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        options = get_chrome_options
        driver = webdriver.Chrome(options=options)
        print("Chrome Browser")
    elif browser_name == "firefox":
        options = get_firefox_options
        driver = webdriver.Firefox(options=options)
        print("Firefox Browser")
    elif browser_name == "edge":
        options = get_edge_options
        driver = webdriver.Edge(options=options)
        print("Edge Browser")
    return driver


@pytest.fixture(scope="function")
def setup(request, get_webdriver):
    driver = get_webdriver
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.implicitly_wait(2)
    # driver.maximize_window()
    print(driver.title)
    print(driver.current_url)
    request.cls.driver = driver
    yield
    driver.close()
    # driver.quite()


# @pytest.mark.hookwrapper
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)