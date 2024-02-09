import tkinter as tk
import scenechoose

def show_choice():
    choice1 = choice.get()
    print(choice1)
    print('aaa')
    if choice1 == 1:
        print('You selected Scene 1')
        # 跳转到 Scene 1 的功能
        root.destroy()
    elif choice1 == 2:
        print('You selected Scene 2')
        # 跳转到 Scene 2 的功能
        root.destroy()
    elif choice1 == 3:
        print('You selected Scene 2')
        # 跳转到 Scene 3 的功能
        root.destroy()
    elif choice1 == 4:
        print('You selected Scene 2')
        # 跳转到 Scene 4 的功能
        root.destroy()
    scenechoose.scechose(choice1)

root = tk.Tk()
root.title('Task Scene Selection')

choice = tk.IntVar()

tk.Label(root, text='Choose a task scene:').pack()

option1 = tk.Radiobutton(root, text='Scene 1 商店', variable=choice, value=1, command=show_choice)
option2 = tk.Radiobutton(root, text='Scene 2 餐厅', variable=choice, value=2, command=show_choice)
option3 = tk.Radiobutton(root, text='Scene 3 医院', variable=choice, value=3, command=show_choice)
option4 = tk.Radiobutton(root, text='Scene 4 教室', variable=choice, value=4, command=show_choice)

option1.pack()
option2.pack()
option3.pack()
option4.pack()

root.mainloop()
