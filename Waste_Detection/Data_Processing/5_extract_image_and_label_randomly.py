import os
import shutil
import random

# 원본 이미지 폴더 경로와 이미지를 복사할 목적지 폴더 경로 설정
image_source_folder = "dataset/train/images/B7"

# 이미지 파일명을 기반으로 텍스트 파일을 찾아서 복사
text_source_folder = "dataset/train/labels/B7_txt"

destination_image_folder = "./yolo_dataset/train/images/"
destination_label_folder = "./yolo_dataset/train/labels/"

random.seed()
image_files = os.listdir(image_source_folder)
selected_image_files = random.sample(image_files, 50)


# 이미지 파일 복사
for image_file in selected_image_files:
    source_image_path = os.path.join(image_source_folder, image_file)
    destination_image_path = os.path.join(destination_image_folder, image_file)
    shutil.copy(source_image_path, destination_image_path)


for image_file in selected_image_files:
    image_file_name = os.path.splitext(image_file)[0]  # 확장자 제거
    text_file_name = image_file_name + ".txt"

    source_text_path = os.path.join(text_source_folder, text_file_name)
    destination_text_path = os.path.join(destination_label_folder, text_file_name)

    if os.path.exists(source_text_path):
        shutil.copy(source_text_path, destination_text_path)
