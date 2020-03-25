import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common import exceptions

comments = open("C:/Users/SKTelecom/Desktop/comments.txt", 'w' , encoding='utf-8')
browser = 'C:/Users/SKTelecom/Desktop/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(browser)

driver.get('https://news.naver.com/main/ranking/read.nhn?m_view=1&mid=etc&sid1=111&rankingType=popular_day&oid=003&aid=0008767285&date=20180822&type=1&rankingSectionId=100&rankingSeq=1')

time.sleep(3)
try:
	while True:
	      driver.find_element_by_css_selector(".u_cbox_btn_more").click()
	      time.sleep(3)

except exceptions.ElementNotVisibleException as e:
	pass

except Exception as e: # 다른 예외 발생시 확인
    pass



html = driver.page_source
bs = BeautifulSoup(html, 'html.parser')
contents = bs.find_all("span", {"class" : "u_cbox_contents"})

temp = [comments.text for comments in contents]

for i in temp:
      comments.write(str(i) + '\n')

comments.close()
