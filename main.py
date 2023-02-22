from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time, random, string, datetime


if __name__ == "__main__":
    driver = webdriver.Chrome()
    url = "https://www.instagram.com/talktv_cz/?hl=cs"

    # Setup driver
    driver.get(url)
    input("Enter after logged and on talktv page")

    while True:
        if datetime.datetime.now().hour >= 19 and datetime.datetime.now().minute > 28:
            # Get canvas status
            driver.get(url)
            time.sleep(6.9)
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, "html.parser")
            story_canvas = soup.find("canvas", {"class": "_aarh"})
            print(story_canvas["style"])

            # New story uploaded
            if story_canvas["style"] == 'position: absolute; top: -9px; left: -9px; width: 168px; height: 168px;':
                random_string = (''.join(random.choice(string.ascii_lowercase) for i in range(10)))
                story_selenum_canvas = driver.find_element(By.CLASS_NAME, '_aarh')
                driver.execute_script("arguments[0].click();", story_selenum_canvas)
                time.sleep(5)
                driver.get_screenshot_as_file(F"story{random_string}.png")

                with open(f"page_source_save{random_string}.txt", "w") as page_source_save:
                    page_source_save.write(driver.page_source)
