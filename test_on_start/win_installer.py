import os
import time

class Installer:
    def install():
        os.system("color 02")
        time.sleep(0)
    def check_venv():
        venv = os.path.exists('venv')
        print("venv exist is:", venv)
        if venv == True:
             pass
        else:
            os.system("python -m venv venv")
    def check_env():
            a = os.path.isfile("DRFapi/DRFapi/.env")
            print('env exists is ', a)
            if a == True:
                pass
            else:
                env = open("DRFapi/DRFapi/.env","a")
                info = open(".envexample", "r")
                text = info.read()
                env.write(text)
                env.close()
                info.close()
    def set_venv():
        os.system('call "venv\\Scripts\\activate.bat"')
        print("SETVENNV")
        os.system("echo 'venv'")
        print(os.getcwd())
    def read_req():
        os.system("pip install -r requirements.txt")

Installer.install()
Installer.check_venv()
Installer.set_venv()
Installer.check_env()
