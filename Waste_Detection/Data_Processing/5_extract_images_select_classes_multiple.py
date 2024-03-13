import os
import shutil
import glob


# 이미지 폴더 경로
image_folder = "dataset_1/images/B10"
# YOLO 텍스트 폴더 경로
folder_path = "dataset_1/labels/B10_txt_class_number_changed"
# 이미지를 저장할 폴더 경로
output_folder = "dataset_2/part/images/B10"



# 클래스 별로 뽑고 싶은 이미지 수를 설정한 딕셔너리
classes_to_extract = {

    # 클래스 00에 해당하는 이미지 00장
    0: 0, # paper # c_1, # c_2_01, # c_2_02
    3: 0, # can # c_3
    4: 0, # glass # c_4_01_02, # c_4_02_01_02, # c_4_02_02_02, # c_4_02_03_02, # c_4_03
    9: 0, # pet # c_5_02
    10: 0, # plastic # c_6
    11: 0, # vinyl # c_7
    25: 0, # foam # c_8_01, #c_8_02
    28: 0, # battery # c_9

    12: 0, # paper + f_s # c_1_01, # c_2_02_01
    14: 0, # can + f_s # c_3_01
    15: 0, # o glass + f_s # c_4_03_01, # c_4_01_01, # c_4_02_01_01, # c_4_02_02_01, # c_4_02_03_01
    16: 0, # pet + f_s + m-p_m # c_5_01_01, # c_5_02_01, # c_5_01
    18: 0, # plastic + f_s # c_6_01
    19: 0, # vinyl + f_s # c_7_01
    27: 0 # foam + f_s # c_8_01_01
}

os.makedirs(output_folder, exist_ok=True)

cnt = {class_label: 0 for class_label in classes_to_extract.keys()}

# 이미지 파일을 복사
for txt_file in glob.glob(os.path.join(folder_path, "*.txt")):
    with open(txt_file, "r") as infile:
        for line in infile:
            parts = line.strip().split()
            if len(parts) >= 1:
                label = int(parts[0])
                if label in classes_to_extract:
                    if cnt[label] < classes_to_extract[label]:
                        # 해당 클래스에 해당하는 이미지 파일 경로
                        image_file = os.path.join(image_folder, os.path.splitext(os.path.basename(txt_file))[0] + ".png")

                        # 이미지 파일을 복사하여 저장 폴더에 저장
                        shutil.copy(image_file, output_folder)
                        cnt[label] += 1

# 이미지 수를 뽑은 클래스 명과 수를 출력
for class_label, num_images in classes_to_extract.items():
    print(f"Extracted {cnt[class_label]} images for class {class_label}")