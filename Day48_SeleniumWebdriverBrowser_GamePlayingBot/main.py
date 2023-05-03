from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.amazon.com")
# driver.get(
#     "https://www.amazon.com/Apple-2022-10-9-inch-iPad-Wi-Fi/dp/B0BJLXMVMV/?_encoding=UTF8&pd_rd_w=pRu1a&content-id=amzn1.sym.64be5821-f651-4b0b-8dd3-4f9b884f10e5&pf_rd_p=64be5821-f651-4b0b-8dd3-4f9b884f10e5&pf_rd_r=KR36WFC43M9HFDNSE8R7&pd_rd_wg=HMcT7&pd_rd_r=83f3381c-1aae-43f3-a5c4-02e574e71fb1&ref_=pd_gw_crs_zg_bs_541966&th=1")
# price = driver.find_element(by=By.CLASS_NAME,
#                             value="a-price-whole")
# print(price)


driver.get("https://www.python.org/")
#
# documentation_link = driver.find_element(By.CSS_SELECTOR,
#                                          ".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element(By.XPATH,
#                                '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)





# driver.close()
driver.quit()
