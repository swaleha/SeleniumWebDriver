from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

path = '/usr/local/bin/chromedriver' # location of chromedriver
website = 'https://web.whatsapp.com' # whatsapp.web URL
phone_number =  # phone number to send image
photo_path = '/Users/.../Documents/image.jpeg' #location of image

# Initiates browser and opens the URL specified
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1: 9222")
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)
driver.maximize_window()
time.sleep(30)

# Searches for the desired phone number
search_phone = driver.find_element(by='xpath',value='//div[@title="Search input textbox"]')
search_phone.send_keys(phone_number)
time.sleep(2)

# Finds the Search results and clicks on first result returned
contacts = driver.find_elements(by='xpath', value='//div[@aria-label="Search results."]//div[@data-testid="cell-frame-container"]')
contacts[-1].click()   # picks last element in the list (This represents first search results returned)
time.sleep(2)

# Attach button is clicked
attach_button = driver.find_element(by='xpath', value='//span[@data-testid="clip"]')
attach_button.click()
time.sleep(2)

# Media button to attach pictures/photos specifically is clicked
attach_image_button = driver.find_element(by='xpath', value='//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
attach_image_button.send_keys(photo_path)
time.sleep(2)

# Send button is clicked
send_image_button = driver.find_element(by='xpath', value='//div[@data-testid="drawer-middle"]//span[@data-testid="send"]')
send_image_button.click()
time.sleep(5)

driver.quit()