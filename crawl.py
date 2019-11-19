from selenium import webdriver
import csv
from tqdm import tqdm

def parse(url, driver):
    driver.get(url)
    comments_element = driver.find_element_by_class_name('mod-reviews')
    items = comments_element.find_elements_by_class_name('item')
    for item in items:
        text = item.find_element_by_class_name('content').text
        stars = item.find_elements_by_xpath('./div[@class="top"]/div/img[@src="//laz-img-cdn.alicdn.com/tfs/TB19ZvEgfDH8KJjy1XcXXcpdXXa-64-64.png"]')
        num_stars = len(stars)
        data = {
            'stars': str(num_stars),
            'text': text
        }
        yield data
    
    
url_list = open('./url_list.txt', 'r', encoding='utf-8')
driver = webdriver.Chrome(executable_path='./chromedriver')
 
with open('./data.csv','w', encoding='utf-8') as csvfile:
    fieldnames=['stars','text']
    writer=csv.DictWriter(csvfile,fieldnames=fieldnames,quoting=csv.QUOTE_ALL)
    writer.writeheader()    
    
    for url in tqdm(url_list):
        try:
            comments_generator = parse(url, driver)
            for data in comments_generator:
                writer.writerow(data)
        except:
            print('Error while parsing link: '+ url)
        
driver.close()
