from tkinter import *
import os

tk = Tk()
tk.title("제목 없음 - window 메모장")

file_name = 'mynote.txt'

# 파일 열기
def open_file():
    if os.path.isfile(file_name):
        f = open(file_name, 'r')
        text.delete('1.0',END)
        line = f.read()
        text.insert('1.0', line)
        f.close()

# 파일 저장
def save_file():
    f = open(file_name,'w')
    f.write(text.get("1.0",END))
    f.close()

# 메뉴 만들기
menu = Menu(tk)
# 파일 메뉴
menu_file = Menu(tk,tearoff = 0)
menu_file.add_command(label = "열기", command = open_file)
menu_file.add_command(label = "저장", command = save_file)
menu_file.add_command(label = "끝내기", command = tk.quit)
menu.add_cascade(label = "파일", menu = menu_file)

# 나머지 메뉴 기능 x
menu.add_cascade(label = "편집", menu = menu_file)
menu.add_cascade(label = "서식", menu = menu_file)
menu.add_cascade(label = "보기", menu = menu_file)
menu.add_cascade(label = "도움말", menu = menu_file)

# 스크롤 바
scrollbar = Scrollbar(tk)
scrollbar.pack(side = "right", fill = "y")

# 텍스트
text = Text(tk)
text.pack(fill = 'both', expand = True)
text.config(yscrollcommand = scrollbar.set)

scrollbar.config(command = text.yview)

tk.config(menu = menu)

tk.mainloop()