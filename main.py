from modules.frames import login
import os

if __name__ == '__main__':
    os.environ['OPENAI_API_KEY'] = '*'
    login.window.mainloop()
