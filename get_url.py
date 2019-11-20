"""CHƯA XONG"""

from selenium import webdriver
from tqdm import tqdm
from time import sleep
from random import randint, shuffle


driver = webdriver.Chrome('./chromedriver')

categories_link = open('./categories.txt').read().split()
root_url = 'https://www.lazada.vn/ta-dung-cu-ve-sinh/'


f = open('./url.txt', 'a', encoding='utf-8')
for cate_link in categories_link:
	page_list = list(range(1, 50))
	shuffle(page_list)
	j=0
	for i in page_list:
		page_url = cate_link + '?page=' + str(i)
		try:
			if j % 5 == 0:
				driver.get('https://www.lazada.vn/')
				sleep(20)
				
			driver.get(page_url)
			div_list_products = driver.find_elements_by_xpath('//div[@class="c2prKC"]')
			for div in div_list_products:
				a_tag = div.find_element_by_tag_name('a')
				link = a_tag.get_attribute('href')
				f.write(str(link) + '\n')
		except:
			print(page_url)
		sleep(randint(30, 60))
		j+=1

driver.close()
