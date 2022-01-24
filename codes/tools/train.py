import argparse
from sympy import im
import torch
from torch.utils.data import DataLoader
import torch.optim as optim
from torch.utils.tensorboard.writer import SummaryWriter
import torch.nn as nn
import tensorboard

import numpy as np
import random
import os
import sys
from tqdm import tqdm

sys.path.append('.')

from configs import parse_args
from utils.dataset import SeqData

if __name__ == '__main__':
    torch.set_printoptions(precision=None, threshold=4096, edgeitems=None, linewidth=None, profile=None)
    os.environ['CUDA_VISIBLE_DEVICES'] = '0'
    if not os.path.exists('./log'):
        os.mkdir('./log')
    if not os.path.exists('./checkpoints'):
        os.mkdir('./checkpoints')
    args = parse_args()
    print(args)
    writer = SummaryWriter(os.path.join('./log', args.name))
    
    trainset = SeqData(args)