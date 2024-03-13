import os

# 시작 폴더 경로를 지정
root_folder = "./dataset_1/images/B10"

# 시작 폴더부터 모든 서브 폴더를 검색하고 파일 확장자 변경
for foldername, subfolders, filenames in os.walk(root_folder):
    for filename in filenames:
        if "_processed" in filename:  # 특정 문자열을 파일 이름에 포함하는 경우
            new_filename = filename.replace("_processed", "")
            old_file_path = os.path.join(foldername, filename)
            new_file_path = os.path.join(foldername, new_filename)
            os.rename(old_file_path, new_file_path)
            print(f"파일 이름 변경: {old_file_path} -> {new_file_path}")