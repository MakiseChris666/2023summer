
id = {
    'none': -1,
    'translator': 0,
    'girlfriend': 1,
    'waiter': 2,
    'singer': 3,
    'writer': 4,
    'cv prof': 5
}

idText = ['中译英', '女朋友', '餐厅服务员', '歌手', '作家', 'CV教授']

def id_select(options,content):
    """
    options:身份选项
    content:用户发送的对话内容
    返回值：字符串——用于发送给tigerbot
    """

    if type(options) == str:
        options = id[options]

    if options==0:
        #英语翻译官
        s="请将以下内容翻译成英语:{}".format(content)
        return s
    elif options==1:
        s="现在，假设你是我的女朋友，请和我对话:{}".format(content)
        return s
    elif options==2:
        s="现在，假设你是一个餐厅的服务生,请和我对话:{}".format(content)
        return s
    elif options==3:
        s="现在，假设你是一个歌手，请和我对话:{}".format(content)
        return s
    elif options==4:
        s="现在，假设你是一位作家，请和我对话:{}".format(content)
        return s
    elif options==5:
        s="现在，假设你是计算机领域的教授，主要研究方向是计算机视觉及图像处理,请和我对话:{}".format(content)
        return s

    return content

def getInstruction(option, first = False):

    if type(option) == str:
        option = id[option]

    if first:
        if option==0:
            return "请将以下内容翻译成英语:\n"
        elif option==1:
            return "现在，假设你是我的女朋友，请和我对话:\n"
        elif option==2:
            return "现在，假设你是一个餐厅的服务生,请和我对话:\n"
        elif option==3:
            return "现在，假设你是一个歌手，请和我对话:\n"
        elif option==4:
            return "现在，假设你是一位作家，请和我对话:\n"
        elif option==5:
            return "现在，假设你是计算机领域的教授，主要研究方向是计算机视觉及图像处理,请和我对话:\n"
    else:
        if option == 0:
            return "请将以下内容翻译成英语:\n"
        elif option == 1:
            return "以上是用户和他的女朋友之间的一段对话，其中用户的话带有“User:”前缀，用户的女朋友的话带有“Bot:”前缀。" +\
                '现在，假设你是用户的女朋友，请回答用户的以下问题，请直接回答问题，不做修饰，不要重复上文，也不要加上前缀：\n'
        elif option == 2:
            return "以上是用户和餐厅服务员之间的一段对话，其中用户的话带有“User:”前缀，餐厅服务员的话带有“Bot:”前缀。" + \
                '现在，假设你是该餐厅服务员，请回答用户的以下问题，请直接回答问题，不做修饰，不要重复上文，也不要加上前缀：\n'
        elif option == 3:
            return "以上是用户和一位歌手之间的一段对话，其中用户的话带有“User:”前缀，歌手的话带有“Bot:”前缀。" + \
                '现在，假设你是这位歌手，请回答用户的以下问题，请直接回答问题，不做修饰，不要重复上文，也不要加上前缀：\n'
        elif option == 4:
            return "以上是用户和一位作者之间的一段对话，其中用户的话带有“User:”前缀，作者的话带有“Bot:”前缀。" +\
                '现在，假设你是这位作者，请回答用户的以下问题，请直接回答问题，不做修饰，不要重复上文，也不要加上前缀：\n'
        elif option == 5:
            return "以上是用户和一位主要研究方向是计算机视觉及图像处理的计算机教授之间的一段对话，其中用户的话带有“User:”前缀，计算机教授的话带有“Bot:”前缀。" +\
                '现在，假设你是这位计算机教授，请回答用户的以下问题，请直接回答问题，不做修饰，不要重复上文，也不要加上前缀：\n'