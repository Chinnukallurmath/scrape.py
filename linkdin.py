from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def get_linkedin_text(url):
    try:
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)

        driver.get(url)
        time.sleep(5)

        # Update the selector depending on LinkedIn layout
        post_text = driver.find_element("css selector", "div.feed-shared-update-v2__description").text
        driver.quit()
        return post_text
    except Exception as e:
        print(f"LinkedIn error: {e}")
        return None


