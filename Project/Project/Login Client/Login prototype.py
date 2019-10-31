from tkinter import *
import os

def register():
  global register_screen
  global username
  global password
  global username_entry
  global password_entry
  
  screen.destroy() and passcheck_screen.destroy() and usercheck_screen.destroy() and logincheck_screen.destroy()

  register_screen = Tk()
  register_screen.title("Registration")
  register_screen.resizable(width=False, height=False)
  screen_width = register_screen.winfo_screenwidth()
  screen_height = register_screen.winfo_screenheight()
  width_of_window = 1280
  height_of_window = 720
  x_coordinate = (screen_width/2) - (width_of_window/2)
  y_coordinate = (screen_height/2) - (height_of_window/2)
  register_screen.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))
  
  username = StringVar()
  password = StringVar()
  show_password = IntVar()

  Checkbutton(register_screen, text="Show Password", variable=show_password).place(x=10,y=300)

  
  Label(register_screen, text = "REGISTER ", borderwidth=2,bg = "#EEEEEE", font = ("calibri bold", 14)).place(x=10,y=115) 
  Label(register_screen, text = "Username: ").place(x=10,y=170)
  
  username_entry = Entry(register_screen, textvariable = username)
  username_entry.place(x=10,y=200)
  Label(register_screen, text = "Password: ").place(x=10,y=240)
  password_entry =  Entry(register_screen, textvariable = password, show="*").place(x=10,y=270)


  Button(register_screen, text = "Register", width = 10, height = 1, command = register_user).place(x=10,y=330)
  Button(register_screen, text = "Back",height = "2", width = "30", command = back_screen).place(x=10,y=670)

  register_screen.configure(background="#EEEEEE")
  register_banner = PhotoImage(file="Login Banner.png")
  Label(image=register_banner).place(x=0,y=0)
  register_gif = PhotoImage(file="Looping Gif.png")
  Label(image=register_gif,borderwidth=0).place(x=250,y=96.5)
  register_screen.mainloop()
  
def login():
  global username_entry1
  global password_entry1
  global username_verify
  global password_verify
  
  Label(screen, text = " LEADER BOARDS ", borderwidth=2,bg = "#EEEEEE", font = ("calibri bold", 14)).place(x=1080,y=115) 

  username_verify = StringVar()
  password_verify = StringVar()

  Label(screen, text = "Username: ",bg = "#EEEEEE", borderwidth=2).place(x=700,y=20)
  username_entry1 = Entry(screen, textvariable = username_verify).place(x=700,y=51, width = 200, height = 35)
  Label(screen, text = "Password: ",bg = "#EEEEEE", borderwidth=2).place(x=920,y=20)
  password_entry1 = Entry(screen, textvariable = password_verify, show="*").place(x=920,y=51, width = 200, height = 35)
  Button(screen, text = "Login", width = 14, height = 2, command = login_verify).place(x=1150,y=15)

def main_screen():
  global screen
  
  screen = Tk()
  screen.resizable(width=False, height=False)
  screen_width = screen.winfo_screenwidth()
  screen_height = screen.winfo_screenheight()
  width_of_window = 1280
  height_of_window = 720
  x_coordinate = (screen_width/2) - (width_of_window/2)
  y_coordinate = (screen_height/2) - (height_of_window/2)
  screen.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))
  
  screen.configure(background="#EEEEEE")
  login_banner = PhotoImage(file="Login Banner.png")
  Label(image=login_banner,borderwidth=0).place(x=0,y=0)
  login_gif = PhotoImage(file="Looping Gif.png")
  Label(image=login_gif,borderwidth=0).place(x=0,y=95)
  screen.title("Competitive Tetris")
  login()
  Button(text = "Register",height = 1, width = 14, command = register).place(x=1150,y=60)
  screen.mainloop()

def login_verify(): 
  username1 = username_verify.get()
  password1 = password_verify.get()

 
  list_of_files = os.listdir()
  if username1 in list_of_files:
    file1 = open(username1, "r")
    verify = file1.read().splitlines()
    if password1 in verify:
        login_sucess()
    else:
        password_not_recognised()
 
  else:
        user_not_found()
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)
  
def register_user():
  username_info = username.get()
  password_info = password.get()
  file=open(username_info, "w")
  file.write(username_info+"\n")
  file.write(password_info)
  file.close()
  username_entry.delete(0, END)
  password_entry.delete(0, END)
  Label(register_screen, text = "Registration Sucess", fg = "green" ,font = ("calibri", 11)).place(x=10,y=350)
  exit_registerscreen()
  main_screen()

def user_not_found():
  global usercheck_screen
  usercheck_screen = Toplevel(screen)
  usercheck_screen.title("Success")
  usercheck_screen.geometry("150x100")
  Label(usercheck_screen, text = "User Not Found").pack()
  Button(usercheck_screen, text = "OK", command =exit_usercheck).pack()

def password_not_recognised():
  global passcheck_screen
  passcheck_screen = Toplevel(screen)
  passcheck_screen.title("Success")
  passcheck_screen.geometry("150x100")
  Label(passcheck_screen, text = "Password Error").pack()
  Button(passcheck_screen, text = "OK", command =exit_passcheck).pack()

def login_sucess():
  global logincheck_screen
  
  logincheck_screen = Tk()
  logincheck_screen.resizable(width=False, height=False)
  width_of_window = 1280
  height_of_window = 720
  screen_width = logincheck_screen.winfo_screenwidth()
  screen_height = logincheck_screen.winfo_screenheight()
  x_coordinate = (screen_width/2) - (width_of_window/2)
  y_coordinate = (screen_height/2) - (height_of_window/2)
  logincheck_screen.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))

  logincheck_screen.title("Loading Game...")
  logincheck_screen.configure(background="#EEEEEE")
  load_banner = PhotoImage(file="Login Banner.png")
  Label(image=load_banner).place(x=0,y=0)
  load_gif = PhotoImage(file="Looping Gif.png")
  Label(image=load_gif,borderwidth=0).place(x=250,y=96.5)
  
  Label(logincheck_screen, text = "Login Sucess: Loading Game... ", borderwidth=2,bg = "#EEEEEE", font = ("calibri bold", 14)).place(x=10,y=115)
  
  exit_mainscreen()
  logincheck_screen.mainloop()

def exit_usercheck():
    usercheck_screen.destroy()
    
def exit_passcheck():
    passcheck_screen.destroy()

def exit_logincheck():
    logincheck_screen.destroy()

def exit_mainscreen():
    screen.destroy()

def exit_registerscreen():
    register_screen.destroy()

def exit_allscreen():
    screen.destroy() and passcheck_screen.destroy() and usercheck_screen.destroy() and register_screen.destroy() and logincheck_screen.destroy()
     
def back_screen():
  exit_registerscreen()
  main_screen()

main_screen()
