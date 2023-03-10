from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())

driver.get('https://www.linkedin.com/')
driver.maximize_window()
driver.quit()
