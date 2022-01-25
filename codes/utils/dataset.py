import os
import numpy as np

import torch.utils.data as data


class SeqData(data.Dataset):
    def __init__(self, args) -> None:
        super().__init__()
        root_path = args.path
        datasets_path = list(args.dataset)
        self.datasets = list()
        for subset_path in datasets_path:
            with open(os.path.join(root_path, 'dataset'+subset_path)) as f:
                for data in f.readlines():
                    data = np.array(list(map(float, data.split())))
                    self.datasets.append(data)
        self.datasets = np.array(self.datasets)
        
    def __getitem__(self, index):
        data = self.datasets[index].astype('float32')
        p, seq, label = data[0], data[1:-1].reshape(32,1), data[-1]
        return p, seq, label

    def __len__(self):
        return self.datasets.shape[0]