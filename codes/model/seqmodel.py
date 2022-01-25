from turtle import forward
import torch
import torch.nn as nn

from .transformers.transformer import Transformer

class SeqModel(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.T = Transformer()
    
    def forward(self, x):
        return self.T(x)