from turtle import forward
from pyrsistent import pbag
import torch
import torch.nn as nn

from .transformers.transformer import Transformer

class SeqModel(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.T = Transformer()
    
    def forward(self, x):
        attention = self.T(x)
        
        # Temporary Decoder
        pred = attention
        
        return pred