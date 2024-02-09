import tkinter as tk
from tkinter import simpledialog
import tkinter.messagebox as tkmsg
import modules.chat as chat
from modules.data import history, users
from modules.frames import mainmenu

def send_message(*args):
    if history.curChat == -1:
        tkmsg.showinfo('未选择对话', '请先选择一个对话！')
        return

    chat_history.configure(state = "normal")

    message = message_entry.get()
    chat_history.insert(tk.END, 'User:' + message + "\n")
    message_entry.delete(0, tk.END)

    ans = chat.uploadMsg(history.saves[history.curChat]['content'], message)
    chat_history.insert(tk.END, 'Bot:' + ans + "\n")
    message_entry.delete(0, tk.END)

    history.saves[history.curChat]['content'].extend([message, ans])

    chat_history.configure(state = "disabled")

def switch_conversation(event):
    chat_history.configure(state = "normal")

    selection = conversation_list.curselection()
    if selection:
        history.curChat = selection[0]
        # index = selection[0]
        # conversation = conversation_list.get(index)
        chat_history.delete(1.0, tk.END)
        chat_history.insert(tk.END, chat.getPrefixedText(history.saves[history.curChat]['content']))
        # chat_history.insert(tk.END, "Conversation with " + conversation + "\n")

    chat_history.configure(state = "disabled")

def add_conversation():
    name = simpledialog.askstring("Add Chat", "Enter chat name:")
    if name:
        history.saves.append({
            'name': name,
            'content': []
        })
        conversation_list.insert(tk.END, name)

def delConversation():
    conversation_list.delete(history.curChat)
    history.saves.pop(history.curChat)
    history.curChat = -1

def onClosing():
    history.saveChat(users.curUser)
    mainFrame.destroy()

def init():
    for ch in history.saves:
        conversation_list.insert(tk.END, ch['name'])

mainFrame = tk.Tk()
mainFrame.title("Chat")
mainFrame.protocol('WM_DELETE_WINDOW', onClosing)

conversation_frame = tk.Frame(mainFrame)
conversation_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand = True)

conversation_list = tk.Listbox(conversation_frame)
conversation_list.bind("<<ListboxSelect>>", switch_conversation)
conversation_list.pack(fill = tk.BOTH, expand = True)

addDelFrame = tk.Frame(conversation_frame)
addDelFrame.pack(fill = tk.X)
add_button = tk.Button(addDelFrame, text="Add", command=add_conversation)
add_button.pack(fill = tk.X, side = tk.LEFT, expand = True)
delButton = tk.Button(addDelFrame, text = 'Del', command = delConversation)
delButton.pack(fill = tk.X, side = tk.RIGHT, expand = True)

chat_frame = tk.Frame(mainFrame)
chat_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

logFrame = tk.Frame(chat_frame)
logFrame.pack(side = tk.TOP, fill = tk.BOTH, expand = True)

chat_history = tk.Text(logFrame)
chat_history.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
chat_history.configure(state = 'disabled')

scrollbar = tk.Scrollbar(logFrame, command=chat_history.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

chat_history.configure(yscrollcommand=scrollbar.set)

entryFrame = tk.Frame(chat_frame)
entryFrame.pack(side = tk.BOTTOM, fill = tk.X)

message_entry = tk.Entry(entryFrame)
message_entry.bind('<Return>', send_message)
message_entry.pack(side = tk.LEFT, fill = tk.X, expand = True)

send_button = tk.Button(entryFrame, text="Send", command=send_message)
send_button.pack(side = tk.RIGHT)

mainmenu.getMenu(mainFrame)