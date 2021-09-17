import keyboard
from PIL import ImageGrab
import time

def screenshot():
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time))

keyboard.add_hotkey("F8", screenshot)   # f9 누르면 캡쳐

keyboard.wait("esc") # esc 누를 때까지 실행