import tkinter as tk
import tkinter.filedialog as tkfile
import tkinter.messagebox as tkmsg
from modules.plugin import rethink, vector, image_captioning, id_select
from modules.data import users

curPlugin = -1

def getMenu(mainFrame):

    def switchRethink():

        def confirmRethink():
            rethink.curRethink = rethinkList.curselection()[0]
            if rethink.curRethink == -1:
                users.userConfigs['mode'] = 'normal'
                mainFrame.title('Chat')
            else:
                users.userConfigs['mode'] = 'rethink'
                mainFrame.title('Chat-外部文档搜索模式，该模式中模型不会记忆历史对话')
            window.destroy()

        def addRethink():
            filepath = tkfile.askopenfilename(title = '请选择JSON类型的外部数据', filetypes = [('JSON', '.json')])
            if filepath == '':
                return
            rethink.createRethink(filepath)
            rethinkList.insert(tk.END, filepath)

        def delRethink():
            curSelect = rethinkList.curselection()
            if len(curSelect) == 0:
                return
            rethink.delRethink(curSelect[0])
            rethinkList.delete(curSelect[0])

        window = tk.Tk()
        window.title('选择或添加外部数据')
        window.geometry('500x300')

        rethinkList = tk.Listbox(window)
        rethinkList.pack(expand = True, fill = tk.BOTH)
        for r in rethink.rethinks:
            rethinkList.insert(tk.END, r['name'])
        rethinkList.selection_set(rethink.curRethink + 1)

        buttonFrame = tk.Frame(window)
        buttonFrame.pack(fill = tk.X)

        confirmButton = tk.Button(buttonFrame, text = 'Confirm', command = confirmRethink)
        confirmButton.pack(fill = tk.X, side = tk.LEFT, expand = True)
        addButton = tk.Button(buttonFrame, text = "Add", command = addRethink)
        addButton.pack(fill = tk.X, side = tk.RIGHT, expand = True)
        delButton = tk.Button(buttonFrame, text = 'Del', command = delRethink)
        delButton.pack(fill = tk.X, side = tk.RIGHT, expand = True)

    def switchVector():

        filepath = tkfile.askopenfilename(title = '请选择文本类型的外部数据', filetypes = [('TXT', '.txt')])
        if filepath == '':
            return
        users.userConfigs['mode'] = 'vector'
        vector.loadDB(filepath)
        mainFrame.title('Chat-向量搜索模式，该模式中模型不会记忆历史对话')

    def switchNormal():
        users.userConfigs['mode'] = 'normal'
        mainFrame.title('Chat')

    def switchImage():
        filepath = tkfile.askopenfilename(title = '请选择一张图片', filetypes = [('图片', ['.jpg', '.jpeg', '.png'])])
        if filepath == '':
            return
        image_captioning.curImagePath = filepath
        users.userConfigs['mode'] = 'image'
        mainFrame.title('Chat-图片模式不会记忆历史对话；当前图片：' + filepath)

    def switchID(idx):
        if idx == -1:
            users.userConfigs['mode'] = 'normal'
            mainFrame.title('Chat')
        else:
            users.userConfigs['mode'] = 'id'
            mainFrame.title('Chat-当前身份：' + id_select.idText[idx])
        users.userConfigs['id'] = idx

    def switchWeb():
        users.userConfigs['mode'] = 'web'
        mainFrame.title('Chat-联机模式')

    def luxunFT():
        users.userConfigs['mode'] = 'luxun'
        mainFrame.title('Chat-和鲁迅对话')

    def noFT():
        users.userConfigs['mode'] = 'normal'
        mainFrame.title('Chat')

    def jhzFT():
        users.userConfigs['mode'] = 'jhz'
        mainFrame.title('Chat-用jhz的风格续写诗')

    def storeMode():
        tkmsg.showinfo('说明', '该模式使用外部数据，在特定场景下检索相应信息并回答用户问题，下面请先选择一个外部数据')

        def confirmRethink():
            rethink.curRethink = rethinkList.curselection()[0]
            if rethink.curRethink == -1:
                users.userConfigs['mode'] = 'normal'
                mainFrame.title('Chat')
            else:
                users.userConfigs['mode'] = 'store'
                mainFrame.title('Chat-商店模式')
            window.destroy()

        def addRethink():
            filepath = tkfile.askopenfilename(title = '请选择JSON类型的外部数据', filetypes = [('JSON', '.json')])
            if filepath == '':
                return
            rethink.createRethink(filepath)
            rethinkList.insert(tk.END, filepath)

        def delRethink():
            curSelect = rethinkList.curselection()
            if len(curSelect) == 0:
                return
            rethink.delRethink(curSelect[0])
            rethinkList.delete(curSelect[0])

        window = tk.Tk()
        window.title('选择或添加外部数据')
        window.geometry('500x300')

        rethinkList = tk.Listbox(window)
        rethinkList.pack(expand = True, fill = tk.BOTH)
        for r in rethink.rethinks:
            rethinkList.insert(tk.END, r['name'])
        rethinkList.selection_set(rethink.curRethink + 1)

        buttonFrame = tk.Frame(window)
        buttonFrame.pack(fill = tk.X)

        confirmButton = tk.Button(buttonFrame, text = 'Confirm', command = confirmRethink)
        confirmButton.pack(fill = tk.X, side = tk.LEFT, expand = True)
        addButton = tk.Button(buttonFrame, text = "Add", command = addRethink)
        addButton.pack(fill = tk.X, side = tk.RIGHT, expand = True)
        delButton = tk.Button(buttonFrame, text = 'Del', command = delRethink)
        delButton.pack(fill = tk.X, side = tk.RIGHT, expand = True)

    def libMode():
        tkmsg.showinfo('说明', '该模式使用外部数据，在特定场景下检索相应信息并回答用户问题，下面请先选择一个外部数据')

        def confirmRethink():
            rethink.curRethink = rethinkList.curselection()[0]
            if rethink.curRethink == -1:
                users.userConfigs['mode'] = 'normal'
                mainFrame.title('Chat')
            else:
                users.userConfigs['mode'] = 'lib'
                mainFrame.title('Chat-图书馆模式')
            window.destroy()

        def addRethink():
            filepath = tkfile.askopenfilename(title = '请选择JSON类型的外部数据', filetypes = [('JSON', '.json')])
            if filepath == '':
                return
            rethink.createRethink(filepath)
            rethinkList.insert(tk.END, filepath)

        def delRethink():
            curSelect = rethinkList.curselection()
            if len(curSelect) == 0:
                return
            rethink.delRethink(curSelect[0])
            rethinkList.delete(curSelect[0])

        window = tk.Tk()
        window.title('选择或添加外部数据')
        window.geometry('500x300')

        rethinkList = tk.Listbox(window)
        rethinkList.pack(expand = True, fill = tk.BOTH)
        for r in rethink.rethinks:
            rethinkList.insert(tk.END, r['name'])
        rethinkList.selection_set(rethink.curRethink + 1)

        buttonFrame = tk.Frame(window)
        buttonFrame.pack(fill = tk.X)

        confirmButton = tk.Button(buttonFrame, text = 'Confirm', command = confirmRethink)
        confirmButton.pack(fill = tk.X, side = tk.LEFT, expand = True)
        addButton = tk.Button(buttonFrame, text = "Add", command = addRethink)
        addButton.pack(fill = tk.X, side = tk.RIGHT, expand = True)
        delButton = tk.Button(buttonFrame, text = 'Del', command = delRethink)
        delButton.pack(fill = tk.X, side = tk.RIGHT, expand = True)

    menubar = tk.Menu(mainFrame)

    pluginMenu = tk.Menu(menubar, tearoff = 0)
    pluginMenu.add_command(label = '无插件', command = switchNormal)
    pluginMenu.add_command(label = '外部文档搜索(JSON文件)', command = switchRethink)
    pluginMenu.add_command(label = '向量搜索(文本文档)', command = switchVector)
    pluginMenu.add_command(label = '图片描述', command = switchImage)
    pluginMenu.add_command(label = '联机搜索', command = switchWeb)
    menubar.add_cascade(label = '插件', menu = pluginMenu)

    idMenu = tk.Menu(menubar, tearoff = 0)
    idMenu.add_command(label = '无身份', command = lambda: switchID(-1))
    idMenu.add_command(label = '中译英', command = lambda: switchID(0))
    idMenu.add_command(label = '女朋友', command = lambda: switchID(1))
    idMenu.add_command(label = '餐厅服务员', command = lambda: switchID(2))
    idMenu.add_command(label = '歌手', command = lambda: switchID(3))
    idMenu.add_command(label = '作家', command = lambda: switchID(4))
    idMenu.add_command(label = 'CV教授', command = lambda: switchID(5))
    menubar.add_cascade(label = '身份选择', menu = idMenu)

    ftMenu = tk.Menu(menubar, tearoff = 0)
    ftMenu.add_command(label = '无', command = noFT)
    ftMenu.add_command(label = '鲁迅', command = luxunFT)
    ftMenu.add_command(label = '某组员', command = jhzFT)
    menubar.add_cascade(label = '数字分身', menu = ftMenu)

    taskMenu = tk.Menu(menubar, tearoff = 0)
    taskMenu.add_command(label = '退出', command = switchNormal)
    taskMenu.add_command(label = '商店购买商品', command = storeMode)
    taskMenu.add_command(label = '图书馆借书', command = libMode)
    menubar.add_cascade(label = '专用模式', menu = taskMenu)

    mainFrame.config(menu = menubar)