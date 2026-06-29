from PIL import Image
import json


def is_valid_pixel(pixel): # Checks if the pixel is out of bounds of the image  
    return

def calculate_average_rgb_5x4(pixels, start_pixel):
    x, y = start_pixel
    width, height = 5, 4
    total_pixels = width * height

    chosen_pixels = []
    
    # Iterate through all pixels in 5x4 area and add to the list "chosen_pixels"

    for i in range(width):
        for k in range(height):
            if is_valid_pixel(pixels[x + i, y + k]) == True:
                chosen_pixels.append(pixels[x + i, y + k])
            else:
                return False
            
    red_value = sum(p[0] for p in chosen_pixels) // len(total_pixels) # get average RED value of the image by summing as red_value of each pixel p[0] and dividing by total pixels in image
    green_value = sum(p[1] for p in chosen_pixels) // len(total_pixels) # get average GREEN value
    blue_value = sum(p[2] for p in chosen_pixels) // len(total_pixels) # get average BLUE value

    average_rgb_value = (red_value, green_value, blue_value)

    with open("../assets/json-data")
    return average_rgb_value



def calculate_all_area_rgb_averages(image, start_pixel=None): # Calculates average RGB value of all size regions (block sizes) starting from "start_pixel"

    if start_pixel == None:
        start_pixel = [0, 0]
    

    pixels = image.load() # Now the pixels in the image can be acceses as a point in a 2D coordinate system

    average_5x4 = calculate_average_rgb_5x4()
    average_4x4 = calculate_average_rgb_4x4()
    average_4x3 = calculate_average_rgb_4x3()
    average_3x3 = calculate_average_rgb_3x3()
    average_3x2 = calculate_average_rgb_3x2()
    average_2x4 = calculate_average_rgb_2x4()
    average_2x3 = calculate_average_rgb_2x3()
    average_2x2 = calculate_average_rgb_2x2()
    average_2x1 = calculate_average_rgb_2x1()
    average_1x3 = calculate_average_rgb_1x3()
    average_1x2 = calculate_average_rgb_1x2()
    average_1x1 = calculate_average_rgb_1x1()


    