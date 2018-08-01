import unittest
import HTMLTestRunner
import os,sys
from searchtests import SearchTests
from homepagetests import HomePageTests

# get the directory path to output report file
dir = os.getcwd()
print dir

# get all tests from SearchProductTest and HomePageTest class
search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTests)
homepage_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTests)


# create a test suite combining search_test and home_page_test
smoke_tests = unittest.TestSuite([homepage_tests, search_tests])


# open the report file
outfile = open(dir + '\SmokeTestReport.html', 'w')

# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(
    stream = outfile,
    title = 'Test Report',
    description = 'Smoke Tests'
)

# run the suite using TestRunner
#unittest.TextTestRunner(verbosity=2).run(smoke_tests)

runner.run(smoke_tests)