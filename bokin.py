from selenium import webdriver
from time import sleep

url = "https://tsite.jp/donation/index.pl"
driver = webdriver.Chrome('./chromedriver.exe')
#ブラウザを開く
driver.get(url)

#ログイン
login = driver.find_element_by_xpath("//*[@id=\"user-nav\"]/ul/li[2]/a/span")
login.click()

#「ログイン」ボタンをクリックする
login_button = driver.find_element_by_xpath("//*[@id=\"contentInner\"]/div[2]/div[2]/div[2]/input")
login_button.click()

sleep(1)

#Yahoo!iD、パスワードを入力する
# your_id = "あなたのID"
# your_password = "あなたのパスワード"
# id,passwordは環境変数に設定する
your_id = ""
your_password = ""
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

#募金ページに移動する
bokin_url = "https://tsite.jp/donation/index.pl?xpg=PCTC0202&bokin_id=507" #任意の募金ページ
driver.get(bokin_url)
#「寄付する」ボタンをクリックする
bokin_button = driver.find_element_by_xpath("//*[@id=\"charity_button\"]/div/a/img")
bokin_button.click()

sleep(0.5)

#パスワードの再入力
password_input = driver.find_element_by_xpath("//*[@id=\"passwd\"]")
password_input.send_keys(your_password)
#「ログイン」をクリックする
login = driver.find_element_by_xpath("//*[@id=\"btnSubmit\"]")
login.click()

#募金額を入力する
money_box = driver.find_element_by_xpath("//*[@id=\"charity_input_point\"]/input")
money_box.send_keys(1) #募金額はここで変えられます。デフォルトでは１円
sleep(0.5)
#「次へ」をクリックする
next = driver.find_element_by_xpath("//*[@id=\"charity_button\"]/div[1]/input")
next.click()
sleep(0.5)
#「確定」をクリックする
confirm = driver.find_element_by_xpath("//*[@id=\"charity_button\"]/div[1]/input[1]")
confirm.click()

sleep(1)

driver.quit()
