import os
import glob

# 원하는 클래스 레이블
desired_labels = {0, 3, 4, 9, 10, 11, 25, 28}

# 경로 설정
input_folder_path = "dataset/train/label_num/B5_txt_class_number_changed"
output_folder_path = "dataset/train/label_num/B5_txt_class_number_removed"

# 폴더 생성
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

for txt_file in glob.glob(os.path.join(input_folder_path, "*.txt")):
    output_file = os.path.join(output_folder_path, os.path.basename(txt_file))

    with open(txt_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            parts = line.strip().split()
            if len(parts) >= 2:
                original_label = int(parts[0])
                if original_label in desired_labels:
                    outfile.write(line)
            else:
                outfile.write(line)

print("데이터 처리가 완료되었습니다.")