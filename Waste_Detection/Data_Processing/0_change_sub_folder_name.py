import os

# 변경할 폴더가 있는 경로 지정
root_folder = "./dataset/"

# 시작 폴더에서 해당하는 모든 서브 폴더의 이름 변경
for foldername, subfolders, filenames in os.walk(root_folder):
    for subfolder in subfolders:
        if "_1.재활용선별장" in subfolder:
            # "_1.재활용선별장"을 새로운 이름으로 대체
            new_subfolder = subfolder.replace("_1.재활용선별장", "")
            new_folder_path = os.path.join(foldername, new_subfolder)
            os.rename(os.path.join(foldername, subfolder), os.path.join(foldername, new_subfolder))
            print(f"폴더 이름 변경: {os.path.join(foldername, subfolder)} -> {new_folder_path}")

        elif "_2.실내형분류기" in subfolder:
            # "_2.실내형분류기"를 새로운 이름으로 대체
            new_subfolder = subfolder.replace("_2.실내형분류기", "")
            new_folder_path = os.path.join(foldername, new_subfolder)
            os.rename(os.path.join(foldername, subfolder), os.path.join(foldername, new_subfolder))
            print(f"폴더 이름 변경: {os.path.join(foldername, subfolder)} -> {new_folder_path}")
