import datetime
from flask import Flask, render_template
from selenium import webdriver
from apscheduler.schedulers.background import BackgroundScheduler
from time import sleep
from PIL import Image
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')


def task1():
    browser = webdriver.Chrome(options=options)

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
        'tribe-events-calendar-month__multiday-event-wrapper'
    )
    # 6階の情報を取得する場合
    anchor = info_floors[0].find_element_by_class_name(
        'tribe-events-calendar-month__multiday-event-hidden-link')
    anchor.click()

    Today_6F = browser.find_element_by_id(
        'scheme-container').screenshot_as_png

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

    Today_7F = browser.find_element_by_id(
        'scheme-container').screenshot_as_png

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
    Today_8F = browser.find_element_by_id(
        'scheme-container').screenshot_as_png

    # ファイルに保存
    with open('./img/Today_8F.png', 'wb') as f:
        f.write(Today_8F)

    # # 終了処理
    sleep(1)
    browser.quit()


    img = Image.open('./img/Today_6F.png')
    img_crop = img.crop((260, 25, 410, 260))
    img_crop2 = img_crop.convert('RGB')
    img_resize = img_crop2.resize((540, 960))
    img_resize.save('./static/img/Today_6F.jpeg')

    def add_margin(pil_img, top, right, bottom, left, color):
        # 元画像の幅,高さを取得
        width, height = pil_img.size
        # 余白追加後の画像の幅、高さを算出
        new_width = width + right + left
        new_height = height + top + bottom
        # 上で算出した幅、高さで無地の画像を作成
        result = Image.new(pil_img.mode, (new_width, new_height), color)
        # 元の画像を無地の画像に貼り付ける
        result.paste(pil_img, (left, top))
        return result
    img = Image.open('./img/Today_7F.png')
    img = add_margin(img, 425, 0, 0, 0, (128, 0, 64))
    img_rotate = img.rotate(90)
    img_crop = img_rotate.crop((470, 10, 610, 625))
    img_crop2 = img_crop.convert('RGB')
    img_crop2.save('./static/img/Today_7F.jpg')


    img = Image.open('./img/Today_8F.png')
    img_crop = img.crop((170, 25, 485, 340))
    img_crop2 = img_crop.convert('RGB')
    img_crop2.save('./static/img/Today_8F.jpg')

sched = BackgroundScheduler(daemon=True)
sched.add_job(task1, 'interval', seconds=5)
sched.start()

app = Flask(__name__)


@app.route('/')
def index():
    t_delta = datetime.timedelta(hours=9)
    JST = datetime.timezone(t_delta, 'JST')
    now = datetime.datetime.now(JST)
    d = now.date().strftime('%Y/%m/%d')
    return render_template('index.html', day=d)


@app.route("/Today_6F")
def Today_6F():
    img_path = './static/img/Today_6F.jpeg'
    return render_template('Today_6F.html', img_6F=img_path)


@app.route("/Today_7F")
def Today_7F():
    img_path = './static/img/Today_7F.jpg'
    return render_template('Today_7F.html', img_7F=img_path)


@app.route("/Today_8F")
def Today_8F():
    img_path = './static/img/Today_8F.jpg'
    return render_template('Today_8F.html', img_8F=img_path)
