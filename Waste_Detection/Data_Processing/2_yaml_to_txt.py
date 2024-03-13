import os
import yaml
from tqdm import tqdm

def box_convert_to_yolo_from_yaml(box_x, box_y, box_width, box_height, image_dim, target_size=640):
    """
    주어진 바운딩 박스 좌표를 YOLO 형식으로 변환합니다.

    :param x: 바운딩 박스의 x 좌표
    :param y: 바운딩 박스의 y 좌표
    :param width: 바운딩 박스의 너비
    :param height: 바운딩 박스의 높이
    :param image_dim: 이미지의 원본 크기 (너비, 높이)
    :return: YOLO 형식의 좌표 (center_x, center_y, normalized_width, normalized_height)
    """
    image_width, image_height = image_dim
    #target_size = 640
    resize_ratio = target_size / image_width
    # 가로 폭이 더 길기 때문에 resize ratio 는 가로 폭을 기준으로 한다.
    padding_size = target_size - (image_height * resize_ratio)

    box_x_in_640 = box_x * resize_ratio # 640 사이즈에서의 box x 좌표
    box_y_in_640 = (box_y * resize_ratio) + (padding_size * 0.5) # 640 사이즈에서의 box y 좌표, half 패딩 더해준다. 
    width_in_640 = box_width * resize_ratio
    height_in_640 = box_height * resize_ratio

    center_x = (box_x_in_640 + width_in_640/2) / target_size
    center_y = (box_y_in_640 + height_in_640/2) / target_size
    normalized_width = width_in_640 / target_size
    normalized_height = height_in_640 / target_size

    return center_x, center_y, normalized_width, normalized_height

def process_yaml_file(file_path):
    """
    지정된 경로의 YAML 파일을 읽고 객체 정보를 추출합니다.

    :param file_path: YAML 파일의 경로
    :return: 이미지의 차원과 객체 정보 목록
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)

    # 원본 이미지 사이즈 구하기. 
    resolution = data["Info"]["RESOLUTION"].split("/")
    image_dim = (float(resolution[0].strip()), float(resolution[1].strip()))

    # 원본 박스 좌표 구하기. 
    objects_info = []
    for obj in data.get("objects", []):
        class_name = obj.get("class_name")
        coord = obj.get("annotation", {}).get("coord", {})
        box_x = float(coord.get("x"))
        box_y = float(coord.get("y"))
        box_width = float(coord.get("width"))
        box_height = float(coord.get("height"))

        yolo_coord = box_convert_to_yolo_from_yaml(box_x, box_y, box_width, box_height, image_dim)
        objects_info.append((class_name, *yolo_coord))

    return image_dim, objects_info

def save_to_txt(output_path, objects_info):
    """
    객체 정보를 .txt 파일로 저장합니다.

    :param output_path: 저장할 파일의 경로
    :param objects_info: 저장할 객체 정보 목록
    """
    with open(output_path, 'w') as file:
        for object_info in objects_info:
            line = " ".join(map(str, object_info)) + "\n"
            file.write(line)



def main(yaml_folder, yolo_txt_folder):
    """
    주어진 폴더의 모든 YAML 파일을 처리하고 결과를 .txt 파일로 저장합니다.

    :param yaml_folder: YAML 파일이 포함된 폴더 경로
    :param yolo_txt_folder: YOLO 형식의 .txt 파일을 저장할 폴더 경로
    """
    os.makedirs(yolo_txt_folder, exist_ok=True)

    # tqdm 라이브러리를 사용하여 진행 상황 바 추가
    yaml_files = os.listdir(yaml_folder)
    for yaml_file in tqdm(yaml_files, desc="Processing YAML files", unit="file"):
        if yaml_file.lower().endswith('.yaml'):
            yaml_file_path = os.path.join(yaml_folder, yaml_file)

            # YAML 파일 처리
            image_dim, objects_info = process_yaml_file(yaml_file_path)

            # 결과를 .txt 파일로 저장
            txt_file_name = os.path.splitext(yaml_file)[0] + ".txt"
            yolo_txt_path = os.path.join(yolo_txt_folder, txt_file_name)
            save_to_txt(yolo_txt_path, objects_info)

# 실행
if __name__ == "__main__":
    YAML_FOLDER_PATH = './data/Training/label/B10_yaml'
    YOLO_TXT_FOLDER_PATH = './data/Training/label/B10_yolo_txt'
    main(YAML_FOLDER_PATH, YOLO_TXT_FOLDER_PATH)

# B8 완료
# B9 완료
# B10 완료