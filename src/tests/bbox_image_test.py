from PIL import Image

# Load the block image
img = Image.open("../../assets/blocks/1x1/Stone Block sprite.png").convert("RGBA")

# Find the bounding box of all non-transparent pixels
bbox = img.getbbox()

# Crop to that bounding box
cropped = img.crop(bbox)
new_image = cropped.crop((0, 4, 16, 20))

# Save the cropped image
new_image.save("block_cropped.png")

print("Saved cropped image.")