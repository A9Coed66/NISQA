import os
import subprocess
import time

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--parent_folder', required=True, type=str, help='folder with subfolders to run each folder')
parser.add_argument('--output_dir', required=True, type=str, help='folder to ouput results.csv')

args = parser.parse_args()
args = vars(args)

if __name__ == "__main__":
    parent_folder = args['parent_folder']
    subfolders = [dir for dir in os.listdir(parent_folder) if os.path.isdir(os.path.join(parent_folder, dir))]

    for subfolder in subfolders:
        print(f'Running {subfolder}')
        try:
            subprocess.run([
                'python', 'run_predict.py', 
                '--mode', 'predict_dir',
                '--pretrained_model', 'weights/nisqa.tar',
                '--data_dir', os.path.join(parent_folder, subfolder),  # Đảm bảo đường dẫn đúng
                '--num_workers', '0',
                '--bs', '10',
                '--output_dir', args['output_dir']
            ], check=True)
        except Exception as e:
            print(f'Error in {subfolder}: {e}')
        print(f'Finished {subfolder}')
        time.sleep(1)
    print('Finished all subfolders')