# Resize all images in a folder

import os
from PIL import Image

def resize_images_in_folder(folder_path, output_folder, width, height):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Check if the current item is a file and has an image extension
        if os.path.isfile(file_path) and any(filename.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.gif']):
            # Open the image file
            image = Image.open(file_path)

            # Resize the image
            resized_image = image.resize((width, height))

            # Save the resized image to the output folder
            output_path = os.path.join(output_folder, filename)
            resized_image.save(output_path)

            print(f"Resized image saved: {output_path}")

    print("Image resizing completed!")

# Provide the folder path containing the images
folder_path = "path/to/folder"
# Provide the output folder path where the resized images will be saved
output_folder = "path/to/save/folder"
# Provide the desired width and height for the resized images
width = 1000
height = 747
resize_images_in_folder(folder_path, output_folder, width, height)