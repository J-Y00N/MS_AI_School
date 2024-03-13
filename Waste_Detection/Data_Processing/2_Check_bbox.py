import cv2
import os

# YOLO 텍스트 파일 경로
yolo_txt_folder = 'C:/Users/54/Desktop/Project/dataset/extract/extractlabel'  # YOLO 텍스트 파일이 있는 폴더
image_folder = 'C:/Users/54/Desktop/Project/dataset/extract/image'  # 이미지 파일이 있는 폴더

# 출력 이미지 폴더
output_folder = 'C:/Users/54/Desktop/Project/dataset/extract/output_image'
os.makedirs(output_folder, exist_ok=True)

# 클래스 이름 및 색상 정의
class_colors = {'Class1': (255, 0, 0), 'Class2': (0, 255, 0), 'Class3': (0, 0, 255)}

# YOLO 텍스트 파일 읽기 및 바운딩 박스 그리기
for yolo_txt_file in os.listdir(yolo_txt_folder):
    if yolo_txt_file.lower().endswith('.txt'):
        yolo_txt_path = os.path.join(yolo_txt_folder, yolo_txt_file)
        image_path = os.path.join(image_folder, os.path.splitext(yolo_txt_file)[0] + ".png")
        output_image_path = os.path.join(output_folder, os.path.splitext(yolo_txt_file)[0] + "_output.png")

        image = cv2.imread(image_path)
        with open(yolo_txt_path, 'r') as txt_file:
            for line in txt_file:
                parts = line.strip().split()
                class_id = parts[0]
                center_x = float(parts[1])
                center_y = float(parts[2])
                width = float(parts[3])
                height = float(parts[4])

                # 좌표 및 크기를 절대 좌표로 변환
                x = int((center_x - width / 2) * 1280)
                y = int((center_y - height / 2) * 1280)
                x_max = int((center_x + width / 2) * 1280)
                y_max = int((center_y + height / 2) * 1280)

                cv2.rectangle(image, (x, y), (x_max, y_max), (0,255,0), 2)

        # 결과 이미지 저장
        cv2.imwrite(output_image_path, image)

        # 결과 이미지 표시
        cv2.imshow('Result Image', image)
        cv2.waitKey(0)