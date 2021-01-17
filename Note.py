from ErrorHandling import ErrorHandling
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import time
import json

class Note:
    def getPos(self):
        pos = []
        pos.append(self.root.winfo_rootx())
        pos.append(self.root.winfo_rooty())
        return pos
    
    def move_window(self, event):
        self.root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))
        while ErrorHandling.file_lock == 1:
            pass
        ErrorHandling.file_lock = 1
        self.datas = self.read_json()
        self.write_json(self.datas)
        ErrorHandling.file_lock = 0

    def click_button(self, event):
        temp = self.buttons[event.widget]
        if temp == 2:
            self.pos = self.getPos()
            Note(int(round(time.time() * 1000)), self.pos[0], self.pos[1], '', self.master)
            time.sleep(0.002)
        elif temp == 1:
            self.root.focus()
        else:
            if len(self.text.get("1.0", "end-1c"))!=0:
                MsgBox = messagebox.askokcancel("Erase?", "Do you want to erase the notes", icon='warning')
                if MsgBox == True:
                    self.delete_json()
                    self.root.destroy()
            else:
                self.root.destroy()

    def delete_json(self):
        self.text.delete(1.0, END)
        while ErrorHandling.file_lock == 1:
            pass
        ErrorHandling.file_lock = 1
        self.datas = self.read_json()
        self.write_json(self.datas)
        ErrorHandling.file_lock = 0

    def read_json(self):
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

            if (len(self.text.get("1.0", "end-1c")) == 0):
                    datas.pop(str(self.title), None)
            else:
                temp = {}
                self.pos = self.getPos()
                temp['x'] = self.pos[0]
                temp['y'] = self.pos[1]
                temp['text'] = self.text.get("1.0", "end-1c")
                datas.update({str(self.title):temp})
        return datas
    
    def write_json(self, datas):
        f = open("datas.json", "w")
        json.dump(datas, f)
        f.close()
        
    def input_text(self, event):
        while ErrorHandling.file_lock == 1:
            pass
        ErrorHandling.file_lock = 1
        self.datas = self.read_json()
        self.write_json(self.datas)
        ErrorHandling.file_lock = 0
    
    def __init__(self, time, x, y, text, master):
        # Window Setting
        self.master = master
        self.root = tk.Toplevel(self.master)
        self.root.overrideredirect(True)
        self.root.geometry("300x300+{0}+{1}".format(x+50, y+50))
        self.title = time

        # Change bar
        # make a frame for the title bar
        self.title_bar = Frame(self.root, bg='#2e2e2e', relief='raised', bd=2,highlightthickness=0)
        # put a close button on the title bar
        self.close_button = Button(self.title_bar, text='x',bg="#2e2e2e",padx=2,pady=2,activebackground='red',bd=0,font="bold",fg='white',highlightthickness=0)
        self.minimize_button = Button(self.title_bar, text='-',bg="#2e2e2e",padx=2,pady=2,activebackground='red',bd=0,font="bold",fg='white',highlightthickness=0)
        self.add_button = Button(self.title_bar, text='+',bg="#2e2e2e",padx=2,pady=2,activebackground='red',bd=0,font="bold",fg='white',highlightthickness=0)
        # a canvas for the main area of the window
        # self.window = Canvas(self.root, bg='#2e2e2e',highlightthickness=0)
        # pack the widgets
        #self.title_bar.pack(expand=1, fill=X)
        #self.title_bar.grid(row=0)
        self.title_bar.pack(fill=X)
        self.close_button.pack(side=RIGHT,anchor=N)
        #self.minimize_button.pack(side=LEFT, anchor=N)
        self.add_button.pack(side=TOP,anchor=E)
        #self.window.pack(expand=1, fill=BOTH)
        # bind function
        self.title_bar.bind('<B1-Motion>', self.move_window)
        self.buttons = {}
        self.buttons[self.close_button] = 0
        self.buttons[self.minimize_button] = 1
        self.buttons[self.add_button] = 2
        self.close_button.bind("<Button-1>", self.click_button)
        self.minimize_button.bind("<Button-1>", self.click_button)
        self.add_button.bind("<Button-1>", self.click_button)

        # Add Text
        self.scroll_y = tk.Scrollbar(self.root, orient="vertical")
        self.scroll_y.pack(side="right", fill="y")
        #self.scroll_y,grid(row=1, column=0)

        self.text = tk.Text(self.root,
                        height=300,
                        width=300,
                        yscrollcommand=self.scroll_y.set) # added one text box
        #self.text.focus_set()
        self.text.bind('<KeyRelease>', self.input_text)
        
        self.text.pack(side=LEFT, fill="y")
        #self.text.gird(row=1, column=0)
        self.scroll_y.config(command=self.text.yview)

        if len(text) != 0:
            self.text.insert(CURRENT, text)

        self.root.after(10, self.update_root)

    def update_root(self):
        self.root.update()
        self.root.after(10, self.update_root)

    def getWindows(self):
        return self.title_bar
