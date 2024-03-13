import os
import shutil


# 원본 폴더, 대상 폴더 및 저장 폴더 경로 설정
source_folder = 'waste_dataset/val/images'
target_folder = 'dataset_2/total/labels/AB_labels'
save_folder = 'waste_dataset/val/labels'

os.makedirs(save_folder, exist_ok=True)

# 원본 폴더를 순회하며 PNG 파일 탐색
for root, dirs, files in os.walk(source_folder):
    for file in files:
        # 확장자가 .png인 파일만 처리
        if file.lower().endswith('.png'):
            png_file_path = os.path.join(root, file)
            
            # 대상 폴더에서 동일한 파일명을 가진 .txt 파일 찾기
            base_name, _ = os.path.splitext(file)
            txt_file_path = os.path.join(target_folder, base_name + '.txt')

            if os.path.exists(txt_file_path):
                # print(f"PNG 파일과 동일한 이름을 가진 TXT 파일 발견: {file}")

                # 저장 폴더로 파일 복사
                save_path = os.path.join(save_folder, os.path.basename(txt_file_path))
                shutil.copy2(txt_file_path, save_path)

                print(f"{os.path.basename(txt_file_path)} -> {os.path.basename(save_path)}")
