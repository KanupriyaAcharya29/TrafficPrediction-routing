import torch
import torch.nn as nn
import torch.optim as optim
from gnn import TrafficGNN
from lstm import TrafficLSTM

def train_model():
    gnn = TrafficGNN(in_channels=3, hidden_channels=16, out_channels=8)
    lstm = TrafficLSTM(input_size=1, hidden_size=32, output_size=1)

    # Example training loop (using dummy data)
    criterion = nn.MSELoss()
    optimizer = optim.Adam(list(gnn.parameters()) + list(lstm.parameters()), lr=0.001)

    for epoch in range(5):
        x = torch.rand(10, 12, 1)   # [batch, seq_len, features]
        y = torch.rand(10, 1)
        pred = lstm(x)
        loss = criterion(pred, y)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        print(f"Epoch {epoch}, Loss {loss.item()}")

if _name_ == "_main_":
    train_model()