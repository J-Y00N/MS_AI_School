#추출한 이미지 잘 됐나 확인
import os

# 이미지 파일이 있는 폴더 경로
image_folder = "waste_dataset/val/images"

# 텍스트 파일이 있는 폴더 경로
yolo_txt_folder = "dataset_2/total/labels/AB_labels"

print(image_folder)

class_counts = {}
# 이미지 파일 이름을 기반으로 YOLO 텍스트 파일을 열어 클래스 레이블을 추출하여 딕셔너리에 저장
for image_file in os.listdir(image_folder):
    if image_file.endswith(".png"):
        image_name = os.path.splitext(image_file)[0]
        txt_file = os.path.join(yolo_txt_folder, image_name + ".txt")

        if os.path.isfile(txt_file):
            with open(txt_file, "r") as infile:
                for line in infile:
                    parts = line.strip().split()
                    if len(parts) >= 1:
                        label = int(parts[0])
                        if label in class_counts:
                            class_counts[label] += 1
                        else:
                            class_counts[label] = 1

# 클래스 종류 및 해당 클래스의 객체 수 출력
for label, count in class_counts.items():
    print(f"클래스 {label}: {count}개의 객체")