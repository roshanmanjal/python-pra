import pyautogui
import pyperclip
import time

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.3

print("Switch to WhatsApp Web window...")
time.sleep(3)

# 1️⃣ Click once to focus WhatsApp Web chat
pyautogui.click(1353, 1165)   # inside chat area
time.sleep(0.3)

# 2️⃣ DRAG from TOP of chat to BOTTOM
pyautogui.moveTo(685, 212)        # start point (top message)
pyautogui.mouseDown()
time.sleep(0.1)

pyautogui.moveTo(1500 , 1040, duration=1.2)  # end point (bottom message)
pyautogui.mouseUp()

time.sleep(0.3)

# 3️⃣ COPY selected text
pyautogui.hotkey("ctrl", "c")
time.sleep(0.3)

# 4️⃣ READ clipboard
chat_text = pyperclip.paste()

print("\n===== COPIED CHAT TEXT =====\n")
print(chat_text)