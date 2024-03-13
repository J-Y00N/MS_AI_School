import os
import shutil

# 이미지 파일 디렉토리, JSON 파일 디렉토리, 그리고 목록을 저장할 디렉토리 설정
image_directory = "./train/image/TS_B9_1"
json_directory = "./train/label/TL_B9_1"
output_directory = "./04.실험"  # 원하는 디렉토리로 수정하세요
image_error_directory = os.path.join(output_directory, '이미지 오류')
json_error_directory = os.path.join(output_directory, 'JSON 오류')

# 이미지 파일 및 JSON 파일 가져오기
image_files = set([os.path.splitext(file)[0] for file in os.listdir(image_directory)])
json_files = set([os.path.splitext(file)[0] for file in os.listdir(json_directory)])

# 이미지 파일에만 존재하는 파일들을 '이미지 오류' 디렉토리로 복사하고 삭제
for file in image_files:
    if file not in json_files:
        source_file = os.path.join(image_directory, file + ".jpg")  # 이미지 파일 확장자에 맞게 수정
        target_file = os.path.join(image_error_directory, file + ".jpg")  # 이미지 파일 확장자에 맞게 수정
        os.makedirs(os.path.dirname(target_file), exist_ok=True)
        shutil.copy2(source_file, target_file)
        os.remove(source_file)

# JSON 파일에만 존재하는 파일들을 'JSON 오류' 디렉토리로 복사하고 삭제
for file in json_files:
    if file not in image_files:
        source_file = os.path.join(json_directory, file + ".json")  # JSON 파일 확장자에 맞게 수정
        target_file = os.path.join(json_error_directory, file + ".json")  # JSON 파일 확장자에 맞게 수정
        os.makedirs(os.path.dirname(target_file), exist_ok=True)
        shutil.copy2(source_file, target_file)
        os.remove(source_file)

# 나머지 파일 수 계산
image_file_count = len(image_files) - len(os.listdir(image_error_directory))
json_file_count = len(json_files) - len(os.listdir(json_error_directory))

print("이미지 파일에만 존재하는 파일 수:", len(os.listdir(image_error_directory)))
print("JSON 파일에만 존재하는 파일 수:", len(os.listdir(json_error_directory)))
print("이미지 파일 수 (오류 포함):", image_file_count)
print("JSON 파일 수 (오류 포함):", json_file_count)
