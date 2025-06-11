import os
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="function")
def browserInstance():
    driver = webdriver.Chrome(service=Service())
    driver.implicitly_wait(4)
    yield driver
    driver.quit()

# Tworzy unikalną nazwę pliku screena
def take_screenshot(driver, name):
    screenshots_dir = os.path.join(os.getcwd(), "screenshots")
    os.makedirs(screenshots_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filepath = os.path.join(screenshots_dir, f"{name}_{timestamp}.png")
    driver.save_screenshot(filepath)
    return filepath

# Hook do pytest-html – dodaje screen do raportu
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    global pytest_html
    outcome = yield
    report = outcome.get_result()

    # Jeśli test się nie powiedzie i jest dostępny driver
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("browserInstance")
        if driver:
            screenshot_path = take_screenshot(driver, item.name)
            # Dodaj screen do raportu HTML
            if hasattr(report, "extra"):
                report.extra.append(pytest_html.extras.image(screenshot_path))
            else:
                report.extra = [pytest_html.extras.image(screenshot_path)]

# Potrzebne, żeby pytest_html działał z report.extra
def pytest_configure(config):
    global pytest_html
    pytest_html = config.pluginmanager.getplugin("html")