from tkinter import *
import tkinter.ttk as ttk
import time

root = Tk()
root.title("tkinter GUI")

#progressbar = ttk.Progressbar(root, maximum = 100, mode = "indeterminate") # 왔다 갔다 함
# progressbar = ttk.Progressbar(root, maximum = 100, mode = "determinate")    # 채워졌다가 초기화 됨
# progressbar.start(10)   # 10ms 마다 움직임
# progressbar.pack()
#
#
# def btncmd():
#     progressbar.stop()  # 작동 중지
# btn = Button(root,text ='중지', command = btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum = 100, length = 150, variable = p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(101):
        time.sleep(0.01)

        p_var2.set(i)   # 프로그레스 바의 값 설정
        progressbar2.update()   # 업데이트 이거 안 하면 다 끝나고 바뀜
        print(p_var2.get())

btn = Button(root,text ='시작', command = btncmd2)
btn.pack()

root.mainloop()