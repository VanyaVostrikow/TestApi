import os
import subprocess
class Venv_check:
    def check():
        venv = os.path.exists('venv')
        if venv is True:
            print(1)
        else:
            print(0)
            
check = Venv_check.check()