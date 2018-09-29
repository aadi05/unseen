# unseen
Movie ticket booking system using python's library tkinter.
import tkinter as tk
import tkinter as ttk
from PIL import Image,ImageTk
from tkinter import ttk
from win32api import GetSystemMetrics
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import sqlite3
import os

w = GetSystemMetrics(0)
h = GetSystemMetrics(1)
w2 = int(w/6.956)

x_cord = (w2/2)-100

path = r"C:\Users\USER\PycharmProjects\unseen\register\login.txt"

summary1 = r"C:\Users\USER\PycharmProjects\unseen\summary\summary1.txt"
summary2 = r"C:\Users\USER\PycharmProjects\unseen\summary\summary2.txt"
summary3 = r"C:\Users\USER\PycharmProjects\unseen\summary\summary3.txt"
summary4 = r"C:\Users\USER\PycharmProjects\unseen\summary\summary4.txt"
summary5 = r"C:\Users\USER\PycharmProjects\unseen\summary\summary5.txt"
summary6 = r"C:\Users\USER\PycharmProjects\unseen\summary\summary6.txt"
summary7 = r"C:\Users\USER\PycharmProjects\unseen\summary\summary7.txt"
summary8 = r"C:\Users\USER\PycharmProjects\unseen\summary\summary8.txt"
summary9 = r"C:\Users\USER\PycharmProjects\unseen\summary\summary9.txt"
summary10 = r"C:\Users\USER\PycharmProjects\unseen\summary\summary10.txt"

global movie_no
global butt1
global butt2
global butt3
global butt4
global butt5
global butt6
global butt7
global butt8
global butt9
global butt10

frames = {}
movie_no = 0
first_time = True

i=500
j=150

ans=0

