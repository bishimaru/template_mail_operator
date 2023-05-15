from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import widget.pcmax 


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
    if url =="https://happymail.co.jp/sp/app/html/mbmenu.php":
        name = driver.find_element(By.CLASS_NAME, "ds_user_display_name")
        window_handle_list[name.text + "ハッピー"] = handle_array[i]
    elif url.startswith("https://pcmax.jp"):
        widget.pcmax.login(driver, wait)
        name = driver.find_elements(By.CLASS_NAME, "p_img")
        print(999)
        print(len(name))
        if len(name):
            # 次の要素を取得
            next_element = name[0].find_element(By.XPATH, value="following-sibling::*[1]")
            print(next_element.text)
            window_handle_list[next_element.text + "PCMAX"] = handle_array[i]
    
for mykey, myvalue in window_handle_list.items():
    print(mykey + ":" + myvalue)
driver.quit()
