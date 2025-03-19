import os
import random

def split_dataset(image_dir, label_dir, train_ratio=0.7, val_ratio=0.2, test_ratio=0.1):
    images = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]
    random.shuffle(images)

    total_images = len(images)
    train_size = int(total_images * train_ratio)
    val_size = int(total_images * val_ratio)

    train_images = images[:train_size]
    val_images = images[train_size:train_size + val_size]
    test_images = images[train_size + val_size:]

    return train_images, val_images, test_images

def write_to_file(file_list, file_name):
    with open(file_name, 'w') as file:
        for item in file_list:
            file.write("%s\n" % item)

# 设置图片路径和标注路径
image_dir = '/home/hello/devdisk/WSF/yolov9-main/data_UAV/Crop12/images'
label_dir = '/home/hello/devdisk/WSF/yolov9-main/data_UAV/Crop12/labels'

train_images, val_images, test_images = split_dataset(image_dir, label_dir)

# 写入到文件
write_to_file(train_images, '/home/hello/devdisk/WSF/yolov9-main/data_UAV/crop12_set/train.txt')
write_to_file(val_images, '/home/hello/devdisk/WSF/yolov9-main/data_UAV/crop12_set/val.txt')
write_to_file(test_images, '/home/hello/devdisk/WSF/yolov9-main/data_UAV/crop12_set/test.txt')

