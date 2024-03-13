import os
import shutil

# 이미지 파일 디렉토리, JSON 파일 디렉토리, 그리고 목록을 저장할 디렉토리 설정
image_directory = "./yolo_dataset/train/images/"
label_directory = "./yolo_dataset/train/labels/"
output_directory = "./yolo_dataset/train/error/"  # 원하는 디렉토리로 수정하세요
image_error_directory = os.path.join(output_directory, 'image')
label_error_directory = os.path.join(output_directory, 'label')

# 이미지 파일 및 JSON 파일 가져오기
image_files = set([os.path.splitext(file)[0] for file in os.listdir(image_directory)])
label_files = set([os.path.splitext(file)[0] for file in os.listdir(label_directory)])


# 이미지 파일에만 존재하는 파일들을 '이미지 오류' 디렉토리로 복사하고 삭제
for file in image_files:
    if file not in label_files:
        source_file = os.path.join(image_directory, file + ".png")  # 이미지 파일 확장자에 맞게 수정
        target_file = os.path.join(image_error_directory, file + ".png")  # 이미지 파일 확장자에 맞게 수정
        # os.makedirs(os.path.dirname(target_file), exist_ok=True)
        shutil.copy2(source_file, target_file)
        # os.remove(source_file)

# JSON 파일에만 존재하는 파일들을 'JSON 오류' 디렉토리로 복사하고 삭제
for file in label_files:
    if file not in image_files:
        source_file = os.path.join(label_directory, file + ".txt")  # JSON 파일 확장자에 맞게 수정
        target_file = os.path.join(label_error_directory, file + ".txt")  # JSON 파일 확장자에 맞게 수정
        # os.makedirs(os.path.dirname(target_file), exist_ok=True)
        shutil.copy2(source_file, target_file)
        # os.remove(source_file)

# 나머지 파일 수 계산
image_file_count = len(image_files) - len(os.listdir(image_error_directory))
label_file_count = len(label_files) - len(os.listdir(label_error_directory))

print("이미지 파일에만 존재하는 파일 수:", len(os.listdir(image_error_directory)))
print("label 파일에만 존재하는 파일 수:", len(os.listdir(label_error_directory)))
print("이미지 파일 수 (오류 포함):", image_file_count)
print("label 파일 수 (오류 포함):", label_file_count)
