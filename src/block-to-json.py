import json
from pathlib import Path
from PIL import Image

EXCLUDED_FOLDERS = {"input", "json-data"} # Use set for O(1) lookup time

SIZES_NAMES = {
    "1x1": "blocks-1x1",
    "2x2": "blocks-2x2",
    "1x3": "blocks-1x3",
    "2x1": "blocks-2x1",
    "1x2": "blocks-1x2",
    "2x4": "blocks-2x4",
    "3x2": "blocks-3x2",
    "3x3": "blocks-3x3",
    "2x3": "blocks-2x3",
    "4x4": "blocks-4x4",
    "4x3": "blocks-4x3",
    "5x4": "blocks-5x4"
}


blocks = {}

for folder in Path("../assets/blocks").iterdir(): # Returns all items in dir as Path objects (folders)
    if folder.name in EXCLUDED_FOLDERS:
        continue

    for file in folder.iterdir(): 
        if file.suffix.lower() == ".png" and "sprite" in file.stem.lower(): # If the file is a png AND it contains the work block
        

            image = Image.open(file) # File is a Path object so needs to be opened using Image library
            image = image.convert("RGBA") # Set Image Mode to RBGA

            pixels = list(image.getdata()) # Returns the values of each pixel is a tuple (R, G, B)
            valid_pixels = [p for p in pixels if p[3] > 0] # Filters transaparent pixels


            red_value = sum(v[0] for v in valid_pixels) // len(pixels) # get average RED value of the image by summing as red_value of each pixel p[0] and dividing by total pixels in image
            green_value = sum(v[1] for v in valid_pixels) // len(pixels) # get average GREEN value
            blue_value = sum(v[2] for v in valid_pixels) // len(pixels) # get average BLUE value

            average_rgb = (red_value, green_value, blue_value)

            blocks[file.stem] = average_rgb

        file_name = SIZES_NAMES.get(folder.name)
        with open(f"../assets/json-data/{file_name}", "w") as f:
            json.dump(blocks, f, indent=4) # dump() converts python data into json format so we convert the "blocks" dictionary into json format

        

