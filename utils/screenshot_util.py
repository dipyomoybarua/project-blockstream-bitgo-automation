import os
from selenium.webdriver.remote.webdriver import WebDriver

def take_screenshot(driver: WebDriver, test_name: str):
    """Take a screenshot and save it to the screenshots directory."""
    screenshot_path = os.path.join(os.getcwd(), "screenshots")
    if not os.path.exists(screenshot_path):
        os.makedirs(screenshot_path)
    screenshot_file = os.path.join(screenshot_path, f"{test_name}.png")
    driver.save_screenshot(screenshot_file)
    print(f"Screenshot saved to {screenshot_file}")
