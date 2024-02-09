import pickle as pkl
import os

_users = {}
curUser = ''
userConfigs = {
    'mode': 'normal',
    'model': 'tiger',
    'id': -1,
    'instr': 0
}

def addUser(name, pwd):
    if name == '':
        return False, '用户名不能为空！'
    if pwd == '':
        return False, '密码不能为空！'
    if name in _users:
        return False, '用户名已被使用！'
    _users[name] = pwd
    saveUsers()
    return True, '注册成功'

def loginUser(name, pwd):
    if name not in _users:
        return False, '没有该用户！'
    if _users[name] != pwd:
        return False, '密码错误！'
    return True, '登录成功'

def saveUsers():
    with open('./users.pkl', 'wb') as f:
        pkl.dump(_users, f)

def loadUsers():
    global _users
    if not os.path.exists('./users.pkl'):
        return
    with open('./users.pkl', 'rb') as f:
        _users = pkl.load(f)