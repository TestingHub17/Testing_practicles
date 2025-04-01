import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.smoke
def test_send_url(driver):
    search_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR , '[name="name"]')))
    search_element.send_keys("Rachana")