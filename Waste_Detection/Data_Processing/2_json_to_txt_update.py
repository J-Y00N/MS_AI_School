import json
import os

# json 파일 경로
json_folder = 'C:/Users/54/Desktop/Project/dataset/extract/label'  # Folder containing JSON files

# txt 파일로 만들어서 어디 저장할지 경로
yolo_txt_folder = 'C:/Users/54/Desktop/Project/dataset/extract/extractlabel'
os.makedirs(yolo_txt_folder, exist_ok=True)

class_mapping = {
    'c_1': 0,
    'c_2_01': 0,
    'c_2_02': 0, #~paper
    'c_3': 1, #can
    'c_4_01_02': 2,
    'c_4_02_01_02': 2,
    'c_4_02_02_02': 2,
    'c_4_02_03_02': 2,
    'c_4_03': 2, #~glass
    'c_5_02': 3, #pet
    'c_6': 4, #plastic
    'c_7': 5, #vinyl
    'c_1_01': 0,
    'c_2_02_01': 0, #~paper
    'c_3_01': 1, #can
    'c_4_03_01': 2, #glass
    'c_5_01_01': 3,
    'c_5_02_01': 3, #~pet
    'c_6_01': 4, #plastic
    'c_7_01': 5, #vinyl
    'c_4_01_01': 2,
    'c_4_02_01_01': 2,
    'c_4_02_02_01': 2,
    'c_4_02_03_01': 2, #~glass
    'c_5_01': 3, #pet
    'c_8_01': 6,
    'c_8_02': 6,
    'c_8_01_01': 6, #~form
    'c_9': 7, #battery
}



# json 파일 읽음
for json_file in os.listdir(json_folder):
    if json_file.lower().endswith('.json'):
        json_file_path = os.path.join(json_folder, json_file)

        yolo_txt_path = os.path.join(yolo_txt_folder, os.path.splitext(json_file)[0] + ".txt")

        with open(yolo_txt_path, 'w') as yolo_txt_file:
            with open(json_file_path, 'r', encoding='utf-8') as stream:
                try:
                    data = json.load(stream)
                    objects = data.get('objects', [])

                    resolution = data["Info"]["RESOLUTION"]
                    parts = resolution.split("/")
                    original_width= float(parts[0].strip())
                    original_height= float(parts[1].strip())
                    target_size = 1280
                    x_scale = original_width / target_size

                    if x_scale<1 :
                        x_scale=1
                        paddingx= (target_size - (original_width / x_scale)) / 2
                        paddingy= (target_size - (original_height / x_scale)) / 2
                        for obj in objects:
                            annotation = obj.get('annotation', {})
                            coord = annotation.get('coord', {})
                            x = int(coord.get('x', 0.0) / x_scale) + paddingx
                            y = int(coord.get('y', 0.0) / x_scale) + paddingy
                            width = int(coord.get('width', 0.0) / x_scale)
                            height = int(coord.get('height', 0.0) / x_scale)
                            class_name = obj.get('class_name', "Unknown")
                            class_id = class_mapping.get(class_name, -1)

                            # 중심좌표
                            center_x = (x + width / 2) / target_size
                            center_y = (y + height / 2) / target_size
                            normalized_width = width / target_size
                            normalized_height = height / target_size

                            # Write YOLO-formatted data to the .txt file
                            yolo_txt_file.write(f"{class_id} {center_x} {center_y} {normalized_width} {normalized_height}\n")

                    else:
                        paddingy = (target_size - (original_height / x_scale)) / 2
                        for obj in objects:
                            annotation = obj.get('annotation', {})
                            coord = annotation.get('coord', {})
                            x = int(coord.get('x', 0.0) / x_scale)
                            y = int(coord.get('y', 0.0) / x_scale) + paddingy
                            width = int(coord.get('width', 0.0) / x_scale)
                            height = int(coord.get('height', 0.0) / x_scale)
                            class_name = obj.get('class_name', "Unknown")
                            class_id = class_mapping.get(class_name, -1)

                            # 중심좌표
                            center_x = (x + width / 2) / target_size
                            center_y = (y + height / 2) / target_size
                            normalized_width = width / target_size
                            normalized_height = height / target_size

                            # Write YOLO-formatted data to the .txt file
                            yolo_txt_file.write(f"{class_id} {center_x} {center_y} {normalized_width} {normalized_height}\n")


                except json.JSONDecodeError as exc:
                    print(f"Error decoding JSON in {json_file}: {exc}")
