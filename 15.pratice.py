from tkinter import *

tk = Tk()
tk.title("제목 없음 - window 메모장")

text = Text(tk)
text.pack(fill = 'both', expand = True)

def open_file():
    f = open('mynote.txt','r')
    while True:
        line = f.readline()
        text.insert(0,line)
        if not line: break
    f.close()


def save_file():
    f = open('mynote.txt','w')
    f.write(text.get("1.0",END))
    f.close()
# frame = Frame(tk)
# frame.pack(fill = 'both')

menu = Menu(text)
menu_file = Menu(tk,tearoff = 0)
menu_file.add_command(label = "열기", command = open_file)
menu_file.add_command(label = "저장", command = save_file)
menu_file.add_command(label = "끝내기", command = tk.quit())
menu.add_cascade(label = "파일", menu = menu_file)

menu.add_cascade(label = "편집", menu = menu_file)
menu.add_cascade(label = "서식", menu = menu_file)
menu.add_cascade(label = "보기", menu = menu_file)
menu.add_cascade(label = "도움말", menu = menu_file)

# scrollbar = Scrollbar(frame)
# scrollbar.pack(side = "right", fill = "y")

tk.config(menu = menu)
tk.mainloop()