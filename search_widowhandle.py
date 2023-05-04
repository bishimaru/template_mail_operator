from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


options = Options()
options.add_argument('--headless')
options.add_argument("--no-sandbox")
options.add_argument("--remote-debugging-port=9222")
options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service, options=options)

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
    elif url == "https://pcmax.jp/pcm/index.php" or url == "https://pcmax.jp/pcm/member.php":
        name = driver.find_element(By.XPATH, "//*[@id='sp_footer']/a[5]/span[2]")
        window_handle_list[name.text + "PCMAX"] = handle_array[i]
    
for mykey, myvalue in window_handle_list.items():
    print(mykey + ":" + myvalue)
driver.quit()
