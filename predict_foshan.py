# import os
# import time

# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# import torch
# from torchvision.transforms import transforms

# from src import u2net_full

# test_path = 'E:\\datasets\\building_seg\\DUTS-TE\\DUTS-TE-Image\\42.jpg'
# threshold = 0.5

# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# data_transform = transforms.Compose([
#     transforms.ToTensor(),
#     transforms.Resize(320),
#     transforms.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225))
# ])


