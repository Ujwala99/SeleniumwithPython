import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestGoogleSearch(unittest.TestCase):

    def setUp(self):
        # Initialize the Chrome WebDriver
        self.driver = webdriver.Chrome()  # Assumes ChromeDriver is in PATH
        self.driver.implicitly_wait(10)  # Wait for elements to load

    def test_search_google(self):
        # Navigate to Google
        self.driver.get("https://www.google.com")
        
        # Verify that the title contains "Google"
        self.assertIn("Google", self.driver.title)

        # Find the search box using its name attribute value
        search_box = self.driver.find_element(By.NAME, "q")
        
        # Enter a search term
        search_box.send_keys("Selenium WebDriver")
        
        # Find and click the Google Search button
        search_box.submit()  # You can also find and click the button if needed

        # Wait until the results are loaded
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "search"))  # Wait for search results to appear
        )

        # Verify that the search results page contains the search term
        self.assertIn("Selenium WebDriver", self.driver.page_source)

    def tearDown(self):
        # Close the browser after the test
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
