import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
#globale Variablen
#dirPath =r"./chatbilder"
#attachmentPath = dirPath + "/Attachments/"
#infoPath = dirPath + "/Info/"
#infoPicturePath = infoPath + "/Picture"

# create the root window
root = tk.Tk()
root.title('Chat-Sortierer')
root.resizable(False, False)
root.geometry('300x150')

def dateien_umbenennen(dirPath):
    
    datei = next(os.walk(dirPath))[2]
    for dateiname in datei:
        if (dateiname.split(".")[1] == "png"):
                print(dateiname)
                if "Attachment" in dateiname:
                    chat_nr = dateiname.split("_")[0].rsplit("Chat", 1)[1]
                    chat_nr = chat_nr.zfill(4) # auffüllen mit führenden Nullen
                    screenshot_nr = dateiname.split(".")[0].rsplit("Screen",1)[1].rsplit("_",1)[0]
                    screenshot_nr = screenshot_nr.zfill(4) # auffüllen mit führenden Nullen
                    attachment_nr = dateiname.split(".")[0].rsplit("Attachment",1)[1]
                    attachment_nr = attachment_nr.zfill(4) # auffüllen mit führenden Nullen
                    neuer_dateiname = "Chat" + chat_nr + "_Screen" + screenshot_nr + "_Attachment" + attachment_nr + ".png"
                    os.rename(dirPath + dateiname, dirPath + "/" + neuer_dateiname)
                    continue
                if "Info" in dateiname:
                    chat_nr = dateiname.split("_")[0].rsplit("Chat", 1)[1]
                    chat_nr = chat_nr.zfill(4) # auffüllen mit führenden Nullen
                    info_nr = dateiname.split(".")[0].rsplit("Info",1)[1]
                    info_nr = info_nr.zfill(4) # auffüllen mit führenden Nullen
                    neuer_dateiname = "Chat" + chat_nr + "_Info" + info_nr + ".png"
                    os.rename(dirPath + dateiname, dirPath + neuer_dateiname)
                    continue
                if "Picture" in dateiname:
                    chat_nr = dateiname.split("_")[0].rsplit("Chat", 1)[1]
                    chat_nr = chat_nr.zfill(4) # auffüllen mit führenden Nullen
                    picture_nr = dateiname.split(".")[0].rsplit("Picture",1)[1]
                    picture_nr = picture_nr.zfill(4) # auffüllen mit führenden Nullen
                    neuer_dateiname = "Chat" + chat_nr + "_Picture" + picture_nr + ".png"
                    os.rename(dirPath + dateiname, dirPath + neuer_dateiname)
                    continue
                else:
                    chat_nr = dateiname.split("_")[0].rsplit("t", 1)[1]
                    chat_nr = chat_nr.zfill(4) # auffüllen mit führenden Nullen
                    screenshot_nr = dateiname.split(".")[0].rsplit("n",1)[1]
                    screenshot_nr = screenshot_nr.zfill(4) # auffüllen mit führenden Nullen
                    neuer_dateiname = "Chat" + chat_nr + "_Screen_" + screenshot_nr + ".png"
                    os.rename(dirPath + "/" + dateiname, dirPath + "/" + neuer_dateiname)
                    continue
        if (dateiname.split(".")[1] == "uix" or dateiname.split(".")[1] == "info"):
                os.unlink(dirPath + "/" + dateiname) # .uix-Dateien löschen


def select_file():
    global dirPath
    #global auswahl_label

    dirPath = fd.askdirectory(
        title='Verzeichnis des Chats auswählen.',
        initialdir='/')

    #showinfo(
    #    title='Selected File',
    #    message=str(dirPath))

    if (dirPath == ''):
        auswahl_label.configure(text="Nichts ausgewählt!")

    else:
        auswahl_label.configure(text=dirPath)
        execute_button.pack(expand=True)


def start():
    print("jetzt gehts ab mit " + dirPath) # hier das rein was passieren soll, wenn OK gedrückt wurde
    attachmentPath = dirPath + "/Attachments/"
    infoPath = dirPath + "/Info/"
    infoPicturePath = infoPath + "/Picture/"
    
    dateien_umbenennen(dirPath)
    if os.path.exists(attachmentPath):
        dateien_umbenennen(attachmentPath)
    if os.path.exists(infoPath):
        dateien_umbenennen(infoPath)
    if os.path.exists(infoPicturePath):
        dateien_umbenennen(infoPicturePath)
    showinfo(
        title='Fertig!',
        message=str("Die Chats in " + dirPath + " wurden sortiert!"))
    root.destroy()

# open button
open_button = ttk.Button(root,text='Chat-Verzeichnis auswählen',command=select_file)

#execute button
execute_button = ttk.Button(root, text="Start", command=start)
open_button.pack(expand=True)

#Auswahl-LAbel
auswahl_label = ttk.Label(root)
auswahl_label.pack()


# run the application
root.mainloop()
print(dirPath)
