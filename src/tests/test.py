from PIL import Image, ImageTk
import numpy as np
import customtkinter as ctk
import tkinter as tk
from math import floor
import random 
from tkinter import filedialog

def button_pressed():
    print("You just presses the button little bro")
    open_image()


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


app = ctk.CTk()
app.title("Testing the GUI")
app.geometry("600x400")

button_text_size = 5
button_font = ctk.CTkFont(family="Mont Heavy DEMO", size=button_text_size)
button = ctk.CTkButton(app, text="Click me", command=button_pressed, font=button_font, fg_color="purple", hover_color="#660042")
button.place(relx=0.5, rely=0.25, relwidth=0.4, relheight=0.1, anchor="center")


def open_image():
    image_file = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[    
            ("Image files", "*.png *.jpg *.jpeg *.gif *.bmp"),
            ("All files", "*.*")
        ]
    )

    if image_file:
        image 
    image_frame = ctk.CTkFrame(app)
    image_frame.pack(padx=20, pady=20)


    image_label = ctk.CTkLabel(image_frame)

    image_label.pack(padx=20, pady=20)

def resize_text(event): 
    if event.widget == app:
        window_width = event.width / 600
        window_height = event.height / 400
        scale = min(window_height, window_width)



        new_font_size = max(int(button_text_size * scale), 1)
        button_font.configure(size=new_font_size)


def button_enter(event):

    x = random.uniform(0.2, 0.7)
    y = random.uniform(0.2, 0.7)
    # button.place_configure(relx=x, rely=y)

def button_leave(event):
    varia = random.randint(0, 7)
    text_info = ["Damn bro, why u so slow",
                 "Yeah ur gonna have to try harder than that",
                 "They call bro IShowSlow",
                 "AHHHHHHH CLICK ME ALREADY",
                 "Skill Issue",
                 "Milanbot", 
                 "Just give up already",
                 "How do you keep getting worse?"
                 "Anytime now.........."
                ]             
    button.configure(text=text_info[varia])

app.bind("<Configure>", resize_text)
button.bind("<Enter>", button_enter)
button.bind("<Leave>", button_leave)
app.mainloop()

