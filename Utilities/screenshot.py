import os
from datetime import datetime

def capture_screenshot(driver, test_name):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )

    screenshot_name = f"{test_name}_{timestamp}.png"
    screenshot_path = os.path.join("Screenshots",screenshot_name)

    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved: {screenshot_path}")
