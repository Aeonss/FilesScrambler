import os
from tkinter import *
import tkinter, tkinter.filedialog
import random
import string

nameLength = 8

def scramble():
    
    # Get the source folder from user
    root = Tk()
    root.directory = tkinter.filedialog.askdirectory(title = 'Please select a directory with your source files to scramble')
    srcFolder = root.directory
    os.chdir(srcFolder)
	
	# Rename each file to a random string of letters and numbers
    for i, file in enumerate(os.listdir(srcFolder)):
        os.chdir(srcFolder)
        fileName, fileExtention = os.path.splitext(file)
        fileName = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(nameLength))
        newName = f'{fileName}{fileExtention}'
        os.rename(file, newName)

if __name__ == '__main__':
	scramble()