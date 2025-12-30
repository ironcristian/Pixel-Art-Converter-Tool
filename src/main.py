from PIL import Image, ImageTk
import numpy as np
import customtkinter as ctk
import tkinter

# Set Theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Pixel Art Converter")
root.geometry("600x400")
img = None

def load_image():
    print("Button Pressed")
    global img
    path = tkinter.filedialog.askopenfilename(title="Image Selection",
        filetypes=[("Image Files", "*.jpg;*.png;*.jpeg;*.bmp;*.tiff;*.gif")])

    if path: 
        img = Image.open(path)
        print(f"Loaded: {path}")
        open_new_window(img)

    

def open_new_window(image):
    new_window = ctk.CTkToplevel(root)
    new_window.geometry("600x400")
    new_window.title("Pixelated Preview")

    image_frame = ctk.CTkFrame(new_window)
    image_frame.pack(padx=20, pady=20,)

    image_label = ctk.CTkLabel(image_frame, text="")
    image_label.pack()


    tk_img = ImageTk.PhotoImage(image)
    image_label.configure(image=tk_img)
    image_label.image = tk_img



file_but = ctk.CTkButton(root, text="Choose File to Convert", command=load_image)
file_but.pack(pady=40)

root.mainloop()


#img = Image.new("RGB", (64,64), color="blue")
#img.save ("../output/pixel_images/test_output.png")

#arr = np.array(img)
#print("Array shape: ", arr.shape)
#print("Test image saved to ../output/pixel_images/test_output.png")

#img = Image.open("../assets/input/Blackberry-pie-c418fda.jpg")

#img_resized = img.resize((img.width // 8 , img.height // 8), resample=Image.NEAREST)
#pixel_art = img_resized.resize((img_resized.height * 8, img_resized.width * 8), resample=Image.NEAREST) 
#pixel_art.show()