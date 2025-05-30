import pyautogui
import time
import pyperclip
from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load Gemini API key from .env file
load_dotenv()
GOOGLE_GEMINI_KEY = os.getenv("GOOGLE_GEMINI_KEY")

# Configure Gemini API
genai.configure(api_key=GOOGLE_GEMINI_KEY)

# Initialize Gemini model
model = genai.GenerativeModel('gemini-1.5-flash')

# Define system prompt
system_prompt = """
You are a person named Ronak who speaks Hindi as well as English.
You are from India and you are a intern under Ravi Singh and you talk about office work.
You analyze chat history and answer about office work only.
Output should be the next chat response (text message only) and short.
Do not start like this [21:02, 12/6/2024] Ravi Singh (SMARTNET):
"""

def is_last_message_from_sender(chat_log, sender_name="Ravi Singh (SMARTNET)"):
    lines = chat_log.strip().splitlines()
    for line in reversed(lines):
        if "] " in line:
            try:
                sender_part = line.split("] ")[1]
                sender_name_in_msg = sender_part.split(":")[0].strip()
                return sender_name.lower() in sender_name_in_msg.lower()
            except IndexError:
                continue
    return False



# Click Chrome icon
pyautogui.click(1164, 1061)
time.sleep(1)
pyautogui.click(502, 115)
time.sleep(14)
pyautogui.click(291, 266)
time.sleep(1)
pyperclip.copy("Ravi Singh")
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')  # Optional: directly open the chat
time.sleep(5)
pyautogui.click(738, 249)
time.sleep(1)

while True:
    time.sleep(5)

    # Select text from chat
    pyautogui.moveTo(742, 296)
    pyautogui.dragTo(1089, 960, duration=2.0, button='left')
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)
    pyautogui.click(1100, 976)

    # Get copied chat history
    chat_history = pyperclip.paste()
    print(chat_history)
    print(is_last_message_from_sender(chat_history))

    if is_last_message_from_sender(chat_history):
        try:
            response = model.generate_content([system_prompt, chat_history])
            roast = response.text.strip()
            pyperclip.copy(roast)

            # Paste roast into chat
            pyautogui.click(1100, 976)
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1)
            pyautogui.press('enter')
        except Exception as e:
            print("Error generating Gemini response:", e)
