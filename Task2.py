from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.alza.cz/')

cook = driver.find_element("xpath",'//*[@id="rootHtml"]/body/alza-component-head/div[6]/div/div/div[2]/a[1]')
cook.click()

cat = driver.find_element("xpath",'//*[@id="litp18890756"]/a')
cat.click()

subcat = driver.find_element("xpath",'//*[@id="ltp"]/div[3]/div/div[1]/a[6]/span')
subcat.click()

subsubcat = driver.find_element("xpath",'//*[@id="content0"]/div[1]/div[2]/div[4]/div/div[1]/a[3]/span')
subsubcat.click()

kavovar = driver.find_element("xpath",'//*[@id="ltp"]/div[3]/div/div[1]/a[3]/span')
kavovar.click()

price = driver.find_element("xpath",'//*[@id="ui-id-4"]')
price.click()

first = driver.find_element("xpath",'//*[@id="boxes"]/div[1]/div[2]/div[1]/span/div/div/a')
first.click()
driver.implicitly_wait(20)

goBack = driver.find_element("xpath",'//*[@id="varBBackButton"]')
goBack.click()

second = driver.find_element("xpath",'//*[@id="boxes"]/div[2]/div[2]/div[1]/span/div/div/a')
second.click()
driver.implicitly_wait(20)
goToCart = driver.find_element("xpath",'//*[@id="varBToBasketButton"]')
goToCart.click()

time.sleep(5)
driver.close()
