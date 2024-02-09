import pickle as pkl
import os

curChat = -1
saves = []

def saveChat(username):
    with open('./saves/' + username, 'wb') as f:
        pkl.dump(saves, f)

def loadChat(username):
    global saves
    if not os.path.exists('./saves/' + username):
        return
    with open('./saves/' + username, 'rb') as f:
        saves = pkl.load(f)

