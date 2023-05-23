from selenium import webdriver

# Specify the path to the Internet Explorer WebDriver executable
ie_driver_path = "path/to/IEDriverServer.exe"

# Specify the Selenium hub URL
hub_url = "http://selenium-hub:4444/wd/hub"

# Create an Internet Explorer WebDriver instance
driver = webdriver.Remote(command_executor=hub_url, desired_capabilities=webdriver.DesiredCapabilities.INTERNETEXPLORER, executable_path=ie_driver_path)

# Test scenario
driver.get("https://www.example.com")
print("Page title:", driver.title)

# Quit the WebDriver session
driver.quit()
