import pygame
import random
from tkinter import *
import os
import time

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
  
  Label(register_screen, text = "REGISTER ", borderwidth=2,bg = "#EEEEEE", font = ("calibri bold", 14)).place(x=10,y=115) 
  Label(register_screen, text = "Username: ").place(x=10,y=170)
  
  username_entry = Entry(register_screen, textvariable = username).place(x=10,y=200)
  Label(register_screen, text = "Password: ").place(x=10,y=240)
  password_entry =  Entry(register_screen, textvariable = password).place(x=10,y=270)


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
        main_menu()
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

def main_menu():
  global mainmenu_screen

  screen.destroy() and passcheck_screen.destroy() and usercheck_screen.destroy() and logincheck_screen.destroy()
    
  mainmenu_screen = Tk()
  mainmenu_screen.title("Competitive Tetris")
  mainmenu_screen.resizable(width=False, height=False)
  screen_width = mainmenu_screen.winfo_screenwidth()
  screen_height = mainmenu_screen.winfo_screenheight()
  width_of_window = 1280
  height_of_window = 720
  x_coordinate = (screen_width/2) - (width_of_window/2)
  y_coordinate = (screen_height/2) - (height_of_window/2)
  mainmenu_screen.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))

  mainmenu_screen.configure(background="#ABABAB")
  main_banner = PhotoImage(file="Client Banner.png")
  Label(image=main_banner,borderwidth=0).place(x=0,y=0)
  main_leaderboards_png = PhotoImage(file="Client Leaderboards.png")
  Label(image=main_leaderboards_png,borderwidth=0).place(x=1092,y=100)

  Label(mainmenu_screen, text = " PERSONAL BEST \n SCORE", borderwidth=2,bg = "#373737", font = ("calibri bold", 14),fg="#E9E9E9").place(x=1115,y=115)

  Button(text = "Introduction",height = 3, width = 80, command = main_introduction).place(x=370,y=200)
  Button(text = "Start New Game",height = 3, width = 80, command = main_newgame).place(x=370,y=325)
  Button(text = "Leader Boards",height = 3, width = 80, command = main_leaderboards).place(x=370,y=450)
  Button(text = "Options",height = 3, width = 32, command = main_options).place(x=370,y=575)
  Button(text = "Exit",height = 3, width = 32, command = main_exit).place(x=710,y=575)
  
  mainmenu_screen.mainloop()

def main_introduction():
    time.sleep(.1)

def main_newgame():
  global newgame_screen

  exit_mainmenu()

  newgame_screen = Tk()
  newgame_screen.title("Competitive Tetris")
  newgame_screen.resizable(width=False, height=False)
  screen_width = newgame_screen.winfo_screenwidth()
  screen_height = newgame_screen.winfo_screenheight()
  width_of_window = 1280
  height_of_window = 720
  x_coordinate = (screen_width/2) - (width_of_window/2)
  y_coordinate = (screen_height/2) - (height_of_window/2)
  newgame_screen.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))

  newgame_screen.configure(background="#ABABAB")
  newgame_banner = PhotoImage(file="Client Banner.png")
  Label(image=newgame_banner,borderwidth=0).place(x=0,y=0)
  newgame_leaderboards_png = PhotoImage(file="Client Leaderboards.png")
  Label(image=newgame_leaderboards_png,borderwidth=0).place(x=1092,y=100)

  Label(newgame_screen, text = " PERSONAL BEST \n SCORE", borderwidth=2,bg = "#373737", font = ("calibri bold", 14),fg="#E9E9E9").place(x=1115,y=115)

  Button(text = "Single Player",height = 3, width = 80, command = single_player).place(x=370,y=200)
  Button(text = "Two Player",height = 3, width = 80, command = two_player).place(x=370,y=325)
  Button(text = "Back",height = 3, width = 40, command = backto_mainmenu_newgame).place(x=370,y=450)
  
  newgame_screen.mainloop()

def main_leaderboards():
  global leaderboards_screen

  exit_mainmenu()

  leaderboards_screen = Tk()
  leaderboards_screen.title("Competitive Tetris")
  leaderboards_screen.resizable(width=False, height=False)
  screen_width = leaderboards_screen.winfo_screenwidth()
  screen_height = leaderboards_screen.winfo_screenheight()
  width_of_window = 1280
  height_of_window = 720
  x_coordinate = (screen_width/2) - (width_of_window/2)
  y_coordinate = (screen_height/2) - (height_of_window/2)
  leaderboards_screen.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))

  leaderboards_screen.configure(background="#ABABAB")
  leaderboards_banner = PhotoImage(file="Client Banner.png")
  Label(image=leaderboards_banner,borderwidth=0).place(x=0,y=0)
  leaderboards_leaderboards_png = PhotoImage(file="Client Leaderboards.png")
  Label(image=leaderboards_leaderboards_png,borderwidth=0).place(x=1092,y=100)

  Label(leaderboards_screen, text = " PERSONAL BEST \n SCORE", borderwidth=2,bg = "#373737", font = ("calibri bold", 14),fg="#E9E9E9").place(x=1115,y=115)
  Label(leaderboards_screen, text = " LEADER BOARDS ", borderwidth=2,bg = "#373737", font = ("calibri bold", 18),fg="#E9E9E9").place(x=575,y=115)
  Label(leaderboards_screen, text = " TOP 50 ", borderwidth=2,bg = "#373737", font = ("calibri bold", 16),fg="#E9E9E9").place(x=625,y=160)

  Button(text = "Back",height = 2, width = 24, command = backto_mainmenu_leaderboards).place(x=370,y=600)
  
  leaderboards_screen.mainloop()

