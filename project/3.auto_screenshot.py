from  PIL import ImageGrab
import time

time.sleep(5)

for i in range(1,11):
    img = ImageGrab.grab()  # 현재 스크린을 이미지로 가져옴
    img.save("Image{}.png".format(i))   # 파일로 저장
    time.sleep(2)
