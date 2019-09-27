#-------------------------------imports--------------------------
import shutil, os
from pathlib import Path
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfiles,askopenfile, askdirectory, askopenfilename

#setting Tkinter window
root = Tk()
Title = root.title( "Move It")

#------------------------------functions----------------------------
#--Opener's--
def OpenFile():
    name = askopenfilename(initialdir="P:",filetypes =(("Text File", "*.txt"),("Python File", "*.py"), ("Word File", "*.docx"),("All Files","*.*")),title = "Choose a file.")
    print(name)
    return name
#FolderOpener
def OpenFolder():
    directory = filedialog.askdirectory()
    print(directory)
    return directory
#SaveToDirectory
def saveTo():
    saveDirectory = filedialog.askdirectory()
    print(saveDirectory)
    return saveDirectory

#--MoveFunctions--
def MoveFile():
    OFile = OpenFile()
    S = saveTo()
    shutil.move(OFile, S)

def MoveFolder():
    OFolder = OpenFolder()
    S = saveTo()
    shutil.move(OFolder, S)

def backUpFile():
    OFile = OpenFile()
    S = saveTo()
    shutil.copy(OFile, S)

def backUpFolder():
    OFolder = OpenFolder()
    S = saveTo()
    shutil.copytree(OFolder,OFolder+"_copy")#copy directory
    shutil.move(OFolder+"_copy", S)#then move the new copied directory
#-----------------------------------Labels----------------------------
intro = Label(root, text = "Welcome to the simple file manager!\n Use the buttons to move or backup files/folders to")
intro.grid(column=0, row=0)
warning = Label(root, text = "*Two windows will open one after the other*\n*1st window to open = Selected file*\n *2nd window to open= the file you want to move to*", foreground= "red")
warning.grid(column=0, row=1)
#-----------------------------------Buttons----------------------------
#MoveFolderButton
Button= ttk.Button(root, text = "Move Folder", command = MoveFolder)
Button.grid(column=0, row=2)
#MoveFileButton
fileButton = ttk.Button(root, text = "Move File", command = MoveFile)
fileButton.grid(column=1, row=2)
#BackupFolderButton
moveButton = ttk.Button(root, text = "Backup Folder", command = backUpFolder)
moveButton.grid(column=0, row=4)
#BackupFileButton
toButton = ttk.Button(root, text = "Backup File", command = backUpFile)
toButton.grid(column=1, row=4)

root.mainloop()