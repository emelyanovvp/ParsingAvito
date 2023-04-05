
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
import time
from selenium_stealth import stealth
stealth(driver, languages=["en-US", "en"], vendor="Google Inc.", platform="Win32",
        webgl_vendor="Intel Inc.", renderer="Intel Iris OpenGL Engine", fix_hairline=True,)
from selenium.common.exceptions import NoSuchElementException

sp_flats = []
driver.implicitly_wait(5)
for page in range(1, 3):
    link = "https://www.avito.ru/anapa/kvartiry/prodam/1-komnatnye-ASgBAQICAUSSA8YQAUDKCBSAWQ?cd=1"
    if page == 1:
        driver.get(link)
    else:
        new_link = link + "&p=" + str(page)
        driver.get(new_link)
    for block in range(1, 11):
        tel_list = []
        tel_xpath = '//div[contains(@data-marker,"item")][' + str(block) + ']//p[text()="Показать телефон"]'
        flat_xpath = '//div[contains(@data-marker,"item")][' + str(block) + ']'
        photo_xpath = '//div[contains(@data-marker,"item")]['+str(block)+']//img[contains(@data-marker,"phone-image")] '
        try:
            driver.execute_script("window.scrollTo(0, 0);")
            flat_element = driver.find_element(By.XPATH, flat_xpath)
            tel_button = driver.find_element(By.XPATH, tel_xpath)
            driver.execute_script("return arguments[0].scrollIntoView(true);", flat_element)
            time.sleep(2)
            driver.execute_script("return arguments[0].click();", tel_button)
            time.sleep(3)
            tel_element = driver.find_element(By.XPATH, photo_xpath)
            tel_link = str(tel_element.get_attribute("src"))
            text = flat_element.text + "\nПосмотреть номер телефона продавца можно, скопировав приведенную ниже ссылку в " \
                                       "поисковой строке браузера:\n" + tel_link
            sp_flats.append(text)
        except NoSuchElementException:
            print(f"In block {block} element is not present")
            continue

for n, item in enumerate(sp_flats, start=1):
    print(f'{n})  {item} ')
    print()

driver.quit()