from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import widget.pcmax 
import time


options = Options()
options.add_argument('--headless')
options.add_argument("--no-sandbox")
options.add_argument("--remote-debugging-port=9222")
options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 15)

# 現在開いているウィンドウハンドルを取得
# current_window_handle = driver.current_window_handle
# print(current_window_handle)

#ウィンドウハンドル一覧
handle_array = driver.window_handles
window_handle_list = {}
print(len(handle_array))
for i in range(len(handle_array)):
    driver.switch_to.window(handle_array[i])
    url = driver.current_url
    if url.startswith("https://happymail.co.jp"):
    # if url =="https://happymail.co.jp/sp/app/html/mbmenu.php":
        driver.get("https://happymail.co.jp/sp/app/html/mbmenu.php")
        wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        time.sleep(1)  
        name = driver.find_element(By.CLASS_NAME, "ds_user_display_name")      
        window_handle_list[name.text + "ハッピー"] = handle_array[i]
        
    elif url.startswith("https://pcmax.jp"):
        widget.pcmax.login(driver, wait)
        name = driver.find_elements(By.CLASS_NAME, "p_img")
        if len(name):
            # 次の要素を取得
            next_element = name[0].find_element(By.XPATH, value="following-sibling::*[1]")
            window_handle_list[next_element.text + "PCMAX"] = handle_array[i]
    elif url.startswith("https://mail.google.com"):
        driver.get("https://mail.google.com/mail/mu")
        wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        time.sleep(1)  
        # カスタム属性の値を持つ要素をXPathで検索
        custom_value = "メニュー"
        xpath = f"//*[@aria-label='{custom_value}']"
        element = driver.find_elements(By.XPATH, value=xpath)
        if element is None:
            print("要素が見つかりません。")
        element[0].click()
        time.sleep(1) 
        # toggleaccountscallout+20 
        custom_value = "toggleaccountscallout+20"
        xpath = f"//*[@data-control-type='{custom_value}']"
        element = driver.find_elements(By.XPATH, value=xpath)
        if element is None:
            print("要素が見つかりません")
        address = element[0].text
        print(address)
        window_handle_list[address] = handle_array[i]



for mykey, myvalue in window_handle_list.items():
    print(mykey + ":" + myvalue)
driver.quit()
