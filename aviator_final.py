import os
from flask import Flask
from threading import Thread

# Render ko dokha dene ke liye ek chota server
app = Flask(__name__)
@app.route('/')
def home(): return "Bot is Alive!"

def run(): app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
Thread(target=run).start()

# --- AB AAPKA PURANA BOT CODE YAHAN SE SHURU HOGA ---
import time
import telebot
# ... (baaki ka pura code jo pehle tha)
import time
import telebot
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- CONFIG ---
TOKEN = "8613146352:AAHh2-cz3hp236lsOo0VjvZ1n26Glsyv48I"
CHAT_ID = "8746160474"
USER_ID = "359782714"
PASSWORD = "Ayankhan@123"
bot = telebot.TeleBot(TOKEN)

def start_engine():
    print("🚀 Server-Side Bot Start ho raha hai...")
    options = uc.ChromeOptions()
    options.add_argument('--headless') # Server ke liye zaroori
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    driver = uc.Chrome(options=options)
    
    try:
        driver.get("https://1wwooz.com")
        print("📡 Website khul rahi hai...")
        time.sleep(15) # Server par loading mein time lagta hai

        # --- AUTO LOGIN (BINA INPUT KE) ---
        try:
            # Login button dhundna
            login_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Login')] | //a[contains(text(), 'Login')]")
            login_btn.click()
            time.sleep(5)
            
            driver.find_element(By.NAME, "login").send_keys(USER_ID)
            driver.find_element(By.NAME, "password").send_keys(PASSWORD)
            driver.find_element(By.XPATH, "//button[@type='submit']").click()
            print("✅ Auto-Login Successful!")
            time.sleep(15)
        except:
            print("ℹ️ Login nahi ho paya ya pehle se login hai.")

        # --- MONITORING LOOP ---
        last_val = ""
        blue_count = 0
        print("📡 Monitoring LIVE! Check Telegram.")
        bot.send_message(CHAT_ID, "🚀 Bot is now LIVE on Server! Tracking starts now.")

        while True:
            try:
                driver.switch_to.frame(0)
                elements = driver.find_elements(By.CLASS_NAME, "bubble-multiplier")
                if elements:
                    current_val = elements[0].text.strip() # Latest number
                    if current_val != last_val and current_val != "":
                        val = float(current_val.replace('x', ''))
                        bot.send_message(CHAT_ID, f"🏁 Round: {current_val}")
                        
                        # sniper logic
                        if val < 1.30: blue_count += 1
                        else: blue_count = 0
                        if blue_count >= 6:
                            bot.send_message(CHAT_ID, "⚠️ SAFE SNIPER: 1.50x Target! 🚀")
                            blue_count = 0
                        
                        last_val = current_val
                driver.switch_to.default_content()
                time.sleep(5)
            except:
                time.sleep(5)
                continue
    except Exception as e:
        print(f"❌ Error: {e}")
        bot.send_message(CHAT_ID, f"⚠️ Bot stopped due to error: {e}")

if __name__ == "__main__":
    start_engine()

