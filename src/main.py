from PIL import Image, ImageTk
import numpy as np
import customtkinter as ctk
import tkinter
from math import floor

# Set Theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Pixel Art Converter")
root.geometry("600x400")
img = None
image_label = None
preview_img = None
max_world_width = 300
max_world_height = 164
CONVERTABLE = False


def load_image():
    print("Button Pressed")
    global img # Python can read global variables but cannot assign them so we need to declare them global in every function
    path = tkinter.filedialog.askopenfilename(title="Image Selection",
        filetypes=[("Image Files", "*.jpg;*.png;*.jpeg;*.bmp;*.tiff;*.gif")]) # The Selected image's path

    if path: # If an image is chosen then we 
        img = Image.open(path) # Loads file into memory. PS (This is why we need to declare img global)
        print(f"Loaded: {path}")
        open_new_window(img) 

    


def sliding(value):
    global img, preview_img, image_label, slider_label, pixelated_size
    display_size = calculate_display_size(img)

    value = max(1, int(value)) #Why get max? In case  value is 0. Even if we set "from_" to 1 the GUI might still return 0.99, which int()
                               # Will round to 0. So we get the max of this incase the value returnes by the GUI is 0.
    slider_label.configure(text=value)
    img_resized = img.resize(
        (img.width // value, img.height // value),
        resample=Image.NEAREST    
    )

    pixel_art = img_resized.resize( # Upscale image back to the orginal size without adding detail (Nearest Neighbour)
        img.size,
        resample=Image.NEAREST
    ) 

    preview_img = ctk.CTkImage(
        light_image=pixel_art,
        dark_image=pixel_art,
        size=display_size

    )

    image_label.configure(image=preview_img)
    image_label.image = preview_img

    w, h = img_resized.size
    if w > max_world_width or h > max_world_height:
        image_size_label.configure(
            text=f"Image Size: {img_resized.size} (Image cannot fit in a world.)",
            text_color="red"
        )
    else:
        image_size_label.configure(
            text=f"Image Size: {img_resized.size}",
            text_color="white"
        )



def calculate_display_size(image):

    MAX_W, MAX_H = 600, 400

    scale = min(MAX_W / image.width, MAX_H / image.height, 1)

    display_size = ( # Resolution of the image scaled down to fit in a 600x400 box
        int(image.width * scale),
        int(image.height * scale)
    )

    return display_size



def create_preview_window(display_size):
    w, h = display_size

    new_window = ctk.CTkToplevel(root)
    new_window.geometry(f"{w + 200}x{h + 200}")
    new_window.title("Pixelated_Preview")

    return new_window


def create_image_size_label(window, image):
    global image_size_label

    if image.width > max_world_width or image.height > max_world_height:    
        image_size_label = ctk.CTkLabel(
            window,
            text=f"Image Size: {image.size} (Image cannot fit in a world)",
            font=("Arial", 18),
            text_color="red"
        )
    else:
        image_size_label = ctk.CTkLabel(
            window,
            text=f"Image Size: {image.size}",
            font=("Arial", 18),
            text_color="white"
        )


    image_size_label.pack(pady=(20, 0))

def create_image_frame(window):
     
    image_frame = ctk.CTkFrame(window) # Make a new Frame (basically a container for elements)
    image_frame.pack(
        padx=20,
        pady=20,
        fill="both",
        expand=True
    ) 
    # This frame will hold the image, i also give it padding
    # A frame doesnt have a resolution it just takes up all sapce available in the whole window. 
    # Due to padding from itself and other elements, it does not actually cover the whole screen

    return image_frame

def create_image_preview(frame, image, display_size):
    global preview_img, image_label

    preview_img = ctk.CTkImage( # CTKImage creates an image object so nothing is displayed yet 
        light_image=image,
        dark_image=image,
        size=display_size # Set the resolution at which the image should be displayed at
    ) 

    image_label = ctk.CTkLabel( # This actually displayed the image object
        frame,
        text="",
        image=preview_img # Image to display
    )

    # Stretches the Label to match the size of the frame, 
    # resulting in the image always being centered
    # Even when the window is resized
    #            vvvvvvvvvvvv

    image_label.pack(fill="both", expand=True)

def create_slider(window):
    global slider_label

    slider = ctk.CTkSlider(
        window,
        from_=1,
        to=100, 
        command=sliding
    )

    
    slider.pack(pady=(40,10), padx=40)
    slider.set(1)

    slider_label = ctk.CTkLabel(window, text="1")
    slider_label.pack(pady=10)

    #preview_img
def open_new_window(image):

    display_size = calculate_display_size(image)

    new_window = create_preview_window(display_size)

    create_image_size_label(new_window, image)

    image_frame = create_image_frame(new_window)

    create_image_preview(image_frame, image, display_size)

    create_slider(new_window)


file_but = ctk.CTkButton(root, text="Choose File to Convert", command=load_image)
file_but.pack(pady=40)

root.mainloop()


#img = Image.new("RGB", (64,64), color="blue")
#img.save ("../output/pixel_images/test_output.png")

#arr = np.array(img)
#print("Array shape: ", arr.shape)
#print("Test image saved to ../output/pixel_images/test_output.png")
3
#img = Image.open("../assets/input/Blackberry-pie-c418fda.jpg")

#img_resized = img.resize((img.width // 8 , img.height // 8), resample=Image.NEAREST)
#pixel_art = img_resized.resize((img_resized.height * 8, img_resized.width * 8), resample=Image.NEAREST) 
#pixel_art.show()