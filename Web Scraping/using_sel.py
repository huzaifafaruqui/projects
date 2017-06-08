from selenium import webdriver
import os
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup



driver = webdriver.Chrome(os.path.join(os.getcwd(), 'chromedriver'))

url = ''  #URL hidden for privacy
driver.get(url)


#Login
#user input username password
element = driver.find_element_by_name('username')
element.send_keys(username)
element2 = driver.find_element_by_name("currentPassword")

element2.send_keys(password)
login_attempt = driver.find_element_by_xpath("//*[@type='submit']")
login_attempt.click()

desired_url = ''  //Redirect URL after login
WebDriverWait(driver, 50).until(
        lambda driver: driver.current_url == desired_url)

n = int(raw_input())
url2 = '' #common url
for i in range(1,n):
	try:
		driver.get(url2+str(i))

		html = driver.page_source
		soup = BeautifulSoup(html,'html.parser')
		for script in soup(["script", "style"]):
			script.extract()    # rip it out

		# get text
		text = soup.get_text()

		# break into lines and remove leading and trailing space on each
		lines = (line.strip() for line in text.splitlines())
		# break multi-headlines into a line each
		chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
		# drop blank lines
		text = '\n'.join(chunk for chunk in chunks if chunk)
		with open(str(i),'w') as f:
			f.write(text)
	except:
		pass
driver.quit()
			