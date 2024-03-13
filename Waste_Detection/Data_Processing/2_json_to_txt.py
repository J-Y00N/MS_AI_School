import cv2
import json
import os

# Define the paths to your input and output folders
image_folder = './Training/image/A2_png'  # Folder containing converted and resized PNG images
json_folder = './Training/label/A2'  # Folder containing JSON files

# Create the output folder for YOLO-formatted .txt files
yolo_txt_folder = './Training/yolo_txt'
os.makedirs(yolo_txt_folder, exist_ok=True)

# Iterate through JSON files in the specified folder
for json_file in os.listdir(json_folder):
    if json_file.lower().endswith('.json'):
        json_file_path = os.path.join(json_folder, json_file)

        # Load the corresponding image
        image_name = os.path.splitext(json_file)[0] + ".png"
        image_path = os.path.join(image_folder, image_name)
        image = cv2.imread(image_path)

        if image is not None:
            original_width, original_height = 1847, 883
            target_size = 640
            x_scale = original_width / target_size
            y_scale = x_scale
            padding_size = int((target_size - (original_height / x_scale)) / 2)

            yolo_txt_path = os.path.join(yolo_txt_folder, os.path.splitext(json_file)[0] + ".txt")
            with open(yolo_txt_path, 'w') as yolo_txt_file:
                with open(json_file_path, 'r', encoding='utf-8') as stream:
                    try:
                        data = json.load(stream)
                        objects = data.get('objects', [])

                        for obj in objects:
                            annotation = obj.get('annotation', {})
                            coord = annotation.get('coord', {})
                            x = int(coord.get('x', 0.0) / x_scale)
                            y = int(coord.get('y', 0.0) / y_scale) + padding_size
                            width = int(coord.get('width', 0.0) / x_scale)
                            height = int(coord.get('height', 0.0) / y_scale)
                            class_id = obj.get('class_name', "Unknown")

                            # Convert bounding box coordinates to YOLO format
                            center_x = (x + width / 2) / target_size
                            center_y = (y + height / 2) / target_size
                            normalized_width = width / target_size
                            normalized_height = height / target_size

                            # Write YOLO-formatted data to the .txt file
                            yolo_txt_file.write(f"{class_id} {center_x} {center_y} {normalized_width} {normalized_height}\n")

                    except json.JSONDecodeError as exc:
                        print(f"Error decoding JSON in {json_file}: {exc}")

        else:
            print(f"Skipping {json_file}: Image not loaded.")