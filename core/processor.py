import os
import re
from tqdm import tqdm
import pandas as pd

def convert_to_csv(input_folder, output_folder):
    """数据转换函数，基于数值特征识别有效数据"""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 定义数据特征正则表达式（匹配两个浮点数）
    sci_pattern = r"^[+-]?(\d+\.?\d*|\.\d+)([eE][+-]?\d+)?\s+[+-]?(\d+\.?\d*|\.\d+)([eE][+-]?\d+)?$"
    data_pattern = re.compile(sci_pattern)
    
    for filename in os.listdir(input_folder):
        if not filename.endswith('.txt'):
            continue

        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.csv")
        
        data = []
        in_data_section = False  # 数据区块标记
        
        with open(input_path, 'r') as f:
            for line in f:
                line = line.strip()
                
                # 自动检测数据区块开始
                if not in_data_section:
                    if data_pattern.match(line):
                        in_data_section = True
                        print(f"Data section starts at line: {line}")
                    else:
                        continue  # 跳过非数据行
                
                # 处理数据行
                parts = re.split(r'[\t\s]+', line)  # 支持制表符和空格分隔
                if len(parts) == 2:
                    try:
                        # 转换为浮点数并保留原始精度
                        disp = float(parts[0])
                        force = float(parts[1])
                        data.append([disp, force])
                    except ValueError:
                        print(f"Skipped invalid data: {line}")
                        continue
        
        if data:
            df = pd.DataFrame(data, columns=['Displacement', 'Force'])
            df.to_csv(output_path, index=False)
            print(f"Converted {filename} ({len(data)} valid points)")
        else:
            print(f"No valid data found in {filename}")

if __name__ == "__main__":
    pass