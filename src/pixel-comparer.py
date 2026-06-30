from PIL import Image
import json
import os


def find_file(file_name):
    blocks_folder = "../assets/blocks"

    for root, folder, file in os.walk(blocks_folder):
        if file != []: # if File is not an empty list
            for block_name in file:
                if file_name == block_name:
                        block_filepath = os.path.join(blocks_folder, block_name)

    return block_filepath

def is_valid_pixel(pixel): # Checks if the pixel is out of bounds of the image  
    return

def calculate_average_rgb_5x4(pixels, start_pixel):
    block_size = "5x4"
    json_data_filename = "blocks-5x4.json"
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

    average_rgb_value_of_area = (red_value, green_value, blue_value)

    with open(f"../assets/json-data/{json_data_filename}") as file: # Takes the JSON dictionary of 5x4 blocks and converts into PYTHON dictionary
        blocks = json.load(file)


    best_colour_match = ("", 9999) # Random High number so I can compare to colour diffrence
    for k, v in blocks.items():
        # k is the name of the block
        # v is the RGB value of that block
        colour_difference = ( # Calculated how similar the colours are in the RGB colour space ( I say RGB because there are diffrent colour spaces. Might change it lter)
            abs(average_rgb_value_of_area[0] - v[0]) +
            abs(average_rgb_value_of_area[1] - v[1]) +
            abs(average_rgb_value_of_area[2] - v[2]) 

        )

        if colour_difference < best_colour_match[1]:
            best_colour_match = (f"{k}.png", colour_difference, block_size)


    return best_colour_match



def calculate_all_area_rgb_averages(image, start_pixel=None): # Calculates average RGB value of all size regions (block sizes) starting from "start_pixel"

    if start_pixel == None:
        start_pixel = [0, 0]
    

    pixels = image.load() # Now the pixels in the image can be acceses as a point in a 2D coordinate system


    best_matches_all_sizes = [
        calculate_average_rgb_5x4(),
        calculate_average_rgb_4x4(),
        calculate_average_rgb_4x3(),
        calculate_average_rgb_3x3(),
        calculate_average_rgb_3x2(),
        calculate_average_rgb_2x4(),
        calculate_average_rgb_2x3(),
        calculate_average_rgb_2x2(),
        calculate_average_rgb_2x1(),
        calculate_average_rgb_1x3(),
        calculate_average_rgb_1x2(),
        calculate_average_rgb_1x1()
    ]
    

    best_match_overall = min(best_matches_all_sizes)


    block_filepath = find_file(best_match_overall[0]) # index [0] contains the filename
    block_image = Image.open(block_filepath).convert("RGBA")  # Needs to be RGBA so we can drop the transparent pixels
    
    bounding_box = block_image.getbbox()
    cropped_block = block_image.crop(bounding_box)
    

















    