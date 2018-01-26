from selenium import webdriver

browser = webdriver.Chrome('C:/Users/erwin/AppData/Local/Programs/Python/Python36-32/selenium/chromedriver.exe')
browser.get('http://localhost:8000')

assert 'Django' in browser.title
