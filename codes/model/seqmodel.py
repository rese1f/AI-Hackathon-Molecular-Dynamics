from sympy import im
import torch
import torch.nn as nn
import torch.nn.functional as F

from .transformers.transformer import Transformer

class SeqModel(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.T = Transformer()
        self.fc1 = nn.Linear(3, 5)
        self.fc2 = nn.Linear(5, 1)
        
    def forward(self, cp, seq):
        attention = self.T(seq)

        # Temporary Decoder
        seq_feature = torch.mean(attention, dim=1)[:,0]
        fraction = torch.mean(seq, dim=1)[:,0]
        x = torch.stack([seq_feature, fraction, cp], dim=1)
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        x = F.relu(x)
        x = x[:,0]
        
        return x, attention