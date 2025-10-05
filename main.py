from pathlib import Path
from core.processor import convert_to_csv
from core.hysteresis_plotter import plot_hysteresis
from utils.path_manager import create_directories

def main():
    create_directories()
    input_dir = Path("inputs")
    csv_dir = Path("outputs/data")
    image_dir = Path("outputs/plots")

    convert_to_csv(input_dir, csv_dir)
    plot_hysteresis(csv_dir, image_dir)

    print("\n处理完成！结果已分类保存于outputs文件夹下：")
    print(f"csv本构数据: ./outputs/data/")
    print(f"滞回曲线: ./outputs/plots/")

if __name__ == "__main__":
    main()