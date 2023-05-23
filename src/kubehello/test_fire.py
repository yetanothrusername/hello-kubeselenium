from selenium import webdriver

# Configure Firefox WebDriver options
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--headless")  # Run in headless mode (without GUI)

# Specify the Selenium hub URL
hub_url = "http://selenium-hub:4444/wd/hub"

# Create a Firefox WebDriver instance
driver = webdriver.Remote(command_executor=hub_url, desired_capabilities=webdriver.DesiredCapabilities.FIREFOX, options=firefox_options)

# Test scenario
driver.get("https://www.example.com")
print("Page title:", driver.title)

# Quit the WebDriver session
driver.quit()
