from selenium import webdriver

username = "jacob_lukose"
password = "workhard123"

getdriver = ("https://www.instagram.com/accounts/login/")

driver = webdriver.PhantomJS()
driver.get(getdriver)
driver.find_element_by_name('username').send_keys(username)
driver.find_element_by_name('password').send_keys(password)
driver.find_element_by_xpath("//button[contains(.,'Log in')]").click()