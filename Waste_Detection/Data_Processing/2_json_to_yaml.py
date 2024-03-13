import os
import json
import yaml

# 입력 및 출력 폴더 경로 설정
input_folder = "./dataset/train/label/"
output_folder = "./dataset/train/label_yaml/"


# 폴더 생성
os.makedirs(output_folder, exist_ok=True)

# 입력 폴더 경로 및 서브폴더 내의 JSON 파일 검색
for root, dirs, files in os.walk(input_folder):
    for file_name in files:
        if file_name.endswith('.json'):
            # JSON 파일 경로
            json_file_path = os.path.join(root, file_name)
            
            # YAML 파일 경로
            yaml_file_name = os.path.splitext(file_name)[0] + ".yaml"
            relative_output_folder = os.path.relpath(root, input_folder)
            yaml_output_folder = os.path.join(output_folder, relative_output_folder)
            yaml_file_path = os.path.join(yaml_output_folder, yaml_file_name)
            
            # 저장될 경로의 서브폴더 생성
            os.makedirs(yaml_output_folder, exist_ok=True)

            # JSON 파일을 읽기
            with open(json_file_path, 'r', encoding='utf-8') as json_file:
                json_data = json.load(json_file)

            # Convert json to yaml
            yaml_data = yaml.dump(json_data, sort_keys=False)

            # YAML 파일 저장
            with open(yaml_file_path, 'w', encoding='utf-8') as yaml_file:
                yaml_file.write(yaml_data)

            print(f"Converted {json_file_path} to {yaml_file_path}")

print("All JSON files converted to YAML.")