# 📝 Google Form Auto-Filler using Gemini AI

This Python program automates the process of reading a Google Form, generating smart answers using Gemini AI, and submitting the form — all through code.

---

## 🚀 Features

- ✅ Automatically reads all form questions
- 🤖 Uses Gemini AI to generate relevant one-line answers
- 🔐 Loads your API key securely from a `.env` file
- 📩 Submits the form with generated answers

---

## 📦 Requirements

- Python 3.7+
- Google Chrome installed
- ChromeDriver (matching your Chrome version)

---

## 📚 Install Dependencies

```bash
pip install selenium beautifulsoup4 python-dotenv requests google-generativeai
🔐 API Key Setup
Create a file named .env in your project folder.

Add the following line inside:

env
Copy
Edit
GEMINI_API_KEY=your_actual_api_key_here
✅ Do NOT add quotes around the key.
📁 Make sure .env is in the same folder as your Python script.

📂 Folder Structure
bash
Copy
Edit
Google-Form-autofiller/
├── test.py         # Main Python script
├── .env            # Stores your Gemini API Key
├── README.md       # This documentation
🧠 How It Works
Opens the target Google Form using Selenium

Extracts all visible questions

For each question:

If it's a name/email → adds a static value

Else → sends to Gemini AI for a one-liner response

Matches the extracted questions to the form's entry.XXXX IDs

Submits the form with a POST request

🖥️ Example Output
bash
Copy
Edit
📝 Questions:
2. Name
3. Aim
4. Yes/no

📝 Entry IDs found:
1. entry.1716460880 | Label: No label found
2. entry.1279561891 | Label: No label found
3. entry.XXXXXXX | Label: No label found

✅ Form submitted successfully.
⚠️ Notes
Works only on public Google Forms (no login required)

Make sure your ChromeDriver version matches your browser

Gemini API has usage limits and quota — don’t abuse it

🤝 Credits
Built by Navaneeth with 💻
Powered by Google Generative AI

yaml
Copy
Edit

---

### ✅ How to Use It

1. Copy the above and paste it into a file named `README.md`
2. Push it to your GitHub repo
3. It’ll be automatically rendered beautifully on your repo’s homepage


