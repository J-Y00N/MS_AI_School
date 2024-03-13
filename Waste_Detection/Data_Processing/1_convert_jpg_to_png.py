from PIL import Image, ImageOps
import os

# Path to the 'Training' folder
training_dir = 'dataset/train/image/'

# Get a list of all subdirectories (image folders) within the 'Training' folder
image_dirs = [d for d in os.listdir(training_dir) if os.path.isdir(os.path.join(training_dir, d))]

# Desired size for the PNG images (640x640)
target_size = (640, 640)

for image_dir in image_dirs:
    # Path to the image folder within the 'Training' folder
    current_image_dir = os.path.join(training_dir, image_dir)

    # Path to the directory where you want to save the PNG images (XX_png)
    output_dir = os.path.join(training_dir, f'{image_dir}_png')

    # Check if the output directory exists, and create it if not
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Process images in the current image folder
    for root, dirs, files in os.walk(current_image_dir):
        for jpg_file in files:
            if jpg_file.endswith(".jpg"):
                # Open the JPG image
                img = Image.open(os.path.join(root, jpg_file))

                # Calculate the resizing dimensions while maintaining aspect ratio
                img.thumbnail(target_size)

                # Create a new blank image with the target size
                new_img = Image.new("RGB", target_size, (0, 0, 0))

                # Calculate the position to center the image
                left = (target_size[0] - img.width) // 2
                top = (target_size[1] - img.height) // 2

                # Paste the resized image onto the blank image
                new_img.paste(img, (left, top))

                # Create the output PNG file name
                png_file = os.path.splitext(jpg_file)[0] + ".png"

                # Save the PNG image to the output directory (XX_png)
                output_path = os.path.join(output_dir, png_file)
                new_img.save(output_path, "PNG")
                print(f"{jpg_file} -> {png_file}")

    print(f"Conversion and resizing with padding completed for '{image_dir}' folder. Output saved in '{output_dir}'.")