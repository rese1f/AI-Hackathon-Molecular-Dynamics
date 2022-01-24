import os
import numpy as np

import torch.utils.data as data


class SeqData(data.Dataset):
    def __init__(self, args) -> None:
        super().__init__()
        root_path = args.path
        datasets_path = list(args.dataset)
        datasets = list()
        for subset in datasets_path:
            subpath = os.path.join(root_path, 'dataset'+subset)
            f = open(subpath, 'r')
            
    
    def __getitem__(self, index):
        return
    
    def __len__(self):
        return