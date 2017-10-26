import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from __builtin__ import classmethod


class SearchTests(unittest.TestCase):
    @classmethod
    def setUp(cls):
        # create a new Firefox session """
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # navigate to the application home page """
        cls.driver.get('http://demo-store.seleniumacademy.com/')
        cls.driver.title

    def test_search_by_category(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()

        # enter search keyword and submit
        self.search_field.send_keys("phones")
        self.search_field.submit()

        # get all the anchor elements which have product names displayed currently on result page
        # using find_elements_by_xpath method

        products = self.driver.find_elements_by_xpath("//h2[@class='product-name']/a")
        self.assertEqual(3, len(products))


    def test_search_by_name(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()

        # enter search keyword and submit
        self.search_field.send_keys("phones")
        self.search_field.submit()

        # get all the anchor elements which have product names displayed currently on result page
        # using find_elements_by_xpath method

        products = self.driver.find_elements_by_xpath("//h2[@class='product-name']/a")
        self.assertEqual(3, len(products))


    def test_search_field(self):
        # check search field exists on Home page
        self.assertTrue(self.is_element_present(By.NAME, 'q'))


    def test_language_option(self):
        # check language options dropdown on Home page
        self.assertTrue(self.is_element_present(By.ID, "select-language"))


    def test_shopping_cart_empty_message(self):
        # check content of My Shopping Cart block on Home page
        shopping_cart_icon = self.driver.\
            find_element_by_css_selector('div.header-minicart span.icon')
        shopping_cart_icon.click()

        shopping_cart_status = self.driver.\
            find_element_by_css_selector('p.empty').text
        self.assertEqual('You have no items in your shopping cart.',
                          shopping_cart_status)

        close_button = self.driver.\
            find_element_by_css_selector('div.minicart-wrapper a.close')
        close_button.click()



    @classmethod
    def tearDown(cls):
        # close the browser window
        cls.driver.quit()

    def is_element_present(self, how, what):
        """
        Utility method to check presence of an element on page
        :params how: By locator type
        :params what: locator value
        """
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e:
            return False
        return True


if __name__ == '__main__':
    unittest.main(verbosity=2)