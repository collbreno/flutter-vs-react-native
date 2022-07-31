import os
import subprocess
from glob import glob
import cv2
import numpy as np
import os
from tqdm import tqdm

def delete_while_duplicated(first_img, img_list):
    img1 = cv2.imread(first_img)
    for img_path in img_list:
        img2 = cv2.imread(img_path)
        r = np.count_nonzero(cv2.absdiff(img1, img2))
        if r < 500000:
            os.remove(img_path)
        else:
            break

def delete_first_duplicated_images(files: list):
    first_img = files.pop(0)
    delete_while_duplicated(first_img, files)

if __name__ == '__main__':

    print('Extracting frames...')
    # extract frames from every video
    videos = glob('../tests_executor/outputs/*/*.mp4')
    for video in tqdm(videos):
        video_name = video.split('\\')[-1]
        app_id = video_name.split('-')[0]
        output_path = f"frames/{app_id}/{video_name.removesuffix('.mp4')}"
        if not os.path.exists(output_path):
            os.makedirs(output_path, exist_ok=True)
            subprocess.run(f'ffmpeg -i {video} {output_path}/frame%03d.png', shell=True, capture_output=True)

    print('Deleting duplicated frames')
    # delete duplicated frames from every video
    folders = glob('./frames/*/*')
    for folder in tqdm(folders):
        files = glob(f'{folder}/*.png')
        delete_first_duplicated_images(files)
        files.reverse()
        delete_first_duplicated_images(files)
    