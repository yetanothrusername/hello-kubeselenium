from selenium import webdriver

# Configure Chrome WebDriver options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # Run in headless mode (without GUI)

# Specify the Selenium hub URL
hub_url = "http://selenium-hub:4444/wd/hub"

# Create a Chrome WebDriver instance
driver = webdriver.Remote(command_executor=hub_url, desired_capabilities=webdriver.DesiredCapabilities.CHROME, options=chrome_options)

# Test scenario
driver.get("https://www.example.com")
print("Page title:", driver.title)

# Quit the WebDriver session
driver.quit()
