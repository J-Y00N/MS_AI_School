import os

# 라벨 변환 매핑
label_mapping = {
    0: 0,
    3: 1,
    4: 2,
    9: 3,
    10: 4,
    11: 5,
    25: 6,
    28: 7,
    12: 8,
    14: 9,
    15: 10,
    16: 11,
    18: 12,
    19: 13,
    27: 14
    # ... 
}

# 시작 폴더 경로를 지정
root_folder = "ultralytics-main/ultralytics/cfg/waste_dataset/val/labels"

# 시작 폴더부터 모든 서브 폴더를 검색하고 txt 파일을 대상으로 라벨 숫자 변경
for foldername, subfolders, filenames in os.walk(root_folder):
    for filename in filenames:
        if filename.endswith(".txt"):
            txt_file_path = os.path.join(foldername, filename)

            # txt 파일을 읽어 라벨 숫자를 변경하고 수정
            with open(txt_file_path, 'r') as file:
                lines = file.readlines()

            with open(txt_file_path, 'w') as file:
                for line in lines:
                    parts = line.strip().split(' ')
                    if len(parts) > 0:
                        original_label = int(parts[0])
                        if original_label in label_mapping:
                            parts[0] = str(label_mapping[original_label])
                            modified_line = ' '.join(parts)
                            file.write(modified_line + '\n')
                        else:
                            file.write(line)
                    else:
                        file.write(line)
