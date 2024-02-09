# 导入Tkinter库
import tkinter as tk
import requests
#import api_inter

def scechose(chose_s):
    # 定义一个函数，用于发送消息
    def send():

        url = "https://api.tigerbot.com/bot-service/ai_service/gpt"

        API_KEY = "0b7987694beee019aa0738bffa6a2c7db463b12d7be28984598e7146b98bd16d"

        headers = {
            'Authorization': 'Bearer ' + API_KEY
        }
        # 定义请求体
        payload = {
            "text": "",
            "modelVersion": "tigerbot-7b-sft"
        }
        message = entry.get()
        #    # 清空输入框
        entry.delete(0, tk.END)
        payload["text"] = message
        # 发送post请求
        response = requests.post(url, headers = headers, json = payload)
        response_text = response.json().get('response')
        response_data = response.json().get('data')
        response_result = response_data.get('result')
        print(f"TIgerBot:{response.text}")
        # 在文本框中显示用户的输入
        chat_history.insert(tk.END, f'You:{message}\n')
        #    # 在文本框中显示接收的消息
        chat_history.insert(tk.END, f'Bot: {response_result}\n')

    root = tk.Tk()
    root.geometry("720x540+100+100")
    # 创建一个文本框，用于显示聊天记录
    chat_history = tk.Text(root)
    chat_history.config(width = 700, height = 35)
    chat_history.pack()
    # 设置文本框随窗口放缩
    chat_history.pack(expand = True)
    # 创建一个输入框，用于输入消息
    entry = tk.Entry(root)
    entry.config(width = 700)
    entry.pack()

    # 设置输出框随窗口放缩
    entry.pack(expand = True)
    # 设置窗口可以放缩
    root.resizable(True, True)
    # 设置窗口的第0列和第0行可以放缩
    root.grid_columnconfigure(0, weight = 1)
    root.grid_rowconfigure(0, weight = 1)
    button = tk.Button(root, text = "发送", command = send)
    # button.pack(side=tk.BOTTOM)
    button.pack()

    if chose_s == 1:
        # 设置窗口标题
        root.title("商店场景")
        chat_history.insert(tk.END,f'现在您正在商店中\n')

    elif chose_s == 2:
        root.title("餐厅场景")
        chat_history.insert(tk.END,f'现在您正在餐厅中\n')

    elif chose_s == 3:
        root.title("医院场景")
        chat_history.insert(tk.END,f'现在您正在医院中\n')
    elif chose_s == 4:
        root.title("教室场景")
        chat_history.insert(tk.END,f'现在您正在教室中\n')

    # 启动主循环，显示窗口并等待用户操作
    root.mainloop()