import torch
import torch.nn as nn

class TrafficLSTM(nn.Module):
    def _init_(self, input_size, hidden_size, output_size, num_layers=2):
        super(TrafficLSTM, self)._init_()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out, _ = self.lstm(x)
        out = self.fc(out[:, -1, :])
        return out