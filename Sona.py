from os import system,remove
from platform import machine
import os
system('git pull')
#exit('security updating...')
try:remove('RMXXD.so')
except:pass
if machine()=='aarch64':
    system('curl -L https://github.com/FARABI-XD/.../raw/main/RMXXD.so -o RMXXD.so')
    import nox
else:
    print(' [=] Your Device Not Support ')
