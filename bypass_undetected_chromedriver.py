import undetected_chromedriver as uc
from time import sleep

if __name__ == "__main__":

    # instantiate a Chrome browser
    driver = uc.Chrome(
        use_subprocess=False,
        #headless=True,
    )

    # visit the target page
    driver.get("https://www.scrapingcourse.com/cloudflare-challenge")

    # wait for the interstitial page to load
    sleep(20)

    # take a screenshot of the current page and save it
    driver.save_screenshot("cloudflare-challenge.png")

    # close the browser
    driver.quit()