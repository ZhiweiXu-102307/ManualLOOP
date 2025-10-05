import os
import pandas as pd
from tqdm import tqdm
import matplotlib.pyplot as plt

def plot_hysteresis(csv_folder, output_folder):
    """绘制符合科研论文标准的滞回曲线"""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    print("\n开始绘制滞回曲线:")
    
    # 设置全局绘图参数（科研论文常用设置）
    plt.rcParams.update({
        'font.size': 16,          # 全局字体大小
        'axes.linewidth': 1.5,    # 坐标轴线宽
        'lines.linewidth': 2.0,   # 曲线线宽
        'xtick.major.width': 1.5, # X轴主刻度线宽
        'ytick.major.width': 1.5, # Y轴主刻度线宽
        'xtick.major.size': 5,    # X轴主刻度长度
        'ytick.major.size': 5,    # Y轴主刻度长度
        'axes.labelsize': 18,     # 坐标轴标签字体大小
        'axes.titlesize': 20      # 标题字体大小
    })
    
    csv_files = os.listdir(csv_folder)
    progress_bar = tqdm(range(len(csv_files)))
    # 遍历文件夹中的所有CSV文件
    for idx in progress_bar:
        filename = csv_files[idx]
        if filename.endswith('.csv'):
            csv_path = os.path.join(csv_folder, filename)
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.png")
            
            df = pd.read_csv(csv_path)
            
            # 创建画布和坐标轴
            fig, ax = plt.subplots(figsize=(8, 6))  # 科研论文常用比例
            
            # 绘制滞回曲线
            ax.plot(df['Displacement'], df['Force'], 
                   color='#1f77b4',  # 使用更专业的颜色
                   zorder=3)         # 设置绘制层级
            
            # 标题和坐标轴标签
            ax.set_title(f"Hysteresis Curve - {os.path.splitext(filename)[0]}", 
                        pad=15)  # 增加标题与图的间距
            ax.set_xlabel('Displacement (mm)', labelpad=10)  # 增加单位说明
            ax.set_ylabel('Force (kN)', labelpad=10)
            
            # 刻度参数强化
            ax.tick_params(axis='both', which='major', 
                           labelsize=16,  # 刻度标签字体大小
                           pad=8)         # 刻度与标签间距
                           
            # 坐标轴范围设置
            ax.set_xlim(left=df['Displacement'].min()*1.1, 
                       right=df['Displacement'].max()*1.1)
            ax.set_ylim(bottom=df['Force'].min()*1.1, 
                       top=df['Force'].max()*1.1)
            
            # 网格线设置
            ax.grid(True, 
                    linestyle='--',  # 虚线网格
                    alpha=0.6,       # 透明度
                    zorder=0)        # 网格在底层
                    
            # 边框强化
            for spine in ax.spines.values():
                spine.set_linewidth(1.5)
                
            # 优化布局
            plt.tight_layout()
            
            # 高质量保存（适合论文投稿的参数设置）
            plt.savefig(output_path, 
                       dpi=600,          # 高分辨率
                       bbox_inches='tight', 
                       facecolor='white')  # 确保背景为白色
            plt.close()

if __name__ == "__main__":
    pass