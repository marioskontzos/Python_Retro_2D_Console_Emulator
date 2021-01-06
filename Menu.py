import sys,os
import pygame
import MenuPictures_Sound
from tkinter import *
from PIL import Image, ImageTk
#import Image, ImageT
import subprocess
#import tkinter

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

#Adapt Window Graphics
info = pygame.display.Info()
display_width = info.current_w
display_height = info.current_h
print(display_width,display_height)
pygame.quit()

path = "C:/Users/marios/Documents/Tutorials-Projects/Personal/Python-VScode/ThesisRetroArcadeGamingMachine/MenuPictures_Sound/"

class full_Screen():

    def __init__(self):
        self.root = Tk()
        self.root.title('')
        self.root.attributes('-fullscreen', True)
        self.frame = Frame(self.root)
        self.frame.pack()
        self.state = False
        #self.root.bind("<Escape>", self.end_fullscreen)

    def end_fullscreen(self, event=None):
        self.state = False
        self.root.attributes("-fullscreen", False)
        return "break"

class about_Screen:
    def __init__(self,root):
        self.top = Toplevel(root)
        self.top.title("About this Operating System...")
        self.text = ("Kappa OS is a simple game operating system developed in order to teach"
                    +"the core building technics of an OS. This is a simulation of old gaming machines "
                    +"with modern development technics and infrastructure using the games as " 
                    +"presentation tools. The user can be a simple person"
                    +"intending to just learn the fundamentals of an OS and especially its connection "
                    +"with video games and how we end up with the gaming machines in our lives."
                    +"Or maybe a developer is interested to learn, improve developing skills and "
                    +"use it as guideline in order for him to produce his own custom OS.\n"
                    +"\nPowered by Kontzos Marios - Siatis Dimitris")
    
    def print_message(self):
        self.message = Message(self.top, text = self.text, bg = "white", font = "SLAB_SERIF",relief = RAISED)
        self.message.pack()
        self.top.geometry("+%d+%d" % ((display_width / 2 ) - 220, (display_height / 2 )+ 80))
        

def start_Star_Guardian():
    sys.path.append('C:/Users/marios/Documents/Tutorials-Projects/Personal/Python-VScode/ThesisRetroArcadeGamingMachine/StarGuardian')
    from Star_Guardian import start
    start()

def start_Snake():
    sys.path.append('C:/Users/marios/Documents/Tutorials-Projects/Personal/Python-VScode/ThesisRetroArcadeGamingMachine/Anaconda/')
    from Main import game_Start
    game_Start()

def system_Shutdown(): 
    #Option 1)Windows, 2)Linux, 3)Testing
    #os.system("shutdown /s /t 1")
    #os.system("shutdown now -f")
    sys.exit(0)

def system_Reboot(): 
    #Option 1)Windows, 2)Linux, 3)Testing
    #os.system("shutdown /r /t 1")
    #os.system("reboot")
    sys.exit(0)

def about_Button():
    x = about_Screen(window.root)
    x.print_message()
    
window = full_Screen()

#Main Window
canv = Canvas(window.root, bg = "grey", height = display_height + 10, width = display_width + 10)
canv.pack()

#Images
#background_Image = ImageTk.PhotoImage(file = path + "Brick_wall2_1366x768.jpg")
#background_Image = ImageTk.PhotoImage(file = path + "Mixed_background_2_1366x768.jpg")
background_Image = ImageTk.PhotoImage(file = path + "Mixed_background_2_1900x1080.jpg")
#background_Image = ImageTk.PhotoImage(file = path + "Mixed_background_1366x768.jpg")
background_label = Label(window.root, image = background_Image)
background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
reboot_button_Image = ImageTk.PhotoImage(file = path + "Reboot_Icon_40x40.jpg")
shutdown_button_Image = ImageTk.PhotoImage(file = path + "Shutdown_Icon_40x40.jpg")
snake_button_Image = ImageTk.PhotoImage(file = path + "Anaconda_30x30.jpg")
guardian_button_Image = ImageTk.PhotoImage(file = path + "Hero_Spaceship_Bee_30x30.jpg")

label_Title = Label(window.root, text = "Welcome to kappa gaming OS", height = 2, width = 40, font = "SLAB_SERIF", bg = "grey")
label_Title.place(relx = 0.5, rely = 0.028, anchor = CENTER)
label_Version = Label(window.root, text = "Version 1.01.000.000", height = 1, width = 17, font = "SLAB_SERIF", bg = "grey")
label_Version.place(relx = 0.94, rely = 0.984, anchor = CENTER)

#Shutdown and reboot buttons for windows alternative method right on button call, no need for custom function
#button3 = Button(window.root, command = lambda: subprocess.call(["shutdown.exe", "-f", "-r", "-t", "0"]), height = 25, width = 38, bg = "red", image = shutdown_button_Image)
#button4 = Button(window.root, text = "Exit and Shutdown", command = lambda: subprocess.call(["shutdown.exe", "-f", "-s", "-t", "0"]), height = 25, width = 38, bg = "red", image = reboot_button_Image)

button_Guardian = Button(window.root, text = "StarGuardian", command = start_Star_Guardian, height = 25, width = 125, font = "SLAB_SERIF", bg = "grey", image = guardian_button_Image, compound = LEFT)
button_Snake = Button(window.root, text = "Anaconda", command = start_Snake, height = 25, width = 125, font = "SLAB_SERIF", bg = "grey", image = snake_button_Image, compound = LEFT)
button_Reboot = Button(window.root, command = system_Reboot, height = 25, width = 38, bg = "red", image = reboot_button_Image)
button_Shutdown = Button(window.root, command = system_Shutdown, height = 25, width = 38, bg = "red", image = shutdown_button_Image)
button_About = Button(window.root, text = "About", command = about_Button, height = 1, width = 14, font = "SLAB_SERIF", bg = "grey")

button_Guardian.place(relx = 0.5, rely = 0.457, anchor = CENTER)
button_Snake.place(relx = 0.5, rely = 0.5, anchor = CENTER)
button_Reboot.place(relx = 0.017, rely = 0.980, anchor = CENTER)
button_Shutdown.place(relx = 0.048, rely = 0.980, anchor = CENTER)
button_About.place(relx = 0.5, rely = 0.570, anchor = CENTER)

window.root.mainloop()