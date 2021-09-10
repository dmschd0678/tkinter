from tkinter import *

root = Tk()
root.title("tkinter GUI")

button1 = Button(root, text = "버튼1")
button1.pack()

button2 = Button(root, padx = 5, pady = 10, text = "버튼2222222222222")       # 버튼의 크기가 변함
button2.pack()

button3 = Button(root, padx = 10, pady = 5, text = "버튼3")
button3.pack()

button4 = Button(root, width = 10, height = 3, text = "버튼44444444444444")   # 크기 고정
button4.pack()

button5 = Button(root,fg = "red", bg = "yellow", text = "버튼5")          # 색 변화
button5.pack()

photo = PhotoImage(file = 'img.png')            # 사진으로 버튼 만들기
button6 = Button(root,image = photo)
button6.pack()

def btncmd():
    print("버튼이 클릭됨")

button7 = Button(root, text = "동작하는 버튼", command = btncmd)  # 이벤트
button7.pack()

root.mainloop()