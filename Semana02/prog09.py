import os
from datetime import datetime

os.chdir('usr/desktop')

for dirpath,dirnames,filenames in os.walk('/user/desktop'):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:',filenames)
    print()
