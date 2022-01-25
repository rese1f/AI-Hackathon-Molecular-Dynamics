import argparse
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
from model.seqmodel import SeqModel

if __name__ == '__main__':
    os.environ['CUDA_VISIBLE_DEVICES'] = '0'
    if not os.path.exists('./log'):
        os.mkdir('./log')
    if not os.path.exists('./checkpoints'):
        os.mkdir('./checkpoints')
    args = parse_args()
    print(args)
    writer = SummaryWriter(os.path.join('./log', args.name))
    
    model = SeqModel()
    if args.checkpoint:
        model.load_state_dict(torch.load(os.path.join('./checkpoints', args.checkpoint)))
    
    trainset = SeqData(args)
    train_iter = DataLoader(trainset,
                            batch_size=args.batch_size,
                            shuffle=True,
                            num_workers=0,
                            pin_memory=True)
    
    # optimizer = optim.SGD(model.parameters(), lr=args.lr, momentum=0.9, weight_decay=0.0005)
    
    print("Done Pre.")
    pbar = tqdm(total = args.epoch)
    
    ###################################
    # This Block is for dataloader test
    for p, seq, label in train_iter:
        print(p, seq, label)
        break
    ###################################
    
    for epoch in range(args.epoch):
        model.train()
        
        # TODO
        
        pbar.update(1)
        
    writer.close()
    torch.save(model.state_dict(), os.path.join('checkpoints', args.name+'.pth'))