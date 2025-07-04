from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup
driver = webdriver.Chrome()
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfLO1MOk5lZtVWdKWZWZlN5EFh5DvtTP3PKPguhOt1wJteHXw/viewform")
time.sleep(3)
l=[]
# Extract all question elements (visible text only)
questions = driver.find_elements(By.CSS_SELECTOR, '[role="heading"]')
print("📝 Questions:\n")
for i, q in enumerate(questions, start=1):
    text = q.text.strip()
    if text and i>=2:
        print(f"{i}. {text}")
        l.append(text)
        print(type(text))
print(l)
driver.quit()
