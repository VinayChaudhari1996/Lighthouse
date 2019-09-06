import torch
from torch import functional as F
import torch.nn as nn
import matplotlib.pyplot as plt

use_cuda = torch.cuda.is_available()
device = torch.device("cuda" if use_cuda else "cpu")

class Net(nn.Module):
    def __init__(self):
        super(Net,self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3,out_channels=32,kernel_size=7,padding=3)
        self.conv1_1 = nn.Conv2d(in_channels=32,out_channels=32,kernel_size=7,padding=3)
        
        self.conv2 = nn.Conv2d(in_channels=32,out_channels=64,kernel_size=7,padding=3)
        self.conv2_1 = nn.Conv2d(in_channels=64,out_channels=64,kernel_size=7,padding=3)
        
        self.conv3 = nn.Conv2d(in_channels=64,out_channels=128,kernel_size=5,padding=2)
        self.conv3_1 = nn.Conv2d(in_channels=128,out_channels=128,kernel_size=5,padding=2)
        
        self.conv4 = nn.Conv2d(in_channels=128,out_channels=256,kernel_size=5,padding=2)
        self.conv4_1 = nn.Conv2d(in_channels=256,out_channels=256,kernel_size=5,padding=2)
        
        self.conv5 = nn.Conv2d(in_channels=256,out_channels=512,kernel_size=5,padding=2)
        self.conv5_1 = nn.Conv2d(in_channels=512,out_channels=512,kernel_size=5,padding=2)
        
        self.fc1 = nn.Linear(in_features=512*7*7,out_features=1024)
        self.fc2 = nn.Linear(in_features=1024,out_features=1024)
        self.fc3 = nn.Linear(in_features=1024,out_features=512)
        self.out = nn.Linear(in_features=1024,out_features=5)
        
        self.dropout = nn.Dropout(0.5)
        
    def forward(self,x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv1_1(x))
        x = F.max_pool2d(x,kernel_size=2,stride=2)
        #print(x.shape)
        x = self.dropout(x)
        
        x = F.relu(self.conv2(x))
        x = F.relu(self.conv2_1(x))
        x = F.max_pool2d(x,kernel_size=2,stride=2)
        #print(x.shape)
        x = self.dropout(x)
        
        x = F.relu(self.conv3(x))
        x = F.relu(self.conv3_1(x))
        x = F.max_pool2d(x,kernel_size=2,stride=2)
        #print(x.shape)
        x = self.dropout(x)
        
        x = F.relu(self.conv4(x))
        x = F.relu(self.conv4_1(x))
        x = F.max_pool2d(x,kernel_size=2,stride=2)
        #print(x.shape)
        x = self.dropout(x)
        
        x = F.relu(self.conv5(x))
        x = F.relu(self.conv5_1(x))
        x = F.max_pool2d(x,kernel_size=2,stride=2)
        x = self.dropout(x)
        #print(x.shape)
        x = x.reshape(-1,512*7*7)
        #print(x.shape)
        x = F.relu(self.fc1(x))
        
        x = self.dropout(x)
        #x = F.relu(self.fc2(x))
        #x = F.relu(self.fc3(x))
        #print(x.shape)
        x = F.log_softmax(self.out(x),dim=1)
        #print(x.shape)
        return x
net = Net().to(device)
im = torch.randn(1, 1, 572, 572)
output = net(im)
