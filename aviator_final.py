import time
import telebot
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# --- CONFIG ---
TOKEN = "8613146352:AAHh2-cz3hp236lsOo0VjvZ1n26Glsyv48I"
CHAT_ID = "8746160474"
USER_ID = "359782714"
PASSWORD = "Ayankhan@123"
bot = telebot.TeleBot(TOKEN)

def start_server_bot():
    print("🚀 Server-Side Aviator Bot Start ho raha hai...")
    chrome_options = Options()
    chrome_options.add_argument("--headless") # Bina screen ke background mein chalne ke liye
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        driver.get("https://1wwooz.com")
        print("🌍 Website khul gayi, Monitoring chalu hai...")
        time.sleep(10)
        
        last_val = ""
        blue_count = 0 # 1.50x Sniper ke liye
        double_paisa_count = 0 # 2.00x Sniper ke liye

        while True:
            try:
                # Frame switch for 1win Aviator
                driver.switch_to.frame(0)
                elements = driver.find_elements(By.CLASS_NAME, "bubble-multiplier")
                
                if elements:
                    current_val = elements.text.strip()
                    if current_val != last_val:
                        val = float(current_val.replace('x', ''))
                        
                        # Telegram History Message
                        bot.send_message(CHAT_ID, f"🏁 Round: {current_val}")

                        # --- 📈 1.50x Sniper Alert (Safe Strategy) ---
                        if val < 1.30: blue_count += 1
                        else: blue_count = 0
                        if blue_count >= 6:
                            bot.send_message(CHAT_ID, "⚠️ SAFE SNIPER ALERT: 1.50x Target round aane wala hai! 🚀")
                            blue_count = 0

                        # --- 🔥 2.00x Sniper Alert (Paisa Double Strategy) ---
                        # Logic: Jab lagatar 4 round 1.20x ke niche hon, toh recovery badi aati hai
                        if val < 1.20: double_paisa_count += 1
                        else: double_paisa_count = 0
                        if double_paisa_count >= 4:
                            bot.send_message(CHAT_ID, "🔥 GOLDEN SNIPER: 2.00x Target round aane wala hai! Paisa Double Mode 💰")
                            double_paisa_count = 0

                        last_val = current_val
                
                driver.switch_to.default_content()
                time.sleep(5)
            except:
                time.sleep(5)
                continue
    except Exception as e:
        print(f"❌ Error: {e}")
        driver.quit()

if __name__ == "__main__":
    start_server_bot()
