from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from datetime import datetime as dt
import time
import csv


class gmaps:
	def __init__(self, email, password, dir):
		self.email = email
		self.password = password
		self.dir = dir
		chrome_options = webdriver.ChromeOptions()
		prefs = {"profile.default_content_setting_values.notifications" : 2}
		chrome_options.add_experimental_option("prefs",prefs)
		chrome_options.add_argument("user-data-dir="+self.dir)
		self.driver = webdriver.Chrome(chrome_options=chrome_options)
		self.action = ActionChains(self.driver)

	def wheel_element(self, element, deltaY = 120, offsetX = 0, offsetY = 0):
		error = element._parent.execute_script("""
			var element = arguments[0];
			var deltaY = arguments[1];
			var box = element.getBoundingClientRect();
			var clientX = box.left + (arguments[2] || box.width / 2);
			var clientY = box.top + (arguments[3] || box.height / 2);
			var target = element.ownerDocument.elementFromPoint(clientX, clientY);

			for (var e = target; e; e = e.parentElement) {
				if (e === element) {
					target.dispatchEvent(new MouseEvent('mouseover', {view: window, bubbles: true, cancelable: true, clientX: clientX, clientY: clientY}));
					target.dispatchEvent(new MouseEvent('mousemove', {view: window, bubbles: true, cancelable: true, clientX: clientX, clientY: clientY}));
					target.dispatchEvent(new WheelEvent('wheel',     {view: window, bubbles: true, cancelable: true, clientX: clientX, clientY: clientY, deltaY: deltaY}));
					return;
				}
			}    
			return "Element is not interactable";
			""", element, deltaY, offsetX, offsetY)
		if error:
			raise WebDriverException(error)


	# def login(self):
	# 	driver = self.driver
	# 	driver.get('http://facebook.com')
	# 	driver.find_elements_by_xpath("//input[@name='email']")[0].send_keys(self.email)
	# 	driver.find_elements_by_xpath("//input[@name='pass']")[0].send_keys(self.password)
	# 	driver.find_elements_by_xpath("//input[@value='Login']")[0].click()

	# def add_group_member(self, group_id):
	# 	driver = self.driver
	# 	self.group = group_id
	# 	driver.get('https://www.facebook.com/groups/'+self.group+'/local_members/')
	# 	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	# 	time.sleep(2)
	# 	e_members = driver.find_elements_by_xpath("//button[contains(@class, 'FriendRequestAdd addButton') and not(contains(@class,'selected')) and not(contains(@class , 'hidden_elem'))]")
	# 	print(len(e_members))
	# 	time.sleep(2)
	# 	n = 0
	# 	mem = []
	# 	for e in e_members:
	# 		link_member = e.find_element_by_xpath("../../../../../../../ a").get_attribute("href")
	# 		print(e,link_member)
	# 		mem.append(link_member.replace('www', 'm'))
	# 		n +=  1

	# 	print(mem)
	# 	e = 0
	# 	while e < len(mem):
	# 		print(e, mem[e])
	# 		driver.get(mem[e])
	# 		time.sleep(5)
	# 		driver.find_element_by_xpath("//div[contains(@data-sigil, 'add-friend')]").click()
	# 		print("added friend and wait 10 sec")
	# 		time.sleep(10)
	# 		driver.back()
	# 		time.sleep(3)
	# 		e += 1

	# def like_beranda_posts(self):
	# 	driver = self.driver
	# 	driver.get('https://facebook.com')
	# 	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	# 	time.sleep(3)
	# 	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	# 	print('get like')
	# 	likes = driver.find_elements_by_xpath("//a[contains(@data-testid, 'UFI2ReactionLink')]")
	# 	print(len(likes))

	# 	for like in likes:
	# 		print(like)
	# 		ActionChains(driver).move_to_element(like).perform()
	# 		like.click()
	# 		print('klikked')
	# 		time.sleep(10)

	#def collect_place(self, keywords, last_crawl):
	# 	driver = self.driver
	# 	id="searchboxinput"
	# 	# print(group_id)
	# 	data = []
	# 	data.append(["Timestamp", "By", "Title", "Price", "Desc"])
	# 	for group_id in groups_id:
	# 		driver.get('https://www.facebook.com/groups/'+group_id)
	# 		posts =  driver.find_elements_by_xpath("//div[@class='_5pcr userContentWrapper']")
	# 		i = 0
	# 		while len(posts) < 250:
	# 			i += 1
	# 			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	# 			time.sleep(2)
	# 			posts =  driver.find_elements_by_xpath("//div[@class='_5pcr userContentWrapper']")
	# 			print(len(posts))
	# 			if i > 25:
	# 				break

			
	# 		print(len(posts))
			
	# 		i = 1
	# 		for post in posts:
	# 			ActionChains(driver).move_to_element(post).perform()
	# 			try:
	# 				by = post.find_element_by_css_selector("span a").get_attribute("title")
	# 				timestamp = post.find_element_by_class_name("timestamp").get_attribute("title")
	# 			except Exception as e:
	# 				continue

	# 			try:
	# 				price = post.find_element_by_css_selector("div.qzhwtbm6.knvmm38d span span span").text
	# 			except Exception as e:
	# 				price = ""	

	# 			try:
	# 				title = post.find_element_by_css_selector("div.qzhwtbm6.knvmm38d span div span span").text
	# 			except Exception as e:
	# 				title = ""

	# 			try:
	# 				desc = post.find_element_by_css_selector("div.userContent div p").text
	# 				print('div p')
	# 			except Exception as e:
	# 				desc = ""

	# 			if desc == "":
	# 				try:	
	# 					desc = post.find_element_by_css_selector("div.userContent div span:nth-child(2) span").text
	# 					print('span')
	# 				except Exception as e:
	# 					continue
					
	# 			try:
	# 				# print(timestamp, type(timestamp))
	# 				post_time = dt.strptime(timestamp, '%d/%m/%y %H.%M')
	# 				if post_time > last_crawl:
	# 					print(post_time, last_crawl, post_time < last_crawl)
	# 					print(i, by, title, price, timestamp)
	# 					print(desc.replace("\n", " "))
	# 					# 	print('old')
	# 					# print(post_time)
	# 					print('\n')
	# 					data.append([timestamp, by, title, price, desc.replace("\n", " ")])
	# 					i += 1
	# 				else:
	# 					continue

	# 			except Exception as e:
	# 				print(e)
	# 			# print(data)
	# 	print(data)
	# 	current_time = str(dt.now().strftime("%m_%d_%y_%I_%M_%p"))
	# 	# current_time = ""
	# 	with open('data_'+current_time+'.csv', 'w', newline='') as file:
	# 		writer = csv.writer(file, delimiter=';')
	# 		writer.writerows(data)

	# 	# print(data)

	def collect_place(self, keywords):
		d = self.driver
		d.get('https://maps.google.com')
		# self.wheel_element(elm, 120)
		d.find_element_by_id('searchboxinput').send_keys(keywords)
		d.find_element_by_id('searchbox-searchbutton').click()
		time.sleep(10)
		d.find_element_by_xpath('//div[@data-result-index="2"]').click()
		time.sleep(10)
		# d.find_element_by_css_selector('div.section-layout-root div:nth-child(48) div div button span').click()
		# time.sleep(10)
		# r_e= d.find_elements_by_xpath('//div[@class="section-review ripple-container"]')

		# ActionChains(d).move_to_element(di[l-1]).perform()
		# time.sleep(5)
		# tab_elm = d.


		
		# actions =  ActionChains(d)
		# for x in range(1, 70):
		# 	actions = actions.send_keys(Keys.TAB)
		# 	actions.perform()
		# 	time.sleep(1)

		# di= d.find_elements_by_xpath('//div[@class="section-divider"]')
		# l = len(di)
		# print(l, di)



# last_crawl = dt.strptime('02/29/20, 12:00 AM', '%m/%d/%y, %I:%M %p')
gm = gmaps('ecosy.corp@gmail.com', 'EcosyCorp001', 'ecosy')
keywords = 'toko komputer malang raya'
gm.collect_place(keywords)


