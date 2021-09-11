from tkinter import *
# radioButton : 하나만 선택하는 것
root = Tk()
root.title("tkinter GUI")

Label(root,text = "메뉴를 선택하세요").pack()

burger_var = IntVar()
btn_burger1 = Radiobutton(root, text = "햄버거", value = 1, variable = burger_var)
btn_burger2 = Radiobutton(root, text = "치즈버거", value = 2, variable = burger_var)
btn_burger3 = Radiobutton(root, text = "치킨버거", value = 3, variable = burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

drink_var = StringVar()

Label(root, text = "음료를 선택하세요").pack()

btn_drink1 = Radiobutton(root, text = "콜라", value = '콜라', variable = drink_var)
btn_drink2 = Radiobutton(root, text = "사이다", value = '사이다', variable = drink_var)
btn_drink3 = Radiobutton(root, text = "물", value = '물', variable = drink_var)

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()

def btncmd():
    print(burger_var.get())     # 선택된 라디오 항목의 값(value)을 출력
    print(drink_var.get())

btn = Button(root,text ='클릭', command = btncmd)
btn.pack()

root.mainloop()