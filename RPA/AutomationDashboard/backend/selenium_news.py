from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def fetch_news(keyword="artificial intelligence"):
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)

    driver.get("https://www.bbc.co.uk/search")
    search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
    search_box.send_keys(keyword)
    search_box.send_keys(Keys.ENTER)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "main")))

    links = driver.find_elements(By.XPATH, "//main//a[@href]")
    data = []
    count = 0
    for link in links:
        title = link.text.strip()
        url = link.get_attribute("href")
        if title and "/news/" in url:
            count += 1
            data.append({"title": title, "url": url})
        if count == 5:
            break

    driver.quit()
    return data
