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



def calculate_average_rgb_and_best_match(pixels, start_pixel, size):
    block_size = size
    json_data_filename = f"blocks-{size}.json"
    x, y = start_pixel
    width, height = int(size[0]), int(size[2]) # Index of the {size} string where there is the numbers
    total_pixels = width * height

    chosen_pixels = []
    
    # Iterate through all pixels in chosen area {size} and add to the list "chosen_pixels"
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


    best_colour_match = ("", 9999, "") # Random High number so I can compare to colour diffrence
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

def crop_image(size, image_path):
    # Because size is a string I index it to get the numbers
    block_tile_width = int(size[0]) 
    block_tile_height = int(size[2])

    if size == "1x1": # Only 1x1 images need the 4 extra pixels cropped

        block_image = Image.open(image_path).convert("RGBA")  # Needs to be RGBA so we can drop the transparent pixels
    
        bounding_box = block_image.getbbox()
        removed_transparent_pixels_block = block_image.crop(bounding_box)

        cropped_block = removed_transparent_pixels_block.crop((0, 4, 16, 20))

        return (cropped_block, None)
    else:
        block_image = Image.open(image_path).convert("RGBA")  # Needs to be RGBA so we can drop the transparent pixels
    
        bounding_box = block_image.getbbox()
        removed_transparent_pixels_block = block_image.crop(bounding_box)

        width, height = removed_transparent_pixels_block.size

        empty_space_x = (16 * block_tile_width ) - width
        empty_space_y = (16 * block_tile_height ) - height

        offset_x = empty_space_y // 2
        offset_y = empty_space_y // 2

        return (removed_transparent_pixels_block, offset_x, offset_x)




       
def calculate_offset_for_big_blocks()

def calculate_all_area_rgb_averages(image, pixelated_image_size): # Calculates average RGB value of all size regions (block sizes) starting from "start_pixel"
    pixelated_image_width, pixelated_image_height = pixelated_image_size

    start_pixel = [0, 0]

    
    pixels = image.load() # Now the pixels in the image can be acceses as a point in a 2D coordinate system
    pixels_finished_processing = False

    while not pixels_finished_processing:
        best_matches_for_all_sizes = [
            calculate_average_rgb_and_best_match(pixels, start_pixel, "5x4"),
            calculate_average_rgb_and_best_match(pixels, start_pixel, "4x4"),
            calculate_average_rgb_and_best_match(pixels, start_pixel, "4x3"),
            calculate_average_rgb_and_best_match(pixels, start_pixel, "4x2"),
            calculate_average_rgb_and_best_match(pixels, start_pixel, "3x4"),
            calculate_average_rgb_and_best_match(pixels, start_pixel, "3x3"),
            calculate_average_rgb_and_best_match(pixels, start_pixel, "3x2"),
            calculate_average_rgb_and_best_match(pixels, start_pixel, "2x4"),
            calculate_average_rgb_and_best_match(pixels, start_pixel, "2x3"),
            calculate_average_rgb_and_best_match(pixels, start_pixel, "2x2"),
            calculate_average_rgb_and_best_match(pixels, start_pixel, "2x1"),
            calculate_average_rgb_and_best_match(pixels, start_pixel, "1x4"),
            calculate_average_rgb_and_best_match(pixels, start_pixel, "1x3"),
            calculate_average_rgb_and_best_match(pixels, start_pixel, "1x2"),
            calculate_average_rgb_and_best_match(pixels, start_pixel, "1x1"),
        ]


        best_match_overall = min(best_matches_for_all_sizes, key=lambda each_list: each_list[1])
        FILENAME, COLOUR_DIFFERENCE, BLOCK_SIZE = best_match_overall


        block_filepath = find_file(FILENAME) # index [0] contains the filename
        cropped_block = crop_image(BLOCK_SIZE, block_filepath)

        canvas = Image.new(
            "RGBA", # Canvas mode
            (pixelated_image_width, pixelated_image_height),
            (0, 0, 0, 0)
        )

        canvas.paste(
            cropped_block,
            ()
        )
        
        start_pixel_x = start_pixel[0] + int(BLOCK_SIZE[0])
        start_pixel_y = start_pixel[1] + int(BLOCK_SIZE[2])
    
        start_pixel = [start_pixel_x, start_pixel_y]

















    