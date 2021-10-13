# Synopsis: Reminds target to drink water every 3 hours.

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from os import system
import time

print("[DRINK WATER REMINDER]\n\n")
# Message and Target info
target = '"' + input("Target: ") + '"'
messages = [
"Good Morning! Go and drink water! ʕ·ᴥ·ʔ",
"Hey! Drink a glass of water! ( ˘ ³˘)",
"Good Afternoon! Remember to hydrate! (^^)",
"Yo hi! take a sip of that h20! ;)",
"Did you drink water? UwU",
"Good night! Take a sip before sleeping. :)",
"Still awake? Hydrate and sleep! (◔‿◔)"
]

# Get chromedriver and log in
print("[LOGGING IN]\n")
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
print("[LOGGED IN]\n")
time.sleep(5)

# Different messages for respective time of the day
ind = ((time.localtime()[3])//3)-4
count = 1
while True:
    # Get local time from clock
    struct_time = time.localtime()
    current_year = struct_time[0]
    current_month = struct_time[1]
    current_day = struct_time[2]
    current_hour = struct_time[3]
    current_minute = struct_time[4]
    current_second = struct_time[5]

    # Conditions to deliver message at an interval of 3 hours
    # Starting at 9AM and not to deliver between 1AM to 9AM
    condition_1 = current_hour % 3 == 0
    condition_2 = current_minute == 0
    condition_3 = current_hour not in range(4, 9)

    if (condition_1) and (condition_2) and (condition_3):
        print("=================================")
        print(f"[MESSAGE {count}]")
        print(f"DATE: {current_day}-{current_month}-{current_year}")
        print(f"[TIME: {current_hour}hr {current_minute}min {current_second}sec]\n")
        message = messages[ind%(len(messages))]
        ind += 1
        count += 1

        # Find target
        print(f"> Finding {target}")
        x_arg = '//span[contains(@title,' + target + ')]'
        group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
        group_title.click()

        # Type and send message
        messagebutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
        print(f"> Typing Message")
        messagebutton.send_keys(message)
        sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
        print("> Sending Message")
        sendbutton.click()
        print("> Message Sent")
        print("=================================\n\n")
        
        # Sleep till some time
        time.sleep(10795)  # 10795 seconds = 2hr 59min 55sec
