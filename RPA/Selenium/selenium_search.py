from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

SEARCH_QUERY = "artificial intelligence"
OUTPUT_FILE = "results.csv"

print("Starting Selenium RPA automation...")

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 20)

# Open BBC Search directly (no CAPTCHA)
driver.get("https://www.bbc.co.uk/search")

# Wait for search box
search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
search_box.send_keys(SEARCH_QUERY)
search_box.send_keys(Keys.ENTER)

# Wait for results to load
wait.until(EC.presence_of_element_located((By.TAG_NAME, "main")))

# Collect news links
links = driver.find_elements(By.XPATH, "//main//a[@href]")

data = []
count = 0

for link in links:
    title = link.text.strip()
    url = link.get_attribute("href")

    if title and "/news/" in url:
        count += 1
        print(f"{count}. {title}")
        data.append([count, title, url])

    if count == 5:
        break

# Save output
with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["S.No", "Title", "URL"])
    writer.writerows(data)

print(f"Saved {len(data)} articles to {OUTPUT_FILE}")

driver.quit()
print("Selenium RPA automation completed successfully.")
