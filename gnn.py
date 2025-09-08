import torch
import torch.nn as nn
from torch_geometric.nn import GCNConv

class TrafficGNN(nn.Module):
    def _init_(self, in_channels, hidden_channels, out_channels):
        super(TrafficGNN, self)._init_()
        self.conv1 = GCNConv(in_channels, hidden_channels)
        self.conv2 = GCNConv(hidden_channels, out_channels)

    def forward(self, x, edge_index):
        x = self.conv1(x, edge_index).relu()
        x = self.conv2(x, edge_index)
        return x