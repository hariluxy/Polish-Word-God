import tkinter as tk
from gui import create_gui

def main():
    root = tk.Tk()
    root.title("Polish Word Wizard by Harilux")
    create_gui(root)
    root.mainloop()

if __name__ == "__main__":
    main()
