# Playwright Web Automation – RPA Demo

## Project Overview
This project demonstrates **web automation using Python and Playwright**.  
The automation performs a Google search and navigates to a result page.

Due to Google security policies, **manual CAPTCHA handling** is intentionally included.

---

## Automation Workflow
1. Launch Chromium browser
2. Open Google homepage
3. Pause for manual CAPTCHA resolution (if shown)
4. Enter search keyword
5. Open first search result
6. Capture and print page title
7. Close browser

---

## Project Structure
RPA/Playwright/
│
├─ playwright_search.py
├─ README.md

Demo video: https://drive.google.com/file/d/1-mQj4wJm1NuLjC_CYmimA3i3ESaNS9zM/view?usp=sharing

---

## Technologies Used
- Python 3.x
- Playwright
- Chromium Browser

---

## Installation

```bash
pip install playwright
playwright install

CAPTCHA Handling

Google may display CAPTCHA due to automation detection.
The script pauses intentionally to allow manual CAPTCHA resolution before continuing.

This approach follows ethical automation practices.

Disclaimer

This automation is created for learning and demonstration purposes only.
No CAPTCHA bypass techniques are used.

Author

Praveen Kumar Selvaraj
Python | RPA | Selenium | Playwright
