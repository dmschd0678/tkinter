from tkinter import *

root = Tk()
root.title("tkinter GUI")

def create_new_file():
    print("새 파일을 만듭니다.")

# File Menu
menu = Menu(root)
menu_file = Menu(menu, tearoff = 0)
menu_file.add_command(label = "New File", command = create_new_file)
menu_file.add_command(label = "New Window")
menu_file.add_separator()       # 구분선
menu_file.add_command(label = "Open File...")
menu_file.add_separator()       # 구분선
menu_file.add_command(label = "Save All", state = "disable") # 비활성화
menu_file.add_command(label = "Exit",command = root.quit())
menu.add_cascade(label = "File", menu = menu_file)

# Edit Meny
menu.add_cascade(label = "Edit")

# Language 메뉴 추가 (radio 버튼)
menu_lang = Menu(menu,tearoff = 0)
menu_lang.add_radiobutton(label = "Python")
menu_lang.add_radiobutton(label = "Java")
menu_lang.add_radiobutton(label = "C++")
menu.add_cascade(label = "Language",menu = menu_lang)

# View 메뉴
menu_view = Menu(menu,tearoff = 0)
menu_view.add_checkbutton(label = "Show Minimap")
menu.add_cascade(label = "View", menu = menu_view)

root.config(menu = menu)
root.mainloop()