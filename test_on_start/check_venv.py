import os
import subprocess
class Venv_check:
    def check():
        venv = os.path.exists('venv')
        return venv
            
check = Venv_check.check()