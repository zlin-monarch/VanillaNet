import os 
from icecream import ic 


dataset = '/home/linlin/dataset/dog_classification_dataset'
train_dir = os.path.join(dataset, 'train')
val_dir = os.path.join(dataset, 'val')
test_dir = os.path.join(dataset, 'test')


def split_dataset():
    # train:val:test = 8:1:1
    for root, dirs, files in os.walk(dataset):
        ic(root, dirs, files)

        for dir in dirs:
            train_sub_dir = os.path.join(train_dir, dir)
            val_sub_dir = os.path.join(val_dir, dir)
            test_sub_dir = os.path.join(test_dir, dir)
            if not os.path.exists(train_sub_dir):
                os.makedirs(train_sub_dir)
            if not os.path.exists(val_sub_dir):
                os.makedirs(val_sub_dir)
            if not os.path.exists(test_sub_dir):
                os.makedirs(test_sub_dir)

            for i, file in enumerate(os.listdir(os.path.join(root, dir))):
            #     ic(file)
            #     ic(os.path.join(root, dir, file))

                if i % 10 == 0:
                    os.rename(os.path.join(root, dir, file), os.path.join(val_sub_dir, file))
                elif i % 10 == 1:
                    os.rename(os.path.join(root, dir, file), os.path.join(test_sub_dir, file))
                else:
                    os.rename(os.path.join(root, dir, file), os.path.join(train_sub_dir, file))
        break

if __name__ == '__main__':
    split_dataset()