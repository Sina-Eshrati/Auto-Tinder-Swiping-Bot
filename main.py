from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

# ------------------------------- Create The Driver ------------------------------------
service = Service(executable_path="E:\Softwares\Chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://tinder.com/")
time.sleep(4)

# ------------------------------- Login To Tinder via FaceBook -------------------------
login_main_page = driver.find_element(By.LINK_TEXT, "Log in")
login_main_page.click()
time.sleep(2)

fb_login = driver.find_element(By.XPATH, '//*[@id="c207610411"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]')
fb_login.click()
time.sleep(2)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

email_input = driver.find_element(By.XPATH, '//*[@id="email"]')
email_input.send_keys("sina_eshrati@yahoo.com")
password_input = driver.find_element(By.XPATH, '//*[@id="pass"]')
password_input.send_keys("sinairge1376")
login_button = driver.find_element(By.NAME, "login")
login_button.click()
driver.switch_to.window(base_window)
time.sleep(6)


allow_location = driver.find_element(By.XPATH, '//*[@id="c207610411"]/div/div/div/div/div[3]/button[1]')
allow_location.click()
accept_cookies = driver.find_element(By.XPATH, '//*[@id="c-13730025"]/div/div[2]/div/div/div[1]/button')
accept_cookies.click()
time.sleep(1)
not_interested_notifications = driver.find_element(By.XPATH, '//*[@id="c207610411"]/div/div/div/div/div[3]/button[2]')
not_interested_notifications.click()
time.sleep(6)

# -------------------------------------- Hit like -------------------------------
try:
    maybe_later = driver.find_element(By.XPATH, '//*[@id="c207610411"]/div/div/div/div[3]/button[2]')
    maybe_later.click()
    time.sleep(2)
except NoSuchElementException:
    pass

for n in range(50):
    time.sleep(2)
    try:
        body = driver.find_element(By.TAG_NAME, 'body')
        body.send_keys(Keys.ARROW_RIGHT)
        print("ok")
    except NoSuchElementException:
        time.sleep(2)
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            time.sleep(2)