import sys
from selenium import webdriver


driver = webdriver.Firefox()

try: 
	driver.get("http://10.10.54.4:8090/")
except:
	sys.exit(0)

print driver.title
print "Logged in"


#username field
inputElement = driver.find_element_by_name("username")
#Replace "staff" with your username/registration number
inputElement.send_keys("staff")

#password field
inputElement = driver.find_element_by_name("password")
#Replace "staff" with your password
inputElement.send_keys("staff")


driver.find_element_by_name("btnSubmit").click()

driver.close()
