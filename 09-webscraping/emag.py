from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://www.emag.ro/#opensearch')

get_element = browser.find_element(by=By.ID, value = 'searchboxTrigger')
get_element.send_keys('telefon')      #Cu send_keys inseram ce vrem sa cautam
get_element.submit()                    #Se apasa enter cu submit

search_element = browser.find_element(by=By.CLASS_NAME, value = 'card-v2')
print(search_element.text)

for i in range(1,62):
    find_element = browser.find_element(by=By.XPATH, value = f'//*[@id="card_grid"]/div[{i}]')
    print(find_element.text)
    print('+++++++++++++++++++++++++++++')

