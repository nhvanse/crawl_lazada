from selenium import webdriver
import csv
from tqdm import tqdm
from time import sleep
from random import randint

# vi tri link dau va vi tri link cuoi
begin, end = 403, 8000


def parse(url, driver):
    driver.get(url)
    try:
        while True:
            comments_element = driver.find_element_by_class_name('mod-reviews')
            items = comments_element.find_elements_by_class_name('item')
            for item in items:
                text = item.find_element_by_class_name('content').text
                stars = item.find_elements_by_xpath('./div[@class="top"]/div/img[@src="//laz-img-cdn.alicdn.com/tfs/TB19ZvEgfDH8KJjy1XcXXcpdXXa-64-64.png"]')
                
                num_stars = len(stars)
                if text == None or text == '' or num_stars > 5 or num_stars < 1:
                    continue
                    
                data = {
                    'stars': str(num_stars),
                    'text': text
                }
                yield data
            
            nextbutton = driver.find_element_by_xpath('//button[@class="next-btn next-btn-normal next-btn-medium next-pagination-item next"]')
            
            dis = nextbutton.get_attribute('disabled')
            if dis:
                break
            driver.execute_script("arguments[0].click();", nextbutton)
            sleep(3)

    except Exception as e:
        pass
        

    
url_list = open('./url_list.txt', 'r', encoding='utf-8').read().split('\n')
driver = webdriver.Chrome(executable_path='./chromedriver')
 
with open('./data.csv','a', encoding='utf-8') as csvfile:
    fieldnames=['stars','text']
    writer=csv.DictWriter(csvfile,fieldnames=fieldnames,quoting=csv.QUOTE_ALL) 
    j=1
    for url in tqdm(url_list[begin-1:end]):

        try:
            comments_generator = parse(url, driver)
            for data in comments_generator:
                writer.writerow(data)
            
            if j % 5 == 0:
                driver.get('https://www.lazada.vn/')
                sleep(randint(15,25))
        except Exception as e:
            pass
        sleep(randint(5,20))
        j+=1
        


driver.close()
