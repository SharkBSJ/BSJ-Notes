from Note import Note
from ErrorHandling import ErrorHandling
import time
import json
import tkinter as tk
from tkinter import *

def load_json():
    while ErrorHandling.file_lock == 1:
        pass
    ErrorHandling.file_lock = 1
    with open("datas.json", "a") as f:
        pass
    datas = {}
    with open("datas.json", "r") as f:
        f.seek(0)
        temp_str = f.read()
        try:
            if (len(temp_str) > 0):
                datas = json.loads(temp_str)
        except:
            print("ERROR: read_json")
            ErrorHandling.handle()

        if len(datas) != 0:
            for temp in datas:
                Note(temp, datas[temp]['x'], datas[temp]['y'], datas[temp]['text'], root)
        else:
            Note(int(round(time.time() * 1000)), 100, 100, '', root)
            time.sleep(0.002)
        ErrorHandling.file_lock = 0
        ErrorHandling.make_back_up()

def destroyer():
    root.quit()
    root.destroy()
    sys.exit()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("BSJ Notes")
    root.geometry("300x300+100+100")
    #root.withdraw()
    #root.overrideredirect(True)
    root.attributes("-alpha",0.0)
    load_json()
    root.protocol("WM_DELETE_WINDOW", destroyer)
    root.mainloop()
