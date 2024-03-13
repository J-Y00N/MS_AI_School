from PIL import Image
import os

# 변경 대상 폴더 경로
root_folder = "./dataset/"

# 하위 폴더 탐색
for foldername, subfolders, filenames in os.walk(root_folder):
    for filename in filenames:
        if filename.lower().endswith(".jpg"):
            jpg_file_path = os.path.join(foldername, filename)
            output_folder = os.path.join(foldername + "_converted")

            # png로 변환
            png_file_path = os.path.join(output_folder, filename.rsplit(".", 1)[0] + ".png")

            # 이미 존재하는 png 파일 스킵
            if not os.path.exists(png_file_path):
                os.makedirs(output_folder, exist_ok=True)
                jpg_image = Image.open(jpg_file_path)
                jpg_image.save(png_file_path, "PNG")
                jpg_image.close()

                print(f"{jpg_file_path} -> {png_file_path}")

            else:
                print(f"{png_file_path} is already exist")