from tkinter import *


def run(root):
    root.resizable(1, 1)
    root.title("Practica de branch")



    frame=Frame()
    frame.pack(fill="y", expand=1)
    frame.config(width="1000",height="450") 
    frame.config(bg="red", bd=15, relief="groove", cursor="hand2")

if __name__ == '__main__':
    root= Tk()
    run(root)
    root.mainloop()