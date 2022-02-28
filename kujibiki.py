from selenium import webdriver
from time import sleep

url = "https://lot.tsite.jp/#/detail2/cccmk_yxm_005"
driver = webdriver.Chrome('./chromedriver.exe')
#ブラウザを開く
driver.get(url)

sleep(1)

#「ログインしてくじを引く！」ボタンをクリックする
kuji_login = driver.find_element_by_xpath("//*[@id=\"app\"]/app-button-top/main/article/section/div[3]/div/span/img")
kuji_login.click()

sleep(1)

#「ログイン」ボタンをクリックする
login_button = driver.find_element_by_xpath("//*[@id=\"contentInner\"]/div[2]/div[2]/div[2]/input")
login_button.click()

#Yahoo!iD、パスワードを入力する
# your_id = "あなたのID"
# your_password = "あなたのパスワード"
your_id = "cibicibi2017"
your_password = "jeGgRb2ARjSIcEhHyK/5"
#idを入力
id_input = driver.find_element_by_xpath("//*[@id=\"username\"]")
id_input.send_keys(your_id)
#「次へ」をクリック
next = driver.find_element_by_xpath("//*[@id=\"btnNext\"]")
next.click()

sleep(1)

#パスワードを入力する
password_input = driver.find_element_by_xpath("//*[@id=\"passwd\"]")
password_input.send_keys(your_password)
#「ログイン」をクリックする
login = driver.find_element_by_xpath("//*[@id=\"btnSubmit\"]")
login.click()

sleep(1)

#「くじを引く！」をクリックする
#もしTカードを登録していなければ、登録する(上手くいかなかったら手動で押してください……)
cur_url = driver.current_url
if "https://lot.tsite.jp/#/detail2/cccmk_yxm_005" in cur_url:
    get_kuji = driver.find_element_by_xpath("//*[@id=\"app\"]/app-button-top/main/article/section/div[3]/div/span/img")
    get_kuji.click()
else:
    try:
        #「登録する」のチェックを外す
        print(cur_url)
        checkbox = driver.find_element_by_xpath("//*[@id=\"tmallmail\"]")
        checkbox.click()
        # 「登録する」を押す
        register = driver.find_element_by_xpath("//*[@id=\"form1\"]/div/input")
        register.click()
        #くじを引く
        get_kuji = driver.find_element_by_xpath("//*[@id=\"app\"]/app-button-top/main/article/section/div[3]/div/span/img")
        get_kuji.click()
    except:
        print("error")
        driver.quit()

sleep(10)

driver.quit()
