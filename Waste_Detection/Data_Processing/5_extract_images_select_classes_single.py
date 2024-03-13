'''
  0: paper # c_1, # c_2_01, # c_2_02
  3: can # c_3
  4: glass # c_4_01_02, # c_4_02_01_02, # c_4_02_02_02, # c_4_02_03_02, # c_4_03
  9: pet # c_5_02
  10: plastic # c_6
  11: vinyl # c_7
  25: foam # c_8_01, #c_8_02
  28: battery # c_9

  12: paper + f_s # c_1_01, # c_2_02_01
  14: can  + f_s # c_3_01
  15: o glass + f_s # c_4_03_01, # c_4_01_01, # c_4_02_01_01, # c_4_02_02_01, # c_4_02_03_01
  16: pet + f_s + m-p_m # c_5_01_01, # c_5_02_01, # c_5_01
  18: plastic + f_s # c_6_01
  19: vinyl + f_s # c_7_01
  27: foam + f_s # c_8_01_01
'''


#필요한 장만큼 이미지 추출
import os
import shutil
import glob

# YOLO 텍스트 파일이 있는 폴더 경로
folder_path = "dataset_1/labels/A9_txt_class_number_changed"

# "0" 클래스에 해당하는 이미지를 저장할 폴더 경로
output_folder = "dataset_2/train/images/A9"

image_folder = "dataset_1/images/A9"

# "0" 클래스에 해당하는 이미지를 뽑을 클래스 번호
class_to_extract = 14

stopnum=14646 # 뽑고싶은 수
cnt=0
# 복사할 위치
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for txt_file in glob.glob(os.path.join(folder_path, "*.txt")):
    with open(txt_file, "r") as infile:
        for line in infile:
            parts = line.strip().split()
            if len(parts) >= 1:
                label = int(parts[0])
                if label == class_to_extract:
                    # 해당 클래스에 해당하는 이미지 파일 경로
                    image_file = os.path.join(image_folder, os.path.splitext(os.path.basename(txt_file))[0] + ".png")

                    # 이미지 파일을 복사하여 저장 폴더에 저장
                    shutil.copy(image_file, output_folder)
                    cnt+=1
    if cnt>stopnum:
        exit()
        print("test end")