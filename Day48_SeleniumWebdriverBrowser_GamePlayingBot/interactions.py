from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# chrome_driver_path = "C:\Development\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)

chromedriver_autoinstaller.install()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(), options=options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_element(By.ID,
#                                     "articlecount")
# print(article_count.text)
# article_count.click()

encyclopedia = driver.find_element(By.LINK_TEXT,
                                   "encyclopedia")
# encyclopedia.click()

search = driver.find_element(By.NAME,
                             "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)


