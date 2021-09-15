from tkinter import *

root = Tk()
root.title("tkinter GUI")

listbox = Listbox(root, selectmode = 'extended', height = 0) # height 숫자만큼 보여줌 0은 다 보여줌
listbox.insert(0,"사과")
listbox.insert(1,"딸기")
listbox.insert(2,"바나나")
listbox.insert(END,"수박")
listbox.insert(END,"포도")
listbox.pack()

def btncmd():
    #listbox.delete(END) # 맨 뒤에 항목 삭제
    listbox.delete(0)    # 맨 앞에 항목 삭제

    # 갯수 확인
    print(listbox.size(), "개")

    # 항목 확인 (시작, 끝)
    print(listbox.get(0,2)) # 첫번째부터 3번째 항목까지 출력

    # 선택된 항목 확인 (index 값으로 반환)
    print(listbox.curselection())

btn = Button(root, text = "클릭", command = btncmd)
btn.pack()

root.mainloop()