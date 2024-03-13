import os
import zipfile

def unzip_to_individual_folders(folder_path):
    try:
        # 지정된 폴더 내의 모든 파일을 나열합니다.
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                # ZIP 파일만 처리합니다.
                if file.endswith(".zip"):
                    # ZIP 파일의 전체 경로를 가져옵니다.
                    full_zip_path = os.path.join(root, file)
                    
                    # 압축을 해제할 새 폴더의 이름을 ZIP 파일 이름(확장자 제외)으로 지정합니다.
                    new_folder_path = os.path.join(root, os.path.splitext(file)[0])
                    # 새 폴더 생성 (이미 존재하는 경우에도 안전)
                    os.makedirs(new_folder_path, exist_ok=True)
                    
                    # ZIP 파일을 연 후, 모든 내용을 새 폴더에 압축 해제합니다.
                    with zipfile.ZipFile(full_zip_path, 'r') as zip_ref:
                        zip_ref.extractall(new_folder_path)  # 압축을 해제할 새 폴더를 지정합니다.
                        print(f"{file} 압축 해제 완료, 위치: '{new_folder_path}'")

        print("모든 ZIP 파일이 성공적으로 압축 해제되었습니다.")

    except Exception as e:
        print(f"압축 해제 중 오류 발생: {e}")

# 압축을 해제할 폴더의 경로
path_to_folder = './data_raw/Training/label/'  # 이 경로를 압축 해제할 실제 폴더 경로로 변경하세요.

# 함수 실행
unzip_to_individual_folders(path_to_folder)