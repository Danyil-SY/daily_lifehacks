# Cropt all images at a specific point in a folder and save them in the same location

from PIL import Image
import os

# Set the path to your folder containing the images
folder_path = r'path/to/your/folder'

# Set the coordinates for cropping (x_pos, y_pos, width+x_pos, height+y_pos)
crop_point = (765, 381, 1789, 1145) 

# Function to crop images in the folder
def crop_images_in_folder(folder_path, crop_point):
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
            image_path = os.path.join(folder_path, filename)
            image = Image.open(image_path)
            cropped_image = image.crop(crop_point)
            cropped_image.save(os.path.join(folder_path, 'cropped_' + filename))
            print(f"Cropped {filename} at {crop_point}")

# Call the function to crop images
crop_images_in_folder(folder_path, crop_point)
