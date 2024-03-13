import os

# 대응 관계를 정의합니다.
label_mapping = {
    'c_1': 0,
    'c_2_01': 1,
    'c_2_02': 2,
    'c_3': 3,
    'c_4_01_02': 4,
    'c_4_02_01_02': 5,
    'c_4_02_02_02': 6,
    'c_4_02_03_02': 7,
    'c_4_03': 8,
    'c_5_02': 9,
    'c_6': 10,
    'c_7': 11,
    'c_1_01': 12,
    'c_2_02_01': 13,
    'c_3_01': 14,
    'c_4_03_01': 15,
    'c_5_01_01': 16,
    'c_5_02_01': 17,
    'c_6_01': 18,
    'c_7_01': 19,
    'c_4_01_01': 20,
    'c_4_02_01_01': 21,
    'c_4_02_02_01': 22,
    'c_4_02_03_01': 23,
    'c_5_01': 24,
    'c_8_01': 25,
    'c_8_02': 26,
    'c_8_01_01': 27,
    'c_9': 28
}

# 폴더 경로를 지정합니다.
folder_path = '../../MS_AI_School/Exercise/16_Object_Recognition_Project/project/ultralytics-main/ultralytics/cfg/tresh_dataset/val/labels'

# 폴더 내의 모든 파일을 대상으로 작업합니다.
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)

        # 파일을 읽고 수정된 내용을 저장할 리스트를 생성합니다.
        new_lines = []

        with open(file_path, 'r') as file:
            for line in file:
                parts = line.split(' ')  # 라벨명을 쉼표와 공백을 기준으로 분할합니다.
                label = parts[0]  # 라벨명을 추출합니다.

                # 대응 관계에 따라 라벨명을 int로 대체합니다.
                if label in label_mapping:
                    parts[0] = str(label_mapping[label])

                # 수정된 라인을 새로운 리스트에 추가합니다.
                new_line = ' '.join(parts)
                new_lines.append(new_line)

        # 수정된 내용을 파일에 저장합니다.
        with open(file_path, 'w') as file:
            file.writelines(new_lines)
