import torch
import torch.utils.data as data

#TODO (example) Implement Custom Dataset

class MyDataset(data.Dataset):
    def __getitem__(self, index):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError
