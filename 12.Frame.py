from tkinter import *

root = Tk()
root.title("tkinter GUI")

Label(root, text = "메뉴를 선택해주세요").pack(side = "top") # side : 위치 설정

Button(root, text= "주문하기").pack(side = "bottom")
# 햄버거 프레임
frame_buger = Frame(root, relief = "solid",bd = 1)  # relief : 경계선 설정, bd : 테두리 두께
frame_buger.pack(side = "left", fill = "both",expand = True)    # fill = 채우기, expand : 요구되지 않은 공간도 채우기

Button(frame_buger,text = "햄버거").pack()
Button(frame_buger,text = "치즈버거").pack()
Button(frame_buger,text = "치킨버거").pack()

# 음료 프레임
frame_drink = LabelFrame(root, text = "음료")
frame_drink.pack(side = "right", fill = "both", expand = True)
Button(frame_drink, text = "콜라").pack()
Button(frame_drink, text = "사이다").pack()

root.mainloop()