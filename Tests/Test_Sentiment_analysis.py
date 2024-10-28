import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from transformers import pipeline

class TestSentimentAnalysis(unittest.TestCase):

    def setUp(self):
        # Initialize the Chrome WebDriver
        self.driver = webdriver.Chrome()  # Assumes ChromeDriver is in PATH
        self.driver.implicitly_wait(10)  # Wait for elements to load

        # Load sentiment analysis model
        self.sentiment_analyzer = pipeline("sentiment-analysis")

    def test_sentiment_analysis(self):
        # Navigate to a sentiment analysis tool (replace with your own URL if needed)
        self.driver.get("https://your-sentiment-analysis-web-app.com")  # Replace with your app URL

        # Sample input for sentiment analysis
        sample_text = "I love coding with Python and Selenium!"
        
        # Enter the sample text into the input field
        input_box = self.driver.find_element(By.NAME, "input")  # Adjust the name as per your web app
        input_box.send_keys(sample_text)

        # Submit the form (or click the analyze button)
        submit_button = self.driver.find_element(By.NAME, "submit")  # Adjust the name as per your web app
        submit_button.click()

        # Analyze sentiment with AI
        result = self.sentiment_analyzer(sample_text)

        # Verify that the result matches the expected sentiment
        expected_sentiment = result[0]['label']
        
        # Wait for the result to be displayed on the page
        self.driver.implicitly_wait(5)  # Wait for the result to appear

        # Find the result on the page
        output_element = self.driver.find_element(By.ID, "output")  # Adjust the ID as per your web app
        actual_result = output_element.text
        
        # Print the results
        print(f"Expected Sentiment: {expected_sentiment}")
        print(f"Actual Sentiment from the web app: {actual_result}")

        # Assert that the actual result matches the expected sentiment
        self.assertIn(expected_sentiment, actual_result)

    def tearDown(self):
        # Close the browser after the test
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
