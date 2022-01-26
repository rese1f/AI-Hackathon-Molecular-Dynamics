import argparse
import torch
from torch.utils.data import DataLoader

import matplotlib.pyplot as plt
import numpy as np
import random
import os
import sys
sys.path.append('.')

from configs import parse_args
from utils.dataset import SeqData
from model.seqmodel import SeqModel

if __name__ == '__main__':
    os.environ['CUDA_VISIBLE_DEVICES'] = '0'
    if not os.path.exists('./log'):
        os.mkdir('./log')
    if not os.path.exists('./checkpoints'):
        os.mkdir('./checkpoints')
    args = parse_args()
    print(args)
    
    model = SeqModel()
    valset = SeqData(args)
    val_iter = DataLoader(valset,
                            batch_size=valset.__len__(),
                            shuffle=True,
                            num_workers=0,
                            pin_memory=True,
                            drop_last=True)
    
    if args.checkpoint:
        model.load_state_dict(torch.load(os.path.join('./checkpoints', args.checkpoint)))
    print("Done Pre.")
    
    model.eval()
    for cp, seq, label in val_iter:
        pred, _ = model(cp, seq)
        fraction = torch.mean(seq, dim=1)
    
    
    x = fraction.detach().numpy()
    p = pred.detach().numpy()
    g = label.detach().numpy()
    plt.scatter(x, p)
    # plt.scatter(x, g)
    plt.show()