from turtle import forward
import torch
import torch.nn as nn

class SeqLoss(nn.Module):
    def __init__(self):
        super().__init__()
        self.loss_func = nn.MSELoss()
    
    def forward(self, pred, label):
        loss = self.loss_func(pred, label)
        return loss