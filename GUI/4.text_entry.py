from tkinter import *

root = Tk()
root.title("tkinter GUI")

txt = Text(root, width = 30, height = 5)    # 글자 쓰고 지울 수 있는 Text 만듦 메모장 비슷함 (여러 줄)
txt.pack()
txt.insert(END, "글자 입력하세요")

e = Entry(root, width = 30)         # 한 줄만
e.pack()
e.insert(0,"한 줄만 입력")

def btncmd():
    # 내용 출력
    print(txt.get("1.0",END))   # 1은 첫번째 라인, 0은 0번째 column
    print(e.get())

    # 내용 삭제
    txt.delete("1.0",END)
    e.delete(0,END)


button = Button(root, text = "클릭", command = btncmd)
button.pack()

root.mainloop()