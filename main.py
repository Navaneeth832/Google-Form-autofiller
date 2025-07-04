from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import requests
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="./.env")
key=os.getenv("GEMINI_API_KEY")
print(f"🔐 Gemini API Key Loaded: {key}")
genai.configure(api_key="AIzaSyCssfshpE93EfbPOzKbcosNUggWTCEqs_U")
model = genai.GenerativeModel("gemini-2.0-flash")
# Separate URLs
view_url = 'https://docs.google.com/forms/d/e/1FAIpQLSfLO1MOk5lZtVWdKWZWZlN5EFh5DvtTP3PKPguhOt1wJteHXw/viewform'
submit_url = 'https://docs.google.com/forms/d/e/1FAIpQLSfLO1MOk5lZtVWdKWZWZlN5EFh5DvtTP3PKPguhOt1wJteHXw/formResponse'
# Launch browser
driver = webdriver.Chrome()
driver.get(view_url)

# Wait for JS to load
l=[]
# Extract all question elements (visible text only)
questions = driver.find_elements(By.CSS_SELECTOR, '[role="heading"]')
print("📝 Questions:\n")
for i, q in enumerate(questions, start=1):
    text = q.text.strip()
    if text and i>=2:
        print(f"{i}. {text}")
        l.append(text)
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()
answers=[]
for i in l:
    prompt="Generate a concise answer for the question: "+i+" in one line. The answer should be relevant to the question and not too long."
    if 'name' in i.lower():
        answers.append("Form AI Model")
    else:
        response = model.generate_content(prompt)
        answers.append(response.text)
# Extract all entry fields
fields = soup.find_all(['input', 'textarea', 'select'], attrs={'name': lambda x: x and x.startswith('entry.')})
form_data = {}
print("📝 Entry IDs found:")
for i, field in enumerate(fields):
    label = field.get('aria-label') or 'No label found'
    print(f"{i+1}. entry ID: {field['name']} | Label: {label}")
    field_id = field['name']
    
    # Smart dummy values based on field type
    if 'email' in label.lower():
        form_data[field_id] = 'test@example.com'
    elif 'name' in label.lower():
        form_data[field_id] = 'AI Model'
    else:
        form_data[field_id] = answers[i] if i < len(answers) else 'N/A'

# Send data
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.post(submit_url, data=form_data, headers=headers)

# Check response
if response.status_code == 200:
    print("✅ Form submitted successfully.")
else:
    print(f"❌ Failed. Status: {response.status_code}")
