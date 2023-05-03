from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

event_times = driver.find_elements(By.CSS_SELECTOR,
                                   ".event-widget time")
# for time in event_times:
#     print(time.text)

event_names = driver.find_elements(By.CSS_SELECTOR,
                                   ".event-widget li a")
# for event in event_names:
#     print(event.text)

events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }

print(events)

driver.quit()
