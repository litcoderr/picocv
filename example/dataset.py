import torch
import torch.utils.data as data
from torchvision.transforms import transforms

import os
from PIL import Image


class MyDataset(data.Dataset):
    def __init__(self):
        self.root = os.path.dirname(os.path.realpath(__file__))
        self.dataset_path = os.path.join(self.root, "small_dataset")

        # Parse class
        self.classes = os.listdir(self.dataset_path)
        self.class_index = {}
        for idx, class_name in enumerate(self.classes):
            self.class_index[class_name] = idx

        self.files = []
        for class_name in self.classes:
            for file_name in os.listdir(os.path.join(self.dataset_path, class_name)):
                temp = {}
                temp["path"] = os.path.join(self.dataset_path, class_name, file_name)
                temp["class"] = self.class_index[class_name]
                self.files.append(temp)

    def __getitem__(self, index):
        """
        WARNING: In order to use PICOCV, should return values in following format
        :param index: dataset index
        :return: tuple(image(tensor(3, width, height)), label(tensor)))
        """
        image_path = self.files[index]["path"]
        image_class = self.files[index]["class"]

        image = transforms.ToTensor()(Image.open(image_path))
        label = torch.Tensor([image_class])

        return image, label

    def __len__(self):
        return len(self.files)
