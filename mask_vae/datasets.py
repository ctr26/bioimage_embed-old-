#  %%
import sys
from torch.utils.data import random_split, DataLoader
import glob
# Note - you must have torchvision installed for this example
from torch.utils.data import Dataset, DataLoader
from PIL import Image
import os
from scipy import ndimage
import matplotlib.pyplot as plt
import numpy as np
import torch
from torch import nn
from scipy.ndimage import convolve,sobel 

from scipy.interpolate import interp1d
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
import torch.optim as optim


class DSB2018(Dataset):
    def __init__(self, path_glob, transform=None):
        self.image_paths = glob.glob(path_glob, recursive=True)
        self.transform = transform

    def __getitem__(self, index):
        x = Image.open(self.image_paths[index])
        # if self.transform is not None:
        x = self.transform(x)

        return x

    def __len__(self):
        return len(self.image_paths)