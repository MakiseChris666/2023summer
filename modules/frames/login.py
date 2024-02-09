import tkinter as tk
from tkinter import messagebox as tkmsg
from modules.data import users, history
from modules.frames import mainframe

def register():
    ret, msg = users.addUser(nameEntry.get(), pwdEntry.get())
    if not ret:
        tkmsg.showinfo('注册失败', msg)
        return
    tkmsg.showinfo('注册成功', '现在您可以直接登录了')

def login():
    ret, msg = users.loginUser(nameEntry.get(), pwdEntry.get())
    if not ret:
        tkmsg.showinfo('登录失败', msg)
        return
    users.curUser = nameEntry.get()
    history.loadChat(users.curUser)
    window.destroy()
    mainframe.init()
    mainframe.mainFrame.deiconify()
    mainframe.mainFrame.mainloop()

mainframe.mainFrame.withdraw()

window = tk.Tk()
window.title('登录或注册')
window.geometry('300x160')

frame = tk.Frame(window)
frame.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)

tk.Label(frame, text='用户名:', font = ('', 15)).grid(row=0, column=0)
nameEntry = tk.Entry(frame)
nameEntry.grid(row=0, column=1)

tk.Label(frame, text='密码:', font = ('', 15)).grid(row=1, column=0)
pwdEntry = tk.Entry(frame, show='*')
pwdEntry.grid(row=1, column=1)

buttonFrame = tk.Frame(frame)
buttonFrame.grid(row = 2, column = 0, columnspan = 2, sticky = 'EW')

tk.Button(buttonFrame, text='登录', font = ('', 13), command=login).pack(side = tk.LEFT, fill = tk.X, expand = True)
tk.Button(buttonFrame, text='注册', font = ('', 13), command=register).pack(side = tk.RIGHT, fill = tk.X, expand = True)

if __name__ == '__main__':
    window.mainloop()
