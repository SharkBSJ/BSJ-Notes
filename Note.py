import tkinter as tk
from tkinter import *
import time

class Note:
    def getPos(self):
        pos = []
        pos.append(self.root.winfo_rootx())
        pos.append(self.root.winfo_rooty())
        return pos
    
    def move_window(self, event):
        self.root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

    def click_button(self, event):
        if self.buttons[event.widget] == 1:
            self.pos = self.getPos()
            note = Note(int(round(time.time() * 1000)), self.pos[0], self.pos[1])
            time.sleep(0.002)
        else:
            self.root.destroy()

    def input_text(self, event):
        print(self.text.get("1.0",END) + " / " + str(self.title))
        self.pos = self.getPos()
        print(str(self.pos[0]) + " / " + str(self.pos[1]))
    
    def __init__(self, time, x, y):
        # Window Setting
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.geometry("300x300+{0}+{1}".format(x+50, y+50))
        self.title = time

        # Change bar
        # make a frame for the title bar
        self.title_bar = Frame(self.root, bg='#2e2e2e', relief='raised', bd=2,highlightthickness=0)
        # put a close button on the title bar
        self.close_button = Button(self.title_bar, text='x',bg="#2e2e2e",padx=2,pady=2,activebackground='red',bd=0,font="bold",fg='white',highlightthickness=0)
        self.add_button = Button(self.title_bar, text='+',bg="#2e2e2e",padx=2,pady=2,activebackground='red',bd=0,font="bold",fg='white',highlightthickness=0)
        # a canvas for the main area of the window
        # self.window = Canvas(self.root, bg='#2e2e2e',highlightthickness=0)
        # pack the widgets
        #self.title_bar.pack(expand=1, fill=X)
        #self.title_bar.grid(row=0)
        self.title_bar.pack(fill=X)
        self.close_button.pack(side=RIGHT,anchor=N)
        self.add_button.pack(side=TOP,anchor=E)
        #self.window.pack(expand=1, fill=BOTH)
        # bind function
        self.title_bar.bind('<B1-Motion>', self.move_window)
        self.buttons = {}
        self.buttons[self.close_button] = 0
        self.buttons[self.add_button] = 1
        self.close_button.bind("<Button-1>", self.click_button)
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

    def getWindows(self):
        return self.title_bar
