import pytest
import os
from torchvision import transforms
import torch

from mask_vae.datasets import DSB2018
from mask_vae.transforms import ImagetoDistogram, cropCentroid, DistogramtoImage, CropCentroidPipeline,CropToDistogramPipeline
from mask_vae.models import AutoEncoder, VAE, VQ_VAE
window_size = 96
train_dataset_glob = os.path.join(os.path.expanduser("~"),
                                  "data-science-bowl-2018/stage1_train/*/masks/*.png")
# test_dataloader_glob=os.path.join(os.path.expanduser("~"),
# "data-science-bowl-2018/stage1_test/*/masks/*.png")

transformer_crop = CropCentroidPipeline(window_size)
transformer_dist = CropToDistogramPipeline(window_size)

train_dataset = DSB2018(train_dataset_glob, transform=transformer_dist)


def test_models():
    # vae = AutoEncoder(1, 1)
    vae = VQ_VAE(channels=1)
    img = train_dataset[0].unsqueeze(0)
    loss, x_recon, perplexity = vae(img)
    z = vae.encoder(img)
    y_prime = vae.decoder(z)
    # print(f"img_dims:{img.shape} y:_dims:{x_recon.shape}")
    print(
        f"img_dims:{img.shape} x_recon:_dims:{x_recon.shape} z:_dims:{z.shape}")

