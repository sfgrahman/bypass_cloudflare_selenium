from selenium import webdriver
from selenium_stealth import stealth
from time import sleep

# Step 2: Change browser properties
# create a ChromeOptions object
options = webdriver.ChromeOptions()

# run in headless mode
options.add_argument("--headless")

# disable the AutomationControlled feature of Blink rendering engine
options.add_argument("--disable-blink-features=AutomationControlled")

# create a driver instance
driver = webdriver.Chrome(options=options)
# Disable WebDriver flag

driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")



# Execute Cloudflare's challenge script

driver.execute_script("return navigator.language")
# enable stealth mode and set extra parameters
#stealth(driver)

# navigate to the target site
driver.get("https://www.scrapingcourse.com/cloudflare-challenge")

# wait for the interstitial page to load
sleep(10)

# take a screenshot of the current page and save it
driver.save_screenshot("cloudflare-challenge-st.png")

# close browser
driver.quit()
