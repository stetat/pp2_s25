import os

path = '/Users/darhanazibek/Desktop/pp2_s25/lab6/del.py'

if os.access(path, os.R_OK) and os.path.exists(path):
    os.remove(path)