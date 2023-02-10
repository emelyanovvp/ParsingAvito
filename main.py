from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
import time
from selenium_stealth import stealth
stealth(driver, languages=["en-US", "en"], vendor="Google Inc.", platform="Win32",
        webgl_vendor="Intel Inc.", renderer="Intel Iris OpenGL Engine", fix_hairline=True,)
sp_texts = []
driver.implicitly_wait(10)
for page in range(1, 3):
    link = "https://www.avito.ru/anapa/kvartiry/prodam/1-komnatnye/vtorichka-ASgBAQICAUSSA8YQAkDmBxSMUsoIFIBZ?cd=1"
    if page == 1:
        driver.get(link)
    else:
        new_link = link + "&p=" + str(page)
        driver.get(new_link)
    all_blocks = driver.find_elements(By.CSS_SELECTOR, "div.iva-item-content-rejJg")
    for block in all_blocks:
        try:
            driver.execute_script("return arguments[0].scrollIntoView(true);", block) # necessary before clicking else it clicks on block
            show_tel = block.find_element(By.CSS_SELECTOR, ".iva-item-phone-qYKgK > div > button")
            driver.execute_script("arguments[0].click();", show_tel)                          # usual click doesn't work
            time.sleep(5)                                                      # for not to be banned for fast clicking
            driver.execute_script("return arguments[0].scrollIntoView(true);", block)   # necessary before get attribute
            time.sleep(5)
            tel_area = block.find_element(By.CSS_SELECTOR, "div.iva-item-phone-qYKgK > div > img")
            tel_link = tel_area.get_attribute("src")
            text = block.text + "\nМожно скопировать приведенную ниже ссылку и посмотреть номер телефона в браузере:\n" + tel_link
            sp_texts.append(text)
        except :
            continue

for n, item in enumerate(sp_texts, start=1):
    print(f'{n})  {item} ')
    print()

driver.quit()

