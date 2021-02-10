import os


class Config:
    data_dir = os.path.abspath('../data')
    train_data_dir = os.path.join(data_dir, 'image_arrays_train')
    test_data_dir = os.path.join(data_dir, 'image_arrays_test')
    submissions_dir = os.path.join(data_dir, '../' 'submissions')
    models_dir = os.path.join(data_dir, '../', 'models')
    bands_of_interest = ['S2_B5', 'S2_B4', 'S2_B3', 'S2_B2', 'CLIM_pr', 'CLIM_soil']
    band_names = [l.strip() for l in open(os.path.join(data_dir, 'bandnames.txt'), 'r').readlines()]
    base_model = 'catboost'
    lr = 1e-2

