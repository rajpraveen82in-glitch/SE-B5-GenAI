# Selenium RPA Automation – News Scraper Demo

## Project Overview
This project demonstrates **Robotic Process Automation (RPA)** using **Python and Selenium WebDriver**.  
The automation extracts the **top 5 news articles** from BBC Search for a given keyword and saves the data in a CSV file.

This project is designed to be **stable, CAPTCHA-free, and demo-friendly**.

---

## Automation Workflow
1. Launch Google Chrome using Selenium WebDriver.
2. Navigate to **BBC Search** (direct URL to avoid CAPTCHA).
3. Enter a search keyword (e.g., *Artificial Intelligence*).
4. Wait for search results to load.
5. Extract the **top 5 news articles**, including title and URL.
6. Save the extracted data into `results.csv`.
7. Close the browser automatically.

---

## Folder Structure
RPA/Selenium/
│
├── selenium_search.py # Main automation script
├── README.md # Project documentation

Demo video link: https://drive.google.com/file/d/1UR8TJzp1sP94fiX6H0Rb5BNsHCcfTa7S/view?usp=sharing


---

## Technologies Used
- Python 3.x
- Selenium WebDriver
- Google Chrome
- ChromeDriver

---

Expected Output

The browser opens and performs a search on BBC.

The console prints the top 5 news article titles.

results.csv is created in the project folder with the following structure:

S.No,Title,URL
1,AI used to detect cancer earlier,https://www.bbc.com/news/...
2,How AI is changing jobs,https://www.bbc.com/news/...
...

Best Practices Followed

Explicit waits for dynamic web elements

Stable XPath selectors

CSV-based output for easy reporting

Clean folder structure for RPA submissions

CAPTCHA-free workflow

Learning Outcomes

Hands-on experience with Selenium WebDriver

Safe automation on live websites

Data extraction and reporting

Writing maintainable RPA scripts suitable for demos

Disclaimer

This project is created for learning and demonstration purposes only.
No CAPTCHA bypassing is attempted. All automation is ethical and safe.

Author

Praveen Kumar Selvaraj
Python | RPA | Selenium | Playwright | PyAutoGUI
