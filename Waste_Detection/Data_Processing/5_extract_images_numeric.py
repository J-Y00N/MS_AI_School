import os
import shutil

# 이미지 경로
image_folder = "waste_dataset_5/train/images"

#추출 경로
ext_folder = "waste_dataset_5/part/my_A_train"

if not os.path.exists(ext_folder):
    os.makedirs(ext_folder)


count = 0 
n = 2 # 몇 번째마다 갖고올 지
for filename in os.listdir(image_folder):
    if count % n == 0:
        img_path = os.path.join(image_folder, filename)
        ext_path = os.path.join(ext_folder, filename)
        shutil.copy(img_path, ext_path)
    count += 1