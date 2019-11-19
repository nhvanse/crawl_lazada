"""CHƯA XONG"""

from selenium import webdriver
from tqdm import tqdm

driver = webdriver.Chrome('./chromedriver')
root_url = 'https://pages.lazada.vn/wow/i/vn/LandingPage/lazmall?wh_weex=true&wx_navbar_transparent=true&data_prefetch=true&scm=1003.4.icms-zebra-5000379-2586391.OTHER_5979073296_4798943'

driver.get(root_url)
