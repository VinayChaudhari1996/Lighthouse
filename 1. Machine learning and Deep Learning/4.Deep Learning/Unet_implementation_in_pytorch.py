class Net(nn.Module):
    def __init__(self):
        super(Net,self).__init__()
        self.conv_1 = nn.Sequential(
        nn.Conv2d(kernel_size=3,out_channels=64,in_channels=3),
        nn.ReLU(),
        nn.BatchNorm2d(64),
        nn.Conv2d(kernel_size=3,in_channels=64,out_channels=64),
        nn.ReLU(),
        nn.BatchNorm2d(64))
        self.max_pool_1 = nn.MaxPool2d(kernel_size=2) 

        self.conv_2 = nn.Sequential(
            nn.Conv2d(kernel_size=3,out_channels=128,in_channels=64),
            nn.ReLU(),
            nn.BatchNorm2d(128),
            nn.Conv2d(kernel_size=3,in_channels=128,out_channels=128),
            nn.ReLU(),
            nn.BatchNorm2d(128))
        self.max_pool_2 = nn.MaxPool2d(kernel_size=2)

        self.conv_3 = nn.Sequential(
            nn.Conv2d(kernel_size=3,out_channels=256,in_channels=128),
            nn.ReLU(),
            nn.BatchNorm2d(256),
            nn.Conv2d(kernel_size=3,out_channels=256,in_channels=256),
            nn.ReLU(),
            nn.BatchNorm2d(256))
        self.max_pool_3 = nn.MaxPool2d(kernel_size=2)

        self.bottleneck = nn.Sequential(
            nn.Conv2d(kernel_size=3,out_channels=512,in_channels=256),
            nn.ReLU(),
            nn.BatchNorm2d(512),
            nn.Conv2d(kernel_size=3,in_channels=512,out_channels=512),
            nn.ReLU(),
            nn.BatchNorm2d(512),
            nn.ConvTranspose2d(in_channels=512,out_channels=256,kernel_size=3,stride=2,padding=1,output_padding=1))

        self.conv_4 = nn.Sequential(
            nn.Conv2d(kernel_size=3,in_channels=512,out_channels=256),
            nn.ReLU(),
            nn.BatchNorm2d(256),
            nn.Conv2d(kernel_size=3,in_channels=256,out_channels=256),
            nn.ReLU(),
            nn.BatchNorm2d(256),
            nn.ConvTranspose2d(in_channels=256,out_channels=128,kernel_size=3,padding=1,output_padding=1,stride=2))

        self.conv_5 = nn.Sequential(
            nn.Conv2d(kernel_size=3,in_channels=256,out_channels=128),
            nn.ReLU(),
           # nn.BatchNorm1d(128),
            nn.Conv2d(kernel_size=3,in_channels=128,out_channels=128),
            nn.ReLU(),
            #nn.BatchNorm2d(128),
            nn.ConvTranspose2d(in_channels=128,out_channels=64,kernel_size=3,padding=1,stride=2,output_padding=1))

        self.final = nn.Sequential(
            nn.Conv2d(kernel_size=3,in_channels=128,out_channels=64),
            nn.ReLU(),
           # nn.BatchNorm1d(64),
            nn.Conv2d(kernel_size=3,in_channels=64,out_channels=64),
            nn.ReLU(),
            #nn.BatchNorm2d(64),
            nn.Conv2d(kernel_size=3,in_channels=64,out_channels=2,padding=1),
            nn.ReLU(),
            nn.BatchNorm2d(2))
    

    def crop_and_cat(self,up,bpass):
        c = (bpass.size()[2] - up.size()[2])//2
        bpass = F.pad(bpass,(-c,-c,-c,-c))
        return torch.cat([up,bpass],dim=1)

    def forward(self,x):
        encode_block_1 = self.conv_1(x)
       # print("CONV_1:",encode_block_1.shape)
        encode_pool_1 = self.max_pool_1(encode_block_1)
        #print("MAX:",encode_pool_1.shape)

        encode_block_2 = self.conv_2(encode_pool_1)
        #print("CONV_2:",encode_block_2.shape)
        encode_pool_2 = self.max_pool_2(encode_block_2)
        #print("MAX:",encode_pool_2.shape)

        encode_block_3 = self.conv_3(encode_pool_2)
        #print("CONV_3:",encode_block_3.shape)
        encode_pool_3 = self.max_pool_3(encode_block_3)
        #print("MAX:",encode_pool_3.shape)

        bottleneck = self.bottleneck(encode_pool_3)
        #print(bottleneck.shape)

        decode_layer_1 = self.crop_and_cat(bottleneck,encode_block_3)
        cat_layer_1 = self.conv_4(decode_layer_1)
        #print(cat_layer_1.shape)

        decode_layer_2 = self.crop_and_cat(cat_layer_1,encode_block_2)
        #print(decode_layer_2.shape)
        cat_layer_2 = self.conv_5(decode_layer_2)
        #print(cat_layer_2.shape)

        final = self.crop_and_cat(cat_layer_2,encode_block_1)
        final = self.final(final)
        #print(final.shape)
        return final
    
model = Net()
