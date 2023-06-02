import os

class Env_er:
    def __init__(self):
        pass
    def check_venv(self):
        a = os.path.isfile("DRFapi/DRFapi/.env")
        if a == True:
            pass
        else:
            env = open("DRFapi/DRFapi/.env","a")
            info = open(".envexample", "r")
            text = info.read()
            env.write(text)
            env.close()
            info.close()

Env_er().check_venv()