class unseen(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        global container
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        global frames

        frames = {}

        for F in (register,homepage, page_one,seat_arrangement,ticket_page,cinema_hall):
            frame = F(container, self)
            frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(register)

    def show_frame(self, cont):
        frame = frames[cont]
        frame.tkraise()


class homepage(tk.Frame):
    def __init__(self, parent, controller):


        def nextpage(movie):
            global movie_no, frames
            movie_no = movie

            global container

            # creates the object of the class page_one with conatiner as tk.Frame
            # print(frames)
            frames[page_one].__init__(container,controller)  # <=-------reinstiallzie the pageone without creating objects
            controller.show_frame(page_one)

        tk.Frame.__init__(self, parent, bg="white")

        img1 = ImageTk.PhotoImage(file="panther.png")
        img2 = ImageTk.PhotoImage(file="rim.jpeg")
        img3 = ImageTk.PhotoImage(file="titu.jpg")
        img4 = ImageTk.PhotoImage(file="padmaavat.jpg")
        img5 = ImageTk.PhotoImage(file="paddington.jpg")
        img6 = ImageTk.PhotoImage(file="manus.jpg")
        img7 = ImageTk.PhotoImage(file="star.jpg")
        img8 = ImageTk.PhotoImage(file="water.jpg")
        img9 = ImageTk.PhotoImage(file="raid.jpg")
        img10 = ImageTk.PhotoImage(file="padman.jpeg")




        butts = tk.Button(self, font=('italic', '9', 'bold'), fg="white", bg="white", height=8,
                          width=w2, bd=0, activebackground="white")
        logo_a = ImageTk.PhotoImage(file="newlogo.png")
        logo_b = ImageTk.PhotoImage(file="newlogo.png")

        '''logo1 = tk.Label(self, image=logo_a, width=300, height=150)
        logo1.image = logo_a
        logo1.place(x=5, y=0)'''
        logo2 = tk.Label(self, image=logo_b, width=170, height=167)
        logo2.image = logo_b
        logo2.place(x=1150, y=2)
        signout = ttk.Button(self, text="Logout", command= lambda: controller.show_frame(register))
        signout.place(x=1200, y=113)
        butts.grid(row=0, columnspan=5)
        label = tk.Label(self, text="TRENDING", font=('arial','15','bold'), pady=8, bg="white", fg="Navajowhite4")
        label.grid(row=1, column=0)

        butt1 = tk.Button(self, image=img1, height=200, width=137, bd=1, bg="black", command=lambda i=1: nextpage(i))
        butt1.image = img1
        butt1.grid(row=2, column=0)

        butt2 = tk.Button(self, image=img2, height=200, width=135, bd=1, bg="black", command=lambda i=2: nextpage(i))
        butt2.image = img2
        butt2.grid(row=2, column=1)

        butt3 = tk.Button(self, image=img3, height=205, width=138, bd=1, bg="black", command=lambda i=3: nextpage(i))
        butt3.image = img3
        butt3.grid(row=2, column=2)

        butt4 = tk.Button(self, image=img4, height=202, width=137, bd=1, bg="black", command=lambda i=4: nextpage(i))
        butt4.image = img4
        butt4.grid(row=2, column=3)

        butt5 = tk.Button(self, image=img5, height=202, width=137, bd=1, bg="black", command=lambda i=5: nextpage(i))
        butt5.image = img5
        butt5.grid(row=2, column=4)
# -----------------------------------------------------------------------------------------------------------------------------

        link = tk.Button(self, text="Black Panther", height=1, fg="black", bg="white", width=15, bd=0, pady=8, font=('italic','9','bold'), activebackground="white"
                         , command=lambda: controller.show_frame(page_one))
        link.grid(row=3, column=0)

        link = tk.Button(self, text="Pacific Rim: Uprising", height=1, bg="white", width=18, bd=0,pady=8, font=('italic','9','bold'), activebackground="white"
                         , command=lambda: controller.show_frame(page_one))
        link.grid(row=3, column=1)

        link = tk.Button(self, text="Sonu Ke Titu Ki Sweety", height=1, bg="white", width=20, bd=0, pady=8, font=('italic','9','bold'), activebackground="white"
                         , command=lambda: controller.show_frame(page_one))
        link.grid(row=3, column=2)

        link = tk.Button(self, text="Padmaavat", height=1, width=15, bg="white", bd=0,pady=8, font=('italic','9','bold'), activebackground="white"
                         , command=lambda: controller.show_frame(page_one))
        link.grid(row=3, column=3)

        link = tk.Button(self, text="Paddington 2", height=1, width=15, bg="white", bd=0,pady=8, font=('italic','9','bold'), activebackground="white"
                         , command=lambda: controller.show_frame(page_one))
        link.grid(row=3, column=4)

# ---------------------------------------------------------------------------------------------------------------------------
        label2 = tk.Label(self, text="OTHER", font=('arial','15','bold'), pady=8, bg="white", fg="Navajowhite4")
        label2.grid(row=4, column=0)


        butt6 = tk.Button(self, image=img6, height=202, width=138, bd=1, bg="black", command=lambda i=6:  nextpage(i))
        butt6.image = img6
        butt6.grid(row=5, column=0)

        butt7 = tk.Button(self, image=img7, height=200, width=137, bd=1, bg="black", command=lambda i=7:  nextpage(i))
        butt7.image = img7
        butt7.grid(row=5, column=1)

        butt8 = tk.Button(self, image=img8, height=200, width=137, bd=1, bg="black", command=lambda i=8:  nextpage(i))
        butt8.image = img8
        butt8.grid(row=5, column=2)

        butt9 = tk.Button(self, image=img9, height=200, width=137, bd=1, bg="black", command=lambda i=9:  nextpage(i))
        butt9.image = img9
        butt9.grid(row=5, column=3)

        butt10 = tk.Button(self, image=img10, height=200, width=137, bd=1, bg="black", command=lambda i=10:  nextpage(i))
        butt10.image = img10
        butt10.grid(row=5, column=4)

# -----------------------------------------------------------------------------------------------------------------------------

        link = tk.Button(self, text="Aapla Manus", height=1, width=10, bg="white", bd=0, pady=8, font=('italic','9','bold'), activebackground="white"
                         , command=lambda: controller.show_frame(page_one))
        link.grid(row=6, column=0)

        link = tk.Button(self, text="Star Wars: The Last Jedi", height=1, width=20, bg="white", bd=0, pady=8, font=('italic','9','bold'), activebackground="white"
                         , command=lambda: controller.show_frame(page_one))
        link.grid(row=6, column=1)

        link = tk.Button(self, text="The Shape Of Water", height=1, width=20, bg="white", bd=0, pady=8, font=('italic','9','bold'), activebackground="white"
                         , command=lambda: controller.show_frame(page_one))
        link.grid(row=6, column=2)

        link = tk.Button(self, text="Raid", height=1, width=10, bd=0, pady=8, bg="white", font=('italic','9','bold'), activebackground="white"
                         , command=lambda: controller.show_frame(page_one))
        link.grid(row=6, column=3)

        link = tk.Button(self, text="Pad Man", height=1, width=15, bd=0, pady=8, bg="white", font=('italic','9','bold'), activebackground="white"
                         , command=lambda: controller.show_frame(page_one))
        link.grid(row=6, column=4)


class page_one(tk.Frame):

    def __init__(self, parent, controller):

        global first_time

        if (first_time == True):  # ------------------------------------->only creates the obj first time
            tk.Frame.__init__(self, parent, bg="black")

            summary = tk.Label(self, text="SUMMARY", font=('italic','25','bold'), fg="white", bg="black")
            summary.place(x=390, y=90)

            global movie_no


            self.movie = tk.Label(self, font=('arial', '25', 'bold', 'underline'), fg="white", bg="black")
            self.movie.place(x=10, y=530)
            self.date = tk.Label(self, font=('arial', '13'), fg="white", bg="black")
            self.date.place(x=10, y=580)
            self.time = tk.Label(self, font=('arial', '13'), fg="white", bg="black")
            self.time.place(x=10,y=610)
            self.imdb = tk.Label(self, font=('arial', '25', 'bold'), fg="white", bg="black")
            self.imdb.place(x=390, y=20)
            self.rating = tk.Label(self, font=('arial', '25'), fg="DarkGoldenrod3", bg="black")
            self.rating.place(x=520, y=20)

            back = ttk.Button(self, text="Back", command= lambda: controller.show_frame(homepage))
            back.place(x=700, y=600)

            book_now = ttk.Button(self, text="Book now", command= lambda: controller.show_frame(cinema_hall))
            book_now.place(x=850, y=600)

        first_time = False  # ------------------------------------->never turn this off

        global movie_no

        self.set = 1
        self.Synopsis()

    def Synopsis(self):
        if (movie_no == 1):
            self.wall = tk.Label(self, bg="black", height=30, width=160)
            self.wall.place(x=390, y=130)

            self.poster1 = ImageTk.PhotoImage(file="mp1.jpg")
            self.img1 = tk.Label(self, bd=2, width=340, height=504, bg="black")
            self.img1.configure(image=self.poster1)
            self.img1.place(x=10, y=10)
            self.movie.configure(text="Black Panther(3D)")
            self.date.configure(text="16 Feb,2018")
            self.time.configure(text="2 hrs 14 mins")
            self.imdb.configure(text="IMDB :")
            self.rating.configure(text="7.8")

            with open(summary1, 'r') as f:
                i=390
                j=150
                for line in f:
                    self.synopsis1 = tk.Label(self, text=line, font=('arial', '13'), bg="black", fg="white")
                    self.synopsis1.place(x=i, y=j)
                    j = j + 35

            self.set = 0
        if (movie_no == 2):
            self.wall = tk.Label(self, bg="black", height=30, width=160)
            self.wall.place(x=390, y=130)

            self.poster2 = ImageTk.PhotoImage(file="mp2.jpg")
            self.img2 = tk.Label(self, bd=2, width=340, height=504, bg="black")
            self.img2.configure(image=self.poster2)
            self.img2.place(x=10, y=10)
            self.movie.configure(text="Pacific Rim:Uprising")
            self.date.configure(text="23 March,2018")
            self.time.configure(text="2 hrs 18 mins")
            self.imdb.configure(text="IMDB :")
            self.rating.configure(text="6.0")


            with open(summary2, 'r') as f:
                i = 390
                j = 150
                for line in f:
                    self.synopsis2 = tk.Label(self, text=line, font=('arial', '13'), bg="black", fg="white")
                    self.synopsis2.place(x=i, y=j)
                    j = j + 35


        if (movie_no == 3):
            self.wall = tk.Label(self, bg="black", height=30, width=160)
            self.wall.place(x=390, y=130)

            self.poster3 = ImageTk.PhotoImage(file="mp3.jpg")
            self.img3 = tk.Label(self, bd=2, width=340, height=504, bg="black")
            self.img3.configure(image=self.poster3)
            self.img3.place(x=10, y=10)
            self.movie.configure(text="Sonu Ke Titu Ki Sweety")
            self.date.configure(text="23 Feb,2018")
            self.time.configure(text="2 hrs 20 mins")
            self.imdb.configure(text="IMDB :")
            self.rating.configure(text="8.3")

            with open(summary3, 'r') as f:
                i = 390
                j = 150
                for line in f:
                    self.synopsis3 = tk.Label(self, text=line, font=('arial', '13'), bg="black", fg="white")
                    self.synopsis3.place(x=i, y=j)
                    j = j + 35

        if (movie_no == 4):
            self.wall = tk.Label(self, bg="black", height=30, width=160)
            self.wall.place(x=390, y=130)

            self.poster4 = ImageTk.PhotoImage(file="mp4.jpg")
            self.img4 = tk.Label(self, bd=2, width=340, height=504, bg="black")
            self.img4.configure(image=self.poster4)
            self.img4.place(x=10, y=10)
            self.movie.configure(text="Padmaavat")
            self.date.configure(text="25 Jan,2018")
            self.time.configure(text="2 hrs 43 mins")
            self.imdb.configure(text="IMDB :")
            self.rating.configure(text="8.2")

            with open(summary4, 'r') as f:
                i = 390
                j = 150
                for line in f:
                    self.synopsis4 = tk.Label(self, text=line, font=('arial', '13'), bg="black", fg="white")
                    self.synopsis4.place(x=i, y=j)
                    j = j + 35


        if (movie_no == 5):
            self.wall = tk.Label(self, bg="black", height=30, width=160)
            self.wall.place(x=390, y=130)

            self.poster5 = ImageTk.PhotoImage(file="mp5.jpg")
            self.img5 = tk.Label(self, bd=2, width=340, height=504, bg="black")
            self.img5.configure(image=self.poster5)
            self.img5.place(x=10, y=10)
            self.movie.configure(text="Paddington 2")
            self.date.configure(text="12 Jan,2018")
            self.time.configure(text="1 hrs 43 mins")
            self.imdb.configure(text="IMDB :")
            self.rating.configure(text="8.6")

            with open(summary5, 'r') as f:
                i = 390
                j = 150
                for line in f:
                    self.synopsis5 = tk.Label(self, text=line, font=('arial', '13'), bg="black", fg="white")
                    self.synopsis5.place(x=i, y=j)
                    j = j + 35

        if (movie_no == 6):
            self.wall = tk.Label(self, bg="black", height=30, width=160)
            self.wall.place(x=390, y=130)

            self.poster6 = ImageTk.PhotoImage(file="mp6.jpg")
            self.img6 = tk.Label(self, bd=2, width=340, height=504, bg="black")
            self.img6.configure(image=self.poster6)
            self.img6.place(x=10, y=10)
            self.movie.configure(text="Aapla Manus")
            self.date.configure(text="9 Feb,2018")
            self.time.configure(text="1 hrs 52 mins")
            self.imdb.configure(text="IMDB :")
            self.rating.configure(text="8.2")

            with open(summary6, 'r') as f:
                i = 390
                j = 150
                for line in f:
                    self.synopsis6 = tk.Label(self, text=line, font=('arial', '13'), bg="black", fg="white")
                    self.synopsis6.place(x=i, y=j)
                    j = j + 35


        if (movie_no == 7):
            self.wall = tk.Label(self, bg="black", height=30, width=160)
            self.wall.place(x=390, y=130)

            self.poster7 = ImageTk.PhotoImage(file="mp7.jpg")
            self.img7 = tk.Label(self, bd=2, width=340, height=504, bg="black")
            self.img7.configure(image=self.poster7)
            self.img7.place(x=10, y=10)
            self.movie.configure(text="Star Wars:The Last Jedi")
            self.date.configure(text="9 Dec,2017")
            self.time.configure(text="2 hrs 31 mins")
            self.imdb.configure(text="IMDB :")
            self.rating.configure(text="8.5")

            with open(summary7, 'r') as f:
                i = 390
                j = 150
                for line in f:
                    self.synopsis7 = tk.Label(self, text=line, font=('arial', '13'), bg="black", fg="white")
                    self.synopsis7.place(x=i, y=j)
                    j = j + 35

        if (movie_no == 8):
            self.wall = tk.Label(self, bg="black", height=30, width=160)
            self.wall.place(x=390, y=130)

            self.poster8 = ImageTk.PhotoImage(file="mp8.jpg")
            self.img8 = tk.Label(self, bd=2, width=340, height=504, bg="black")
            self.img8.configure(image=self.poster8)
            self.img8.place(x=10, y=10)
            self.movie.configure(text="The Shape Of Water")
            self.date.configure(text="16 Feb,2018")
            self.time.configure(text="2 hrs 04 mins")
            self.imdb.configure(text="IMDB :")
            self.rating.configure(text="8.0")

            with open(summary8, 'r') as f:
                i = 390
                j = 150
                for line in f:
                    self.synopsis8 = tk.Label(self, text=line, font=('arial', '13'), bg="black", fg="white")
                    self.synopsis8.place(x=i, y=j)
                    j = j + 35

        if (movie_no == 9):
            self.wall = tk.Label(self, bg="black", height=30, width=160)
            self.wall.place(x=390, y=130)

            self.poster9 = ImageTk.PhotoImage(file="mp9.jpg")
            self.img9 = tk.Label(self, bd=2, width=340, height=504, bg="black")
            self.img9.configure(image=self.poster9)
            self.img9.place(x=10, y=10)
            self.movie.configure(text="Raid")
            self.date.configure(text="16 March,2018")
            self.time.configure(text="2 hrs 08 mins")
            self.imdb.configure(text="IMDB :")
            self.rating.configure(text="8.1")

            with open(summary9, 'r') as f:
                i = 390
                j = 150
                for line in f:
                    self.synopsis9 = tk.Label(self, text=line, font=('arial', '13'), bg="black", fg="white")
                    self.synopsis9.place(x=i, y=j)
                    j = j + 35

        if (movie_no == 10):
            self.wall = tk.Label(self, bg="black", height=30, width=160)
            self.wall.place(x=390, y=130)

            self.poster10 = ImageTk.PhotoImage(file="mp10.jpg")
            self.img10 = tk.Label(self, bd=2, width=340, height=504, bg="black")
            self.img10.configure(image=self.poster10)
            self.img10.place(x=10, y=10)
            self.movie.configure(text="Pad Man")
            self.date.configure(text="9 Feb,2018")
            self.time.configure(text="1 hrs 56 mins")
            self.imdb.configure(text="IMDB :")
            self.rating.configure(text="8.9")

            with open(summary10, 'r') as f:
                i = 390
                j = 150
                for line in f:
                    self.synopsis10 = tk.Label(self, text=line, font=('arial', '13'), bg="black", fg="white")
                    self.synopsis10.place(x=i, y=j)
                    j = j + 35


class register(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        global entry1

        def login_check():
            c = entry1.get() + entry2.get()
            with open(path, 'r') as f:
                data = f.readlines()
                i = 0
                k = 0
                for line in data:
                    if entry1.get() == "" or entry2.get() == "":
                        messagebox.showwarning('Invalid Input', 'Enter Proper Credentials')
                        k=11
                        break
                    if data[i].rstrip() == c:
                        controller.show_frame(homepage)
                        k = 5
                    else:
                        i=i+1
                if k != 5 and k!=11:
                    messagebox.showwarning('Invalid Inputs', 'Invalid Username/Password')

        def create():
            e1 = tk.StringVar()
            e2 = tk.StringVar()
            e3 = tk.StringVar()
            window = tk.Toplevel(bg="white")
            window.geometry('470x180')
            label = tk.Label(window, text="USER REGISTRATION", bg="black", fg="white", font=('arial', '21', 'bold'),
                             relief="raised", bd=5)
            label.grid(columnspan=4)
            name = tk.Label(window, text="Full name", font=('arial', '15'), fg="black", bg="white")
            name.grid(row=1, column=0)
            e1 = tk.Entry(window, width=40, font=('arial', '13'), bg="gainsboro")
            e1.grid(row=1, column=1)
            username = tk.Label(window, text="Username", font=('arial', '15'), fg="black", bg="white")
            username.grid(row=2, column=0)
            e2 = tk.Entry(window, width=25, font=('arial', '13'), bg="gainsboro")
            e2.grid(row=2, column=1, sticky="w")
            password = tk.Label(window, text="Password", font=('arial', '15'), fg="black", bg="white")
            password.grid(row=3, column=0)
            e3 = tk.Entry(window, width=30, font=('arial', '13'), show="*", bg="gainsboro")
            e3.grid(row=3, column=1, sticky="w")

            def signup():
                with open(path, 'a') as f:
                    if e1.get() == "" or e2.get() == "" or e3.get() == "":
                        messagebox.showwarning('Invalid Input', 'Enter all Credentials')
                    else:
                        x1 = e1.get()
                        x2 = e2.get()
                        x3 = e3.get()
                        conn = sqlite3.connect('test.db')
                        c = conn.cursor()
                        c.execute('''insert into register(fname,username,password) values(?,?,?)''', (x1,x2,x3))
                        conn.commit()
                        c.execute('''select * from register''')
                        print(c.fetchall())
                        f.write(e2.get())
                        f.write(e3.get())
                        f.write('\n')
                        f.close()
                        label = tk.Label(window, text="Your account has been succesfully created.", fg="green",
                                         font=('arial', '13', 'bold'), bg="salmon")
                        label.place(x=10, y=155)

            signup_butt = ttk.Button(window, text="Signup", width=11, command=signup)
            signup_butt.place(x=110, y=130)

            def quit():
                window.destroy()

            quit_butt = ttk.Button(window, text="Quit", command=quit, width=11)
            quit_butt.place(x=250, y=130)
            window.mainloop()

        background_image = ImageTk.PhotoImage(file="darth.jpg")
        background_label = tk.Label(self, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        label = tk.Label(self, text="USER LOGIN", bg="black", fg="grey", font=('arial', '21', 'bold'), relief="raised",
                         bd=0)
        label.place(x=110, y=400)
        user = tk.Label(self, text="Username", bg="black", font=('arial', '15'), fg="white")
        user.place(x=10, y=500)
        entry1 = tk.Entry(self, width=30, font=('arial', '13'), bg="white")
        entry1.place(x=130, y=503)
        password = tk.Label(self, text="Password", bg="black", font=('arial', '15'), fg="white")
        password.place(x=10, y=550)
        entry2 = tk.Entry(self, width=30, font=('arial', '13'), show="*", bg="white")
        entry2.place(x=130, y=553)

        login_butt = ttk.Button(self, text="Login", width=11, command=login_check)
        login_butt.place(x=70, y=620)
        create_butt = ttk.Button(self, text="Create account", width=15, command=create)
        create_butt.place(x=210, y=620)

class cinema_hall(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        dead = tk.Label(self, width=w2, height=4, bg="grey")
        dead.grid(row=0, columnspan=5)
        back = ttk.Button(self, text="Back", command= lambda: controller.show_frame(page_one))
        back.place(x=1200, y=25)

        hall1 = tk.Button(self, font=('italic', '9', 'bold'), fg="black", bg="white", height=8,
                          width=w2, bd=2, justify="left", command=lambda:controller.show_frame(seat_arrangement), activebackground="white")
        hall1.grid(row=1, columnspan=5, sticky="w")
        h1 = tk.Button(self, text="Inox R-City Ghatkopar", font=('italic', '20', 'bold'), bg="white"
                       , command=lambda: controller.show_frame(seat_arrangement), relief="flat", activebackground="white", bd=0)
        h1.place(x=20, y=100)
        addr1 = tk.Button(self, text="Rcity mall, Lal Bahadur Shastri, Mumbai 400086, India", font=('italic', '13'), bg="white"
                          , command=lambda: controller.show_frame(seat_arrangement), activebackground="white", bd=0)
        addr1.place(x=24, y=140)


        hall2 = tk.Button(self, font=('italic', '9', 'bold'), fg="black", bg="white", height=8,
                          width=w2, bd=2, justify="left", command=lambda:controller.show_frame(seat_arrangement), activebackground="white")
        hall2.grid(row=2, columnspan=5)
        h2 = tk.Button(self, text="PVR Cinema", font=('italic', '20', 'bold'), bg="white"
                       , command=lambda: controller.show_frame(seat_arrangement), activebackground="white", bd=0)
        h2.place(x=20, y=220)
        addr2 = tk.Button(self, text="JVPD Scheme | Dynamic Mall, 5th Floor, Mumbai 400056, India", font=('italic', '13'),
                         bg="white", command=lambda:controller.show_frame(seat_arrangement), activebackground="white", bd=0)
        addr2.place(x=22, y=265)


        hall3 = tk.Button(self, font=('italic', '9', 'bold'), fg="black", bg="white", height=8,
                          width=w2, bd=2, justify="left", command=lambda:controller.show_frame(seat_arrangement), activebackground="white")
        hall3.grid(row=3, columnspan=5)
        h3 = tk.Button(self, text="INOX: Thakur Mall, Dahisar", font=('italic', '20', 'bold'), bg="white", command=lambda:controller.show_frame(seat_arrangement), activebackground="white", bd=0)
        h3.place(x=20, y=360)
        addr3 = tk.Button(self, text="Central Mall 3rd Floor, Opp to Sunshine Hotel,Western Express Highway, Mumbai 403756,India", font=('italic', '13'),
                         bg="white", command=lambda:controller.show_frame(seat_arrangement), activebackground="white", bd=0)
        addr3.place(x=22, y=400)


        hall4 = tk.Button(self, font=('italic', '9', 'bold'), fg="black", bg="white", height=8,
                          width=w2, bd=2, justify="left", command=lambda:controller.show_frame(seat_arrangement), activebackground="white")
        hall4.grid(row=4, columnspan=5)
        h4 = tk.Button(self, text="Carnival Cinemas", font=('italic', '20', 'bold'), bg="white", command=lambda:controller.show_frame(seat_arrangement), activebackground="white", bd=0)
        h4.place(x=20, y=470)
        addr4 = tk.Button(self, text="Plot No 1, Ram Mandir Road | Goregaon West, Off S V Road, Mumbai 400062, India", font=('italic', '13'),
                         bg="white", command=lambda:controller.show_frame(seat_arrangement), activebackground="white", bd=0)
        addr4.place(x=24, y=510)


        hall5 = tk.Button(self, font=('italic', '9', 'bold'), fg="black", bg="white", height=8
                          ,width=w2, bd=2, justify="left", command=lambda:controller.show_frame(seat_arrangement), activebackground="white")
        hall5.grid(row=5, columnspan=5)
        h5 = tk.Button(self, text="IMAX BIG Cinemas", font=('italic', '20', 'bold'), bg="white", command=lambda:controller.show_frame(seat_arrangement), activebackground="white", bd=0)
        h5.place(x=20, y=605)
        addr5 = tk.Button(self, text="Anik Agar Link Road, Mumbai 400037, India", font=('italic', '13'),
                         bg="white", command=lambda:controller.show_frame(seat_arrangement), activebackground="white", bd=0)
        addr5.place(x=22, y=645)



class seat_arrangement(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        canvas = tk.Canvas(self, width=1600, height=900, bg="white")
        canvas.pack()
        blackline = canvas.create_line(700, 0, 700, 900)

        line1 = canvas.create_line(100,90,650,90)
        line2 = canvas.create_line(100,650,650,650)
        line3 = canvas.create_line(100, 90, 100, 650)
        line4 = canvas.create_line(650, 90, 650, 650)

        top_label = tk.Label(self, bg="grey", width=w2, height=4)
        top_label.place(x=0, y=0)

        back = ttk.Button(self, text="Back", command=lambda: controller.show_frame(cinema_hall))
        back.place(x=1200, y=25)



        def display():
            global ans
            ans=0
            # clear entrybox
            selected_seat.delete(0, 'end')

            # add selected items in entrybox
            for text, var in zip(cb_list1, cb_var1):
                if var.get():
                    # the checkbutton is selected
                    selected_seat.insert('end', text)
                    selected_seat.insert('end', '  ')
                    subt.delete(0, 'end')
                    ans = ans + 430
                    subt.insert('end',ans)

            for text, var in zip(cb_list2, cb_var2):
                if var.get():
                    # the checkbutton is selected
                    selected_seat.insert('end', text)
                    selected_seat.insert('end', '  ')
                    subt.delete(0, 'end')
                    ans = ans + 380
                    subt.insert('end', ans)

            for text, var in zip(cb_list3, cb_var3):
                if var.get():
                    # the checkbutton is selected
                    selected_seat.insert('end', text)
                    selected_seat.insert('end', '  ')
                    subt.delete(0, 'end')
                    ans = ans + 300
                    subt.insert('end', ans)

            for text, var in zip(cb_list4, cb_var4):
                if var.get():
                    # the checkbutton is selected
                    selected_seat.insert('end', text)
                    selected_seat.insert('end', '  ')
                    subt.delete(0, 'end')
                    ans = ans + 300
                    subt.insert('end', ans)

            for text, var in zip(cb_list5, cb_var5):
                if var.get():
                    # the checkbutton is selected
                    selected_seat.insert('end', text)
                    selected_seat.insert('end', '  ')
                    subt.delete(0, 'end')
                    ans = ans + 260
                    subt.insert('end', ans)

            for text, var in zip(cb_list6, cb_var6):
                if var.get():
                    # the checkbutton is selected
                    selected_seat.insert('end', text)
                    selected_seat.insert('end', '  ')
                    subt.delete(0, 'end')
                    ans = ans + 260
                    subt.insert('end', ans)

        cb_list1 = ['V1', 'V2', 'V3', 'V4', 'V5']
        cb_var1 = []
        cb_list2 = ['P1', 'P2', 'P3', 'P4', 'P5']
        cb_var2 = []
        cb_list3 = ['G1', 'G2', 'G3', 'G4', 'G5']
        cb_var3 = []
        cb_list4 = ['G6', 'G7', 'G8', 'G9', 'G10']
        cb_var4 = []
        cb_list5 = ['S1', 'S2', 'S3', 'S4', 'S5']
        cb_var5 = []
        cb_list6 = ['S6', 'S7', 'S8', 'S9', 'S10']
        cb_var6 = []


        m = 150
        label1 = tk.Label(self, text="VIP-Rs.430", justify="center", font=('times', '20', 'bold', 'italic'), bg="white")
        label1.place(x=300, y=100)
        for r, tx in enumerate(cb_list1):
            var = tk.BooleanVar(self, False)
            cb = ttk.Checkbutton(self, variable=var, text=tx)
            cb.place(x=m, y=150)
            m = m + 100
            cb_var1.append(var)

        n = 150
        label2 = tk.Label(self, text="Platinum-Rs.380", justify="center", font=('times', '20', 'bold', 'italic'), bg="white")
        label2.place(x=270, y=200)
        for r, tx in enumerate(cb_list2):
            var = tk.BooleanVar(self, False)
            cb = ttk.Checkbutton(self, variable=var, text=tx)
            cb.place(x=n, y=250)
            n = n + 100
            cb_var2.append(var)

        label3 = tk.Label(self, text="Gold-Rs.300", justify="center", font=('times', '20', 'bold', 'italic'), bg="white")
        label3.place(x=290, y=300)
        p1=150
        for r, tx in enumerate(cb_list3):
            var = tk.BooleanVar(self, False)
            cb = ttk.Checkbutton(self, variable=var, text=tx)
            cb.place(x=p1, y=350)
            p1 = p1 + 100
            cb_var3.append(var)

        p2=150
        for r, tx in enumerate(cb_list4):
            var = tk.BooleanVar(self, False)
            cb = ttk.Checkbutton(self, variable=var, text=tx)
            cb.place(x=p2, y=400)
            p2 = p2 + 100
            cb_var4.append(var)

        label4 = tk.Label(self, text="Silver-Rs.260", justify="center", font=('times', '20', 'bold', 'italic'), bg="white")
        label4.place(x=280, y=450)
        p3 = 150
        for r, tx in enumerate(cb_list5):
            var = tk.BooleanVar(self, False)
            cb = ttk.Checkbutton(self, variable=var, text=tx)
            cb.place(x=p3, y=500)
            p3 = p3 + 100
            cb_var5.append(var)

        p4 = 150
        for r, tx in enumerate(cb_list6):
            var = tk.BooleanVar(self, False)
            cb = ttk.Checkbutton(self, variable=var, text=tx)
            cb.place(x=p4, y=550)
            p4 = p4 + 100
            cb_var6.append(var)

        ok_button = ttk.Button(self, text='Book', command=display)
        ok_button.place(x=330, y=600)

        info = tk.Label(self, text="ALL EYES THIS WAY PLEASE", font=('times', '20', 'bold'), bg="white")
        info.place(x=175, y=660)



        name = tk.Label(self, text="Name", font=('times', '13', 'bold'), bg="white")
        name.place(x=750, y=150)
        name_entry = ttk.Entry(self, width=60)
        name_entry.place(x=900, y=150)

        seats = tk.Label(self, text="Seats Reserved", font=('times', '13', 'bold'), bg="white")
        seats.place(x=750, y=250)
        selected_seat = ttk.Entry(self, width=50)
        selected_seat.place(x=900, y=250)

        mail = tk.Label(self, text="Email", font=('times', '13', 'bold'), bg="white")
        mail.place(x=750, y=200)
        mail_entry = ttk.Entry(self, width=40)
        mail_entry.place(x=900, y=200)

        subtotal = tk.Label(self, text="SUBTOTAL", font=('times', '15', 'bold'), bg="white")
        subtotal.place(x=750, y=310)

        subt = tk.Entry(self)
        subt.place(x=900, y=310)

        def send_mail():
            global ans
            ans=0
            z=3
            while mail_entry.get() != "":

                controller.show_frame(ticket_page)

                email_user = 'unseentechnologies05@gmail.com'
                email_password = 'unseen05'
                email_send = mail_entry.get()

                subject = 'Your Ticket'

                msg = MIMEMultipart()
                msg['From'] = email_user
                msg['To'] = email_send
                msg['Subject'] = subject

                body = 'Greetings from the unseentechnologies \nShow the soft copy of this ticket at the counter and you are good to go.\nHope you enjoy the movie, Stay tuned!!!'
                msg.attach(MIMEText(body, 'plain'))

                filename = 'mail.jpg'
                attachment = open(filename, 'rb')

                part = MIMEBase('application', 'octet-stream')
                part.set_payload((attachment).read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename= " + filename)

                msg.attach(part)
                text = msg.as_string()
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email_user, email_password)

                server.sendmail(email_user, email_send, text)
                server.quit()
                z = 5
                break
            if z!=5:
                messagebox.showerror('Invalid Inputs','Enter your email')
        proceed_butt = ttk.Button(self, text="Proceed", command=send_mail)
        proceed_butt.place(x=1000, y=400)

class ticket_page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Your ticket has been succesfully mailed to your email", justify="center", font=('times', '30', 'bold', 'italic'), fg="green")
        label.place(x=210,y=300)
        button = ttk.Button(self, text="Back", command=lambda: controller.show_frame(seat_arrangement))
        button.place(x=630, y=550)

app = unseen()
app.mainloop()



