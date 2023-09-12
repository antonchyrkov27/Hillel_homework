from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

HOME_PAGE_URL = "https://the-internet.herokuapp.com"


def test_open_website_and_check_title():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(HOME_PAGE_URL)
    assert driver.title == 'The Internet'
    sleep(1)
    driver.quit()


def test_open_website_and_check_elements():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(HOME_PAGE_URL)
    web_element = driver.find_element(By.CLASS_NAME, 'heading')
    assert web_element.is_displayed()
    assert web_element.text == 'Welcome to the-internet'
    sleep(1)
    driver.quit()


def test_open_checkboxes_page_and_check_their_manipulation():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(HOME_PAGE_URL)
    sleep(2)
    web_link = driver.find_element(By.LINK_TEXT, 'Checkboxes')
    assert web_link.is_displayed()
    web_link.click()
    sleep(2)
    assert driver.current_url == f'{HOME_PAGE_URL}/checkboxes'
    assert driver.find_element(By.TAG_NAME, 'h3').text == 'Checkboxes'
    checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    assert len(checkboxes) == 2
    assert not checkboxes[0].is_selected()
    assert checkboxes[1].is_selected()
    sleep(1)
    checkboxes[0].click()
    sleep(1)
    assert checkboxes[0].is_selected()
    sleep(1)
    checkboxes[1].click()
    assert not checkboxes[1].is_selected()
    sleep(1)
    driver.back()
    sleep(1)
    assert driver.current_url == f'{HOME_PAGE_URL}/'
    sleep(1)
    driver.forward()
    sleep(1)
    assert driver.current_url == f'{HOME_PAGE_URL}/checkboxes'
    driver.quit()


def test_inputs():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(HOME_PAGE_URL)
    sleep(1)
    web_link = driver.find_element(By.LINK_TEXT, 'Inputs')
    assert web_link.is_displayed()
    web_link.click()
    sleep(1)
    assert driver.current_url == f'{HOME_PAGE_URL}/inputs'
    assert driver.find_element(By.TAG_NAME, 'h3').text == 'Inputs'
    sleep(1)
    input_el = driver.find_element(By.XPATH, "//input[@type='number']")
    assert input_el.is_displayed()
    input_el.send_keys(50)
    sleep(1)

    assert input_el.get_attribute('value') == '50'

    driver.quit()
def test_key_presses():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/key_presses")
    sleep(1)
    assert driver.current_url == "https://the-internet.herokuapp.com/key_presses"
    assert driver.find_element(By.TAG_NAME, 'h3').text == 'Key Presses'
    input_field = driver.find_element(By.XPATH, "//input[@id='target']")
    assert input_field.is_displayed()
    input_field.send_keys(Keys.SPACE)  # Updated line
    result_message = driver.find_element(By.XPATH, "//p[@id='result']")
    assert result_message.is_displayed()
    assert result_message.text == 'You entered: SPACE'
    sleep(1)
    driver.quit()


from selenium.webdriver.common.action_chains import ActionChains


def test_redirector():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/redirector")
    sleep(1)
    assert driver.current_url == "https://the-internet.herokuapp.com/redirector"
    assert driver.find_element(By.TAG_NAME, 'h3').text == 'Redirection'
    redirect_button = driver.find_element(By.XPATH, "//a[@id='redirect']")
    assert redirect_button.is_displayed()

    action = ActionChains(driver)
    action.click(redirect_button)
    action.perform()

    sleep(2)
    new_url = driver.current_url
    assert new_url != "https://the-internet.herokuapp.com/redirector"
    assert new_url.startswith("https://the-internet.herokuapp.com/")
    sleep(1)
    driver.quit()


def test_status_codes():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(HOME_PAGE_URL)
    sleep(2)
    web_link = driver.find_element(By.LINK_TEXT, 'Status Codes')
    assert web_link.is_displayed()
    web_link.click()
    sleep(2)
    assert driver.current_url == f'{HOME_PAGE_URL}/status_codes'
    assert driver.find_element(By.TAG_NAME, 'h3').text == 'Status Codes'
    link_200 = driver.find_element(By.XPATH, './/a[@href="status_codes/200" and text() = "200"]')
    assert link_200
    hover = ActionChains(driver)
    hover.move_to_element(link_200).perform()
    assert hover
    sleep(1)
    link_200.click()
    sleep(1)
    assert driver.current_url == f'https://the-internet.herokuapp.com/status_codes/200'
    sleep(1)
    driver.back()
    sleep(2)
    link_301 = driver.find_element(By.XPATH, './/a[@href="status_codes/301" and text() = "301"]')
    assert link_301
    hover = ActionChains(driver)
    hover.move_to_element(link_301).perform()
    assert hover
    sleep(1)
    link_301.click()
    sleep(1)
    assert driver.current_url == f'https://the-internet.herokuapp.com/status_codes/301'
    sleep(1)
    driver.back()
    sleep(2)
    link_404 = driver.find_element(By.XPATH, './/a[@href="status_codes/404" and text() = "404"]')
    assert link_404
    hover = ActionChains(driver)
    hover.move_to_element(link_404).perform()
    assert hover
    sleep(1)
    link_404.click()
    sleep(1)
    assert driver.current_url == f'https://the-internet.herokuapp.com/status_codes/404'
    sleep(1)
    driver.back()
    sleep(2)
    link_500 = driver.find_element(By.XPATH, './/a[@href="status_codes/500" and text() = "500"]')
    assert link_500
    hover = ActionChains(driver)
    hover.move_to_element(link_500).perform()
    assert hover
    sleep(1)
    link_500.click()
    sleep(1)
    assert driver.current_url == f'https://the-internet.herokuapp.com/status_codes/500'
    sleep(1)
    home_link = driver.find_element(By.XPATH, './/a[@href="/status_codes" and text() = "here"]')
    assert home_link
    hover = ActionChains(driver)
    hover.move_to_element(home_link).perform()
    assert hover
    sleep(1)
    home_link.click()
    sleep(1)
    assert driver.current_url == f'https://the-internet.herokuapp.com/status_codes'
    sleep(2)

    driver.quit()