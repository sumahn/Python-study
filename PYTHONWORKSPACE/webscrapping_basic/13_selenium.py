from selenium import webdriver
import random 
# browser = webdriver.Chrome("D:/study/PYTHONWORKSPACE/chromedriver.exe")
# browser.get("http://naver.com")

# elem = browser.find_element_by_class_name("link_login") # 찾고자 하는 클래스 이름의 element 반환
# elem.click() # 클릭 attribute를 갖는다면 클릭 가능

# browser.back() # 뒤로 돌아가기
# browser.forward() # 앞으로 
# browser.refresh() # 새로고침

# elem = browser.find_element_by_id("query") # id로 찾기

# from selenium.webdriver.common.keys import Keys
# elem.send_keys("나도코딩") # 키 값을 주어진 elem에 보낼 수 있다.
# elem.send_keys(Keys.ENTER) # ENTER 키 실행 보내기 

import time
browser = webdriver.Chrome("PYTHONWORKSPACE/webscrapping_basic/chromedriver.exe")
browser.maximize_window()
# 1. 네이버 이동 
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. id, pw 입력
time.sleep(random.uniform(1,3))
my_id = input("아이디를 입력하세요>>> ")
my_pw = input("패스워드를 입력하세요>>> ")
# browser.find_element_by_id("id").send_keys(my_id)
# browser.find_element_by_id("pw").send_keys(my_pw)
time.sleep(random.uniform(1,3))

# 4. 로그인 버튼 클릭
# browser.find_element_by_id("log.login").click()

# 5. id를 새로 입력
# browser.back()
input_js = ' \
        document.getElementById("id").value = "{id}"; \
        document.getElementById("pw").value = "{pw}"; \
    '.format(id = my_id, pw = my_pw)

time.sleep(random.uniform(1,3))
browser.execute_script(input_js)
time.sleep(random.uniform(1,3))
browser.find_element_by_id("log.login").click()
# browser.find_element_by_id("id").clear()
# browser.find_element_by_id("id").send_keys("cktnaks1")

# 6. html 정보 출력
# print(browser.page_source)

# 7. browser 종료
# browser.close() # 현재 탭만 종료 
# browser.quit() # 전체 브라우저 종료
