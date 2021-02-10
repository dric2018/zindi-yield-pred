# acknowledgement : The code base is from the starter nb released by Johno W.
# starter code link :
# https://zindi.africa/competitions/cgiar-crop-yield-prediction-challenge/data/Starter_Notebook_CGIAR_Yield_Estimation.ipynb

import numpy as np
import os
import pandas as pd
from matplotlib import pyplot as plt
from .config import Config


def process_im(fid, folder=Config.train_data_dir):
    fn = f'{folder}/{fid}.npy'
    arr = np.load(fn)
    Config.bands_of_interest
    values = {}
    for month in range(12):
        # Bands of interest for this month
        bns = [str(month) + '_' + b for b in Config.bands_of_interest]
        # Index of these bands
        idxs = np.where(np.isin(Config.band_names, bns))
        vs = arr[idxs, 20, 20]  # Sample the im at the center point
        for bn, v in zip(bns, vs[0]):
            values[bn] = v
    return values


def show_samples(df: pd.DataFrame, data_dir: str):
    # Look at a sample:
    fid = df['Field_ID'].sample().values[0]
    fn = os.path.join(data_dir, f'{fid}.npy')  # File name based on Field_ID
    print(f'Loading {fn} as an array')
    arr = np.load(fn)  # Loading the data with numpy
    print('Array shape:', arr.shape)  # 360 bands, images 40 or 41px a side
    # Combine three bands for viewing
    rgb_jan = np.stack([arr[4], arr[3], arr[2]], axis=-1)
    # Scale band values to (0, 1) for easy image display
    rgb_jan = rgb_jan / np.max(rgb_jan)
    plt.imshow(rgb_jan)  # View with matplotlib

    return arr


def save_model(model_name, model, params: dict = None):
    path = os.path.join(Config.models_dir, model_name)
    try:
        model.save_model(fname=path, format='cbm', export_parameters=params)
        # print(f'[INFO] model saved as {path}')
        return path

    except Exception as ex:
        print(f"[ERROR] {ex}")
