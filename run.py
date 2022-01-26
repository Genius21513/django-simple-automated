import mechanicalsoup
import time

for i in range(4):
    browser = mechanicalsoup.Browser()
    page = browser.get("http://olympus.realpython.org/dice")
    tag = page.soup.select("#result")[0]
    result = tag.text
    print(f"Dice Result:{result}")
    time.sleep(10)