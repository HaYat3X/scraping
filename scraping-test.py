# モジュールにインポート
from selenium import webdriver
from time import sleep
import datetime
import schedule
import time


# def task():
# MacとWindowsに注意
# Chromeを使う
browser = webdriver.Chrome()

# URLアクセス
url = 'https://braingate.matrix.jp/internet/'
browser.get(url)

# 自動ログインシステム
# ユーザー名に指定の値を代入
UserName = browser.find_element_by_id("log")
UserName.send_keys('intern4')

# パスワードに指定の値を代入
UserPassword = browser.find_element_by_id('pwd')
UserPassword.send_keys('intern4')

# ログインボタンを押す
Btn = browser.find_element_by_class_name('buttons')
Btn.click()

# スクショサイズ調整
w = browser.execute_script("return document.body.scrollWidth;")
h = browser.execute_script("return document.body.scrollHeight;")
browser.set_window_size(w, h)

date = datetime.datetime.now()

# actions = ActionChains(browser)
id = 'tribe-events-calendar-day-' + \
    str(date.year) + '-0' + str(date.month) + '-' + str(date.day)

# 日付ごとの枠を取得
cell_today = browser.find_element_by_id(id)
# 日付の枠内での各階層の要素を取得(リストで取得)
info_floors = cell_today.find_elements_by_class_name(
    'tribe-events-calendar-month__multiday-event-wrapper')
# 6階の情報を取得する場合
anchor = info_floors[0].find_element_by_class_name(
    'tribe-events-calendar-month__multiday-event-hidden-link')
anchor.click()

Today_6F = browser.find_element_by_id('scheme-container').screenshot_as_png

# ファイルに保存
with open('./img/Today_6F.png', 'wb') as f:
    f.write(Today_6F)

# 座席予約の画面へ戻る
home_redirect1 = 'https://braingate.matrix.jp/internet/events/'
browser.get(home_redirect1)

id = 'tribe-events-calendar-day-' + \
    str(date.year) + '-0' + str(date.month) + '-' + str(date.day)

# 日付ごとの枠を取得
cell_today = browser.find_element_by_id(id)
# 日付の枠内での各階層の要素を取得(リストで取得)
info_floors = cell_today.find_elements_by_class_name(
    'tribe-events-calendar-month__multiday-event-wrapper')
# 6階の情報を取得する場合
anchor = info_floors[1].find_element_by_class_name(
    'tribe-events-calendar-month__multiday-event-hidden-link')
anchor.click()

Today_7F = browser.find_element_by_id('scheme-container').screenshot_as_png

# ファイルに保存
with open('./img/Today_7F.png', 'wb') as f:
    f.write(Today_7F)

    # 座席予約の画面へ戻る
home_redirect2 = 'https://braingate.matrix.jp/internet/events/'
browser.get(home_redirect2)

id = 'tribe-events-calendar-day-' + \
    str(date.year) + '-0' + str(date.month) + '-' + str(date.day)

# 日付ごとの枠を取得
cell_today = browser.find_element_by_id(id)
# 日付の枠内での各階層の要素を取得(リストで取得)
info_floors = cell_today.find_elements_by_class_name(
    'tribe-events-calendar-month__multiday-event-wrapper')
# 6階の情報を取得する場合
anchor = info_floors[2].find_element_by_class_name(
    'tribe-events-calendar-month__multiday-event-hidden-link')
anchor.click()

# スクリーンショット取得(このパスに工夫が必要)
Today_8F = browser.find_element_by_id('scheme-container').screenshot_as_png

# ファイルに保存
with open('./img/Today_8F.png', 'wb') as f:
    f.write(Today_8F)

    # # 終了処理
sleep(1)
browser.quit()


# 10秒ごとに実行しています。
# schedule.every(5).seconds.do(task)
# while True:
#     schedule.run_pending()
#     print('待機中です')
#     time.sleep(1)
