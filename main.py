import tkinter
from Canvas import board

def main():
    root = tkinter.Tk()
    window = board(root)
    root.mainloop()
    #root.bind("<KeyPress-x>", lambda _:root.displayBalls())


if __name__ == '__main__':
    main()