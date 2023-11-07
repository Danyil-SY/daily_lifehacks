# Make a background color more light

from PIL import Image
import os

# Set the path to your folder containing the images and enhance factor
folder_path = r'path/to/your/folder'

# Function to improve images in the folder
def enhance_images_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
            image_path = os.path.join(folder_path, filename)
            image = Image.open(image_path)

            # Convert the image to RGB mode if it's not in RGB already
            image = image.convert("RGB")

            # Iterate over each pixel to adjust the colors
            pixels = image.load()
            for i in range(image.size[0]):
                for j in range(image.size[1]):
                    r, g, b = pixels[i, j]
                    if r > 170 and g < 110 and b < 110:  # Adjust the threshold values as needed
                        pixels[i, j] = (r+30, g+10, b+10)  # Adjust the RGB formula
            image.save(os.path.join(folder_path, 'enhanced_' + filename))
            print(f"Enhanced {filename}")

# Call the function to enhance images
enhance_images_in_folder(folder_path)
