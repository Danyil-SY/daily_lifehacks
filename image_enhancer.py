# Improve image quality properties the PIL library

from PIL import Image
from PIL import ImageEnhance
import os

# Set the path to your folder containing the images and enhance factors
folder_path = r'path/to/your/folder'

contrast_factor = 1.0 # Adjust the contrast
brightness_factor = 1.0 # Adjust the brightness
sharpness_factor = 1.0  # Adjust the sharpness
color_factor = 1.0 # # Adjust the color balance

# Function to emprove images in the folder
def enhance_images_in_folder(folder_path, contrast_factor, brightness_factor, sharpness_factor, color_factor):
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
            image_path = os.path.join(folder_path, filename)
            image = Image.open(image_path)
            
            enhancer = ImageEnhance.Contrast(image) 
            enhanced_image = enhancer.enhance(contrast_factor)
            
            enhancer = ImageEnhance.Brightness(image) 
            enhanced_image = enhancer.enhance(brightness_factor)

            enhancer = ImageEnhance.Color(image)
            enhanced_image = enhancer.enhance(color_factor)

            enhancer = ImageEnhance.Sharpness(image)
            enhanced_image = enhancer.enhance(sharpness_factor)
            
            enhanced_image.save(os.path.join(folder_path, 'enhanced_' + filename))
            print(f"Enhanced {filename}")

# Call the function to enhance images
enhance_images_in_folder(folder_path, contrast_factor, brightness_factor, sharpness_factor, color_factor)