def main_options():
  global options_screen

  exit_mainmenu()

  options_screen = Tk()
  options_screen.title("Competitive Tetris")
  options_screen.resizable(width=False, height=False)
  screen_width = options_screen.winfo_screenwidth()
  screen_height = options_screen.winfo_screenheight()
  width_of_window = 1280
  height_of_window = 720
  x_coordinate = (screen_width/2) - (width_of_window/2)
  y_coordinate = (screen_height/2) - (height_of_window/2)
  options_screen.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))

  options_screen.configure(background="#ABABAB")
  options_banner = PhotoImage(file="Client Banner.png")
  Label(image=options_banner,borderwidth=0).place(x=0,y=0)
  options_leaderboards_png = PhotoImage(file="Client Leaderboards.png")
  Label(image=options_leaderboards_png,borderwidth=0).place(x=1092,y=100)

  Label(options_screen, text = " PERSONAL BEST \n SCORE", borderwidth=2,bg = "#373737", font = ("calibri bold", 14),fg="#E9E9E9").place(x=1115,y=115)
  Label(options_screen, text = " OPTIONS ", borderwidth=2,bg = "#373737", font = ("calibri bold", 18),fg="#E9E9E9").place(x=615,y=115)

  Button(text = " SOUND OFF/ON ",height = 3, width = 40, command = sound_off_on).place(x=370,y=200)
  Button(text = " MUSIC OFF/ON ",height = 3, width = 40, command = music_off_on).place(x=370,y=275)
  Button(text = " CONTROLS ",height = 3, width = 20, command = menu_controls).place(x=370,y=350)
  Button(text = " Back ",height = 3, width = 24, command = backto_mainmenu_options).place(x=750,y=350)
  
  options_screen.mainloop()
  

def single_player():
  time.sleep(0.1)

def two_player():
  time.sleep(0.1)

def backto_mainmenu_newgame():
    exit_newgame()
    main_menu()

def backto_mainmenu_leaderboards():
    exit_leaderboards()
    main_menu()

def backto_mainmenu_options():
    exit_options()
    main_menu()

def exit_mainmenu():
    mainmenu_screen.destroy()

def exit_newgame():
    newgame_screen.destroy()

def exit_leaderboards():
    leaderboards_screen.destroy()

def exit_options():
    options_screen.destroy()

def main_exit():
    exit_mainmenu()

def menu_controls():
  global controls_screen

  exit_options()

  controls_screen = Tk()
  controls_screen.title("Competitive Tetris")
  controls_screen.resizable(width=False, height=False)
  screen_width = controls_screen.winfo_screenwidth()
  screen_height = controls_screen.winfo_screenheight()
  width_of_window = 1280
  height_of_window = 720
  x_coordinate = (screen_width/2) - (width_of_window/2)
  y_coordinate = (screen_height/2) - (height_of_window/2)
  controls_screen.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))

  controls_screen.configure(background="#ABABAB")
  controls_banner = PhotoImage(file="Client Banner.png")
  Label(image=controls_banner,borderwidth=0).place(x=0,y=0)
  controls_leaderboards_png = PhotoImage(file="Client Leaderboards.png")
  Label(image=controls_leaderboards_png,borderwidth=0).place(x=1092,y=100)

  Label(controls_screen, text = " PERSONAL BEST \n SCORE", borderwidth=2,bg = "#373737", font = ("calibri bold", 14),fg="#E9E9E9").place(x=1115,y=115)
  Label(controls_screen, text = " CONTROLS ", borderwidth=2,width=40 ,bg = "#373737", font = ("calibri bold", 18),fg="#E9E9E9").place(x=400,y=115)
  Label(controls_screen, text = " PLAYER 1 ", borderwidth=2,width=20 ,bg = "#373737", font = ("calibri bold", 16),fg="#E9E9E9").place(x=400,y=165)
  Label(controls_screen, text = " PLAYER 2 ", borderwidth=2,width=20 ,bg = "#373737", font = ("calibri bold", 16),fg="#E9E9E9").place(x=700,y=165)

  Label(controls_screen, text = " MOVE LEFT ", borderwidth=2,width=20 ,bg = "#373737", font = ("calibri bold", 16),fg="#E9E9E9").place(x=400,y=250)
  Label(controls_screen, text = " MOVE RIGHT ", borderwidth=2,width=20 ,bg = "#373737", font = ("calibri bold", 16),fg="#E9E9E9").place(x=400,y=300)
  Label(controls_screen, text = " ROTATE ", borderwidth=2,width=20 ,bg = "#373737", font = ("calibri bold", 16),fg="#E9E9E9").place(x=400,y=350)
  Label(controls_screen, text = " ROTATE ", borderwidth=2,width=20 ,bg = "#373737", font = ("calibri bold", 16),fg="#E9E9E9").place(x=400,y=400)

  Label(controls_screen, text = " MOVE LEFT ", borderwidth=2,width=20 ,bg = "#373737", font = ("calibri bold", 16),fg="#E9E9E9").place(x=700,y=250)
  Label(controls_screen, text = " MOVE RIGHT ", borderwidth=2,width=20 ,bg = "#373737", font = ("calibri bold", 16),fg="#E9E9E9").place(x=700,y=300)
  Label(controls_screen, text = " ROTATE ", borderwidth=2,width=20 ,bg = "#373737", font = ("calibri bold", 16),fg="#E9E9E9").place(x=700,y=350)
  Label(controls_screen, text = " ROTATE ", borderwidth=2,width=20 ,bg = "#373737", font = ("calibri bold", 16),fg="#E9E9E9").place(x=400,y=400)
   
  Button(text = " Back ",height = 2, width = 24, command = backto_mainmenu_options).place(x=700,y=450)
  
  controls_screen.mainloop()

def sound_off_on():
    time.sleep(0.1)

def music_off_on():
    time.sleep(0.1)

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
