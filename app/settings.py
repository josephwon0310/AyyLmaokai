'''
helper file to tell flask where to look for files, when using uploaded files
'''

import os
# __file__ refers to the file settings.py 
APP_ROOT = os.path.dirname(os.path.abspath(__file__)) #root dir
APP_STATIC = os.path.join(APP_ROOT, 'static') #Use this

'''
Example:
import os
from settings import APP_STATIC
with open(os.path.join(APP_STATIC, 'filename')) as f:
    do something
'''