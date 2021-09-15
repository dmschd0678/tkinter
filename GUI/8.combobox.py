from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("tkinter GUI")

values = [str(i) + "일" for i in range(1,32)]

# 선택 창에 글을 쓸 수가 있음
combobox = ttk.Combobox(root, height = 5, values = values)  # height = ? : ? 의 갯수만큼 값을 보여줌
combobox.pack()
combobox.set("카드 결제일") #최초 목록 제목 설정, 버튼 클릭을 통한 설정

# 못 쓰게 하는 법
readonly_combobox = ttk.Combobox(root, height = 10, values = values, state = "readonly")
readonly_combobox.current(0)    # 0번째 인덱스 값 선택
readonly_combobox.pack()

def btncmd():
    print(combobox.get())

btn = Button(root,text ='선택', command = btncmd)
btn.pack()

root.mainloop()