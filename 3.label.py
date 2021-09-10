from tkinter import *

root = Tk()
root.title("tkinter GUI")

label1 = Label(root, text = "Hi!")      # 글씨만 보임
label1.pack()

photo = PhotoImage(file = 'img.png')    # 사진만 보임
label2 = Label(root, image = photo)
label2.pack()

def change():
    label1.config(text = "Bye!")    # label1의 내용을 변경
    global photo2
    photo2 = PhotoImage(file = 'img2.png')  # label2의 이미지를 변경
    label2.config(image = photo2)   # 변경 - config

button = Button(root, text = "클릭", command = change)
button.pack()

root.mainloop()