import os

if os.access('/Users/darhanazibek/Desktop/pp2_s25', os.F_OK):
    print("The directory exists")

if os.access('/Users/darhanazibek/Desktop/pp2_s25', os.R_OK):
    print("The directory is readable")

if os.access('/Users/darhanazibek/Desktop/pp2_s25', os.W_OK):
    print("The directory is writable")

if os.access('/Users/darhanazibek/Desktop/pp2_s25', os.X_OK):
    print("The directory is executable")

