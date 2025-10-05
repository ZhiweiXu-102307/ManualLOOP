import os
from pathlib import Path

def create_directories():
    """创建目录"""
    dir_structure = {
        'inputs': '原始数据输入',
        'outputs/data': '导出csv格式滞回曲线数据',
        'outputs/plots': '绘制符合科研论文标准的滞回曲线',
    }
    print("初始化目录结构...")
    for path, desc in dir_structure.items():
        try:
            Path(path).mkdir(parents=True, exist_ok=True)
            print(f"已初始化目录: [{path}] ({desc})")
        except Exception as e:
            print(f"目录创建失败: [{path}]: {str(e)}")

if __name__ == "__main__":
    pass