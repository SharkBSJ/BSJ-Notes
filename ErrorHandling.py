from tkinter import messagebox

class ErrorHandling:
    file_lock=0 # For Critical Section
    
    def make_back_up():
        while ErrorHandling.file_lock == 1:
            pass
        ErrorHandling.file_lock = 1
        with open("datas.json", "r") as original:
            backup = open("datas.backup", "w")
            backup.write(original.read())
            backup.close()
        ErrorHandling.file_lock = 0
    def handle():
        with open("datas.backup", "r") as original:
            backup = open("datas.json", "w")
            backup.write(original.read())
            backup.close()
        with open("datas.backup", "w") as f:
            pass
        
        messagebox.showerror("Error", "Error Occured! Please Restart Program")
        quit()
    def __init__(self):
        pass

