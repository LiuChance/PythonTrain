import cv2
import os
import shutil
import re
import argparse


parser = argparse.ArgumentParser(description='trans vidio 2 image')
parser.add_argument('-v', '--vidio-dir', default='path to vidio', type=str)
parser.add_argument('-s', '--save-dir', default='path to save', type=str)
args = parser.parse_args()


def getthe_image_from_vidio(vidio_dir, vidio_name, save_dir):
    count = 50  # 100对应4s左右
    videoCapture = cv2.VideoCapture(os.path.join(vidio_dir, vidio_name))
    i, j = -1, -1
    while True:
        success, frame = videoCapture.read()
        i += 1
        if not success:
            print('all read')
            break
        if i % count == 0:
            j += 1
            savedname = vidio_name.split('.')[0] + '_' + str(j) + '_' + str(i)+'.jpg'
            save_path = os.path.join(save_dir, savedname)
            cv2.imwrite(save_path, frame)
            print('image of %s is saved'%(savedname))



def deal_onepath_of_vidio(dir_of_vidio, save_root_dir):
    vidio_names_list = os.listdir(dir_of_vidio)
    for vidio_name in vidio_names_list:
        save_dir = os.path.join(save_root_dir, vidio_name.split('.')[0])
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        getthe_image_from_vidio(dir_of_vidio, vidio_name, save_dir)


if __name__ == "__main__":
    dir_of_vidio = args.vidio_dir
    save_root_dir = args.save_dir
    deal_onepath_of_vidio(dir_of_vidio, save_root_dir)
