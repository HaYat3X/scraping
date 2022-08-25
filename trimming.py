from PIL import Image
import schedule
import time


def task():
    img_6F = Image.open('./static/img/Today_6F.png')
    success_6F = img_6F.crop((270, 25, 410, 350))
    success_6F.save('./img/6F.png')
    print('変換しました')


schedule.every(2).seconds.do(task)
while True:
    schedule.run_pending()
    time.sleep(1)
