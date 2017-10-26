import os
from selenium import webdriver


# get the path of chromedriver
dir = os.path.dirname(__file__)
dir = '/Users/smodak/PycharmProjects/setests'
chrome_driver_path = dir + "/chromedriver"


# create a new firefox session
#driver = webdriver.Firefox()
driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(10)
driver.maximize_window()


# navigate to the application home page
driver.get("http://demo-store.seleniumacademy.com/")

# get the search textbox
search_field = driver.find_element_by_name("q")
search_field.clear()


# enter search keyword and submit
search_field.send_keys("phones")
search_field.submit()


# get all the anchor elements which have product names displayed currently on result page using find_elements_by_xpath method
products = driver.find_elements_by_xpath("//h2[@class='product-name']/a")


# get the number of anchor elements found
print "Found " + str(len(products)) + " products:"


# iterate through each anchor element and print the text which is name of the product


for product in products:
    print product.text


# close the browser winow
driver.quit()