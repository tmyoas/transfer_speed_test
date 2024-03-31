import shutil
import time
import os
import sys

def move_files_and_measure_time(source_dir, target_dir):
    # ターゲットディレクトリが存在しない場合は作成
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    # 移動開始時間を記録
    start_time = time.time()
    
    # ソースディレクトリ内のすべてのファイルをターゲットディレクトリに移動
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        if os.path.isfile(file_path):
            shutil.copy(file_path, target_dir)
    
    # 移動終了時間を記録
    end_time = time.time()
    
    # 移動にかかった時間を計算して表示
    elapsed_time = end_time - start_time
    print(f"移動にかかった時間: {elapsed_time}秒")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <source_dir> <target_dir>")
        sys.exit(1)
    
    source_dir = sys.argv[1]
    target_dir = sys.argv[2]
    move_files_and_measure_time(source_dir, target_dir)
