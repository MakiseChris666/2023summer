from modules.chat import tigerbot, chatgpt
import modules.data.users as users
from modules.plugin import vector, rethink, image_captioning, id_select, search, clone
import os

os.environ['OPENAI_API_KEY'] = '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'

_prefix = ['User:', 'Bot:']
def getPrefixedText(texts):
    res = ''
    for i, t in enumerate(texts):
        res += _prefix[i % 2] + t + '\n'
    return res

def uploadMsg(hist, msg):
    if users.userConfigs['mode'] == 'vector':
        msg = vector.query(msg)
        hist = []
    elif users.userConfigs['mode'] == 'rethink':
        return rethink.uploadRethink(msg)
    elif users.userConfigs['mode'] == 'image':
        msg = image_captioning.imageQuery(msg)
        hist = []
    elif users.userConfigs['mode'] == 'id':
        if not hist:
            instr = id_select.getInstruction(users.userConfigs['id'], first = True)
            msg = instr + msg
        else:
            instr = id_select.getInstruction(users.userConfigs['id'], first = False)
            hist = getPrefixedText(hist)
            return tigerbot.uploadMsg(hist, msg, instruction = instr)
    elif users.userConfigs['mode'] == 'web':
        webres = search.searchBing(msg)
        webs = ''
        for r in webres:
            webs += r + '\n'
        msg = webs + '请你根据上文回答以下问题：\n' + msg
        hist = []
    elif users.userConfigs['mode'] == 'luxun':
        return clone.luxunClone(msg)
    elif users.userConfigs['mode'] == 'jhz':
        return clone.jhzClone(msg)
    elif users.userConfigs['mode'] == 'store':
        pre = tigerbot.uploadMsg('', '你是一家商店的导购员，顾客对你说' + msg + '。请问顾客可能要买什么商品？不用解释，只输出商品名称，不输出其他任何信息。')
        pre = pre[:pre.find('。') + 1]
        sr = rethink.searchRethink(pre)
        res = '您可能需要以下商品：\n\n'
        for r in sr:
            res += r['text'] + '\n\n'
        return res
    elif users.userConfigs['mode'] == 'lib':
        pre = tigerbot.uploadMsg('',
                                 '你是一个图书馆的管理员，顾客对你说' + msg + '。请问顾客可能要借怎么样的书？不用解释，只输出对书的描述，不输出其他任何信息。')
        pre = pre[:pre.find('。') + 1]
        sr = rethink.searchRethink(pre)
        res = '您可能需要以下书籍：\n\n'
        for r in sr:
            res += r['text'] + '\n\n'
        return res

    if users.userConfigs['model'] == 'tiger':
        hist = getPrefixedText(hist)
        return tigerbot.uploadMsg(hist, msg)
    elif users.userConfigs['model'] == 'chatgpt':
        return chatgpt.uploadMsg(hist + [msg])
    return None