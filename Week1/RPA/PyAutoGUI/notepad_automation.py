import pyautogui
import time
from datetime import datetime
import os

print("Automation started")

pyautogui.FAILSAFE = True
time.sleep(2)

# ✅ Correct target folder
save_folder = r"C:\Users\Dell Latitude\OneDrive\Desktop\2.Social Eagle AI\Assignments\RPA\Notepad Automated Report Creation"

# Ensure folder exists
os.makedirs(save_folder, exist_ok=True)

# File details
today = datetime.now().strftime("%Y-%m-%d")
filename = f"Automation_Report_{today}.txt"
full_path = os.path.join(save_folder, filename)

# File content
content = f"""
RPA Automation Report
---------------------
Tool Used: PyAutoGUI
Date: {today}

Objective:
Automate desktop actions and generate a report.

Approach:
- Python handled file creation (reliable)
- PyAutoGUI handled desktop automation

Status: SUCCESS
"""

# ✅ Create the file (NO UI dependency)
with open(full_path, "w", encoding="utf-8") as file:
    file.write(content)

print(f"File created at: {full_path}")

# ---- UI DEMO USING PyAutoGUI ----

# Open Notepad
pyautogui.hotkey("win", "r")
time.sleep(1)
pyautogui.write("notepad")
pyautogui.press("enter")
time.sleep(2)

# Open the generated file
pyautogui.hotkey("ctrl", "o")
time.sleep(2)
pyautogui.write(full_path)
pyautogui.press("enter")
time.sleep(2)

# Close Notepad
pyautogui.hotkey("alt", "f4")

print("Automation completed successfully")
