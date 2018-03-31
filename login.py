import sys

from selenium import webdriver


driver = webdriver.Firefox()

try: 
	driver.get("https://nac.nitk.ac.in:8090/")
except:
	sys.exit(0)

username = driver.find_element_by_name("username")
username.clear()

password = driver.find_element_by_name("password")
password.clear()

username.send_keys("staff")
password.send_keys("staff")

driver.find_element_by_id("loginbutton").click()

print "Logged In."

driver.close()