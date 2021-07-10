import sys
from tkinter import Canvas, Image

from PIL import ImageTk

WIDTH = 300
HEIGHT = 300
DOT_SIZE = 10
DELAY = 100





class Board(Canvas):

    def __int__(self, parent):
        super().__init__(width=WIDTH, heigth=HEIGHT, background='black', highlightthickness=0)

        self.parent = parent
        self.ini_game()
        self.pack()

    def ini_game(self):
        self.left = False
        self.right = True
        self.up = False
        self.down = False
        self.in_game = True

        self.dot_x = 100
        self.dot_y = 190

        try:
            self.ibody = Image.open('dot.png')
            self.body = ImageTk.PhotoImage(self.ibody)
            self.ibody = Image.open('head.png')
            self.head = ImageTk.PhotoImage(self.ibody)
            self.idot = Image.open('dot.png')
            self.dot = ImageTk.PhotoImage(self.ibody)
        except IOError as e:
            print(str(e))
            sys.exit(1)

        self.focus_get()
        self.create_objects()
        self.bind_all('<Key>', self.on_key_press)
        self.after(DELAY, self.on_time)

    def crete_objects(self):
        self.create_image(self.dot_x, self.dot_y, image=self.dot, anchor=NW, tag='dot')
        self.create_image(50, 50, image=self.head, anchor=NW, tag='head')
        self.create_image(40, 50, image=self.body, anchor=NW, tag='body')
        self.create_image(30, 50, image=self.body, anchor=NW, tag='body